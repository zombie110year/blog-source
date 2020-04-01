---
title: 「Rust每日一库」rand 随机数
date: 2020-03-31 21:07:56
tags:
  - rust
categories:
  - Rust每日一库
description: |
  rand 是 Rust 的随机数生成库。
---

- [rand | GitHub](https://github.com/rust-random/rand)
- [The Rust Rand Book](https://rust-random.github.io/book/) 讲述 Rust 中随机数的处理方法

rand 提供了随机数生成器，可以生成数字或其他任意类型，也提供了随机性算法。

# 快速入门

> 在 `Cargo.toml` 中添加:
>
> ```toml
> rand = "^0.7"
> ```

如果不希望只将需要的要素引入作用域，那么可以使用 `use rand::prelude::*;` 将常用要素
一次引入。

## 生成任意类型随机数

使用 `rand::random` 函数，此为泛型函数，可以生成受支持的类型的随机数据：

```rust
// 内置类型
let a: i32 = rand::random();
println!("{}", a);
let a: u128 = rand::random();
println!("{}", a);
let a: f64 = rand::random();
println!("{}", a);
// 静态数组
let a: [i32; 8] = rand::random();
println!("{:?}", a);
```

- `rand::random` 其实是 `thread_rng().gen()` 的别名。
- 浮点数的随机数生成域为 `[0, 1)`。

如果要生成一个数组（容器）的随机数，也可以使用 `fill_bytes`：

```rust
// 引入作用域以提供 fill_bytes 方法
use rand::RngCore;
fn main() {
    // let mut arr: [u8; 10] = Default::default();
    let mut arr = [0u8; 10];
    let mut rng = rand::thread_rng();
    rng.fill_bytes(&mut arr);
    println!("{:?}", arr);
}
```

## 随机数生成器种子

## 生成指定范围的随机数

需要将 `rand::rngs::Rng` 引入到作用域中：

```rust
let mut rng = rand::thread_rng();
// 内置类型
let a: i32 = rng.gen_range(-2, 2);
println!("{}", a);
let a: u128 = rng.gen_range(0, 2);
println!("{}", a);
let a: f64 = rng.gen_range(-10_f64, 0_f64);
println!("{}", a);
```

- 数组不能使用 `gen_range` 方法。

或者，可以使用 `rand::distributions::` 中的

## 随机性方法

### shuffle 洗牌算法

对集合使用 shuffle 方法，需要该集合实现了 `rand::seq::SliceRandom` 特性。

-   将 `rand::seq::SliceRandom` 引入作用域，`[T; N]` 数组和 `Vec<T>` 向量等都已实现此特性。
-   将随机数生成器的 **可变引用** 传递给 `.shuffle` 方法。

```rust
use rand::seq::SliceRandom;

fn main() {
    let mut rng = rand::thread_rng();
    let mut a: [i32; 6] = [1, 2, 3 ,4 ,5 ,6];
    a.shuffle(&mut rng);
    println!("{:?}", a);
}
```

另有一 `partial_shuffle` 方法，可以限定洗牌的次数。

```rust
use rand::seq::SliceRandom;

fn main() {
    let mut rng = rand::thread_rng();
    let mut a: Vec<i32> = vec![1, 2, 3, 4, 5, 6];
    // 只洗一次
    a.partial_shuffle(&mut rng, 1);
    println!("{:?}", a);
}
```

### choose 随机选择

`choose` 方法可以对实现了 `rand::seq::{SliceRandom, IteratorRandom}` 之一的任何集合使用。

```rust
use rand::seq::IteratorRandom;

fn main() {
    let mut rng = rand::thread_rng();
    // 这是一个迭代器
    let a = "abcdefg".chars();
    // choose 方法返回 Option<T>
    if let Some(ch) = a.choose(&mut rng) {
        println!("{}", ch);
    } else {
        println!("未选择");
    }
}
```

`choose_multiple` 可以选择一定数目的元素（$m \choose n$），返回 `Vec<T>`。

```rust
use rand::seq::IteratorRandom;

fn main() {
    let mut rng = rand::thread_rng();
    let a = "abcdefg".chars();
    let ch = a.choose_multiple(&mut rng, 3);
    println!("{:?}", ch);
}
```

`choose_weighted` 在选择时会考虑权重，只为 `SliceRandom` 实现。

```rust
use rand::seq::SliceRandom;

fn main() {
    let mut rng = rand::thread_rng();
    let w: [i32; 7] = [9, 1, 1, 1, 1, 1, 1];
    // 按 9:1:1:1:1:1:1 的概率分布获取字母
    let chars = "abcdefg".chars();
    let choice: Vec<(char, &i32)> = chars.zip(w.iter()).collect();
    let ch = choice
        .choose_weighted(&mut rng, |pair: &(char, &i32)| *pair.1)
        .unwrap()
        .0;
    println!("{}", ch);
}
```

# 模块详解

## distributions

<!-- TODO
### Standard 标准分布
 -->

### Weighted 权重分布

```rust
// 引入 trait 到作用域，为随机数分布提供 sample（取样）方法
use rand::distributions::Distribution;
use rand::distributions::WeightedIndex;

fn main() {
    let mut rng = rand::thread_rng();
    let w: [i32; 7] = [9, 1, 1, 1, 1, 1, 1];
    let dist = WeightedIndex::new(w.iter()).unwrap();
    // 按 9:1:1:1:1:1:1 的概率分布得到 0~6 的 usize
    let sample = dist.sample(&mut rng);
    println!("{}", &sample);

    let mut chars = "abcdefg".chars();
    println!("{}", chars.nth(sample).unwrap());
}
```

<!-- TODO
## seq 处理序列 -->

## rngs 随机数生成器（算法）

参考 https://rust-random.github.io/book/guide-rngs.html

# 为任意类型生成随机数据

rand 库可以为将 `rand::distributions::Distribution` 实现到
`rand::distributions::Standard` trait 的类型提供便捷的随机值方法：

```rust
use rand::distributions::{Distribution, Standard};
use std::fmt::Debug;

#[derive(Debug)]
struct T {
    x: i32,
    y: i32,
    z: i32,
}

impl Distribution<T> for Standard {
    fn sample<R: rand::Rng + ?Sized>(&self, rng: &mut R) -> T {
        T {
            x: rng.gen(),
            y: rng.gen(),
            z: rng.gen(),
        }
    }
}

fn main() {
    let t: T = rand::random();
    println!("{:?}", t);
}
```

<!-- TODO # 其他 rand crates

曾经有部分功能是 rand 所内置的，随后它们被拆分成单独的 crate 发布了。

-->
