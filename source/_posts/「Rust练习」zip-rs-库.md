---
layout: posts
title: 「Rust练习」zip-rs 库
date: 2020-02-26 16:28:26
tags:
  - rust
  - zip
categories: 记录
description: |
  Rust 的 zip-rs 库提供了创建、写入、读取 Zip 格式归档的功能。
---

[mvdnes/zip-rs | GitHub](https://github.com/mvdnes/zip-rs)

# zip-rs 的 README 要点

> 由于无人关注和作者时间稀缺，此仓库的维护不活跃。
> 目前此仓库的最新版本是 `0.5.5` 版。

支持压缩算法：

- stored（仅存储）
- deflate
- bzip2

目前不支持的 zip 扩展：

- 加密
- 分片

## 使用方法

在 `Cargo.toml` 文件中添加依赖：`zip = "^0.5"`。
如果要取消默认特性，需要

```toml
zip = { version = "^0.5", default-features = false }
```

拥有的特性有：

- `deflate`：zip 文件默认的压缩算法
- `bzip2`：bzip2 压缩算法
- `time`：启用 crate `time`（已废弃）的特性

默认情况下，以上特性全部启用。

# 使用实例

## 创建 zip 文件

```rust
// 必须导入 Write, Read 等 trait 才能调用对应的 write_* 等方法
use std::io::prelude::*;

fn main() {
    // 创建文件
    let filepath = std::path::Path::new("test.zip");
    let zipfile = std::fs::File::create(filepath).unwrap();
    // 用创建的文件实例化写入器
    let mut zipwriter = zip::ZipWriter::new(zipfile);
    // 设置注释，默认 "zip-rs"
    // 字符编码是 UTF-8
    zipwriter.set_comment("示例 zip 压缩文件");
    // 用链式调用风格配置 zip 选项，一共有三种
    let options = zip::write::FileOptions::default()
        // 压缩算法
        .compression_method(zip::CompressionMethod::Deflated)
        // Unix 权限描述符
        .unix_permissions(0o744_u32)
        // 最后修改时间
        .last_modified_time(zip::DateTime::from_date_and_time(2020, 1, 1, 0, 0, 0).unwrap());

    // 创建一个文件对象
    zipwriter.start_file("README.md", options).unwrap();
    // 向这个文件对象中写入内容
    zipwriter
        .write_all(b"Hello World!\n")
        .expect("无法写入 README.md");

    // 创建一个目录
    // Default::default 指向 FileOption 的 default 方法
    zipwriter.add_directory("opt", Default::default()).unwrap();
    // 在这个目录中添加文件
    zipwriter
        .start_file("opt/hello.rs", Default::default())
        .unwrap();
    zipwriter.write_all(b"println!(\"Hello World\")").unwrap();

    // !调用 finish 方法才会将 zip 文件持久化到文件系统中
    // 会返回之前传递的文件对象
    let _zipfile = zipwriter.finish().unwrap();
}
```

## 解压文件


```rust
use std::io::prelude::*;

fn main() {
    // 打开文件并实例化读取器
    let filepath = std::path::Path::new("test.zip");
    let zipfile = std::fs::File::open(filepath).expect("无法打开文件");
    let mut zipreader = zip::ZipArchive::new(zipfile).unwrap();

    // 读取压缩文件注释
    let comment: &[u8] = zipreader.comment();
    println!("注释：{}", String::from_utf8(comment.to_vec()).unwrap());

    // 列举压缩包中的文件
    for i in 0..zipreader.len() {
        // 实现了 Read trait，可能是文件，也可能是目录
        let mut entry = zipreader.by_index(i).unwrap();
        // 也可以通过压缩包内的路径来获取
        // let mut entry = zipreader.by_name("README.md").unwrap();
        if entry.is_file() {
            let path = entry.sanitized_name();
            println!(
                "文件：{}，大小：{} 字节",
                path.as_path().display(),
                entry.size()
            );
            // 在文件系统中创建文件
            if let Some(parent) = path.parent() {
                if !parent.exists() {
                    std::fs::create_dir_all(parent).unwrap();
                }
            }
            let mut outfile = std::fs::File::create(path).unwrap();
            // 写入内容
            std::io::copy(&mut entry, &mut outfile).unwrap();
        } else if entry.is_dir() {
            let path = entry.sanitized_name();
            println!("目录：{}", path.as_path().display());
            // 创建目录
            std::fs::create_dir_all(path).unwrap();
        } else {
            let path = entry.sanitized_name();
            println!("不知道什么玩意：{}", path.as_path().display());
        }
    }
}
```
