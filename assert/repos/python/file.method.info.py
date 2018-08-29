#! File 类型的对象其所属类名并不是 File, 实际上是TextIOWrapper, BufferedReader, BufferedWriter, BufferedRandom, StringIO, BytesIO 中的一种. 此处仅为说明示例.
class TextFile():
    def close(self):
        """关闭文件"""
        return
    def read(self, size=-1):
        """读取指定 size 文本文件内容到内存中, 若 size 为负数则读取至 EOF"""
        return "所有读取到的字符串"
    def readline(self, size=-1):
        """读取一行中指定 size 的文本文件内容到内存中, 若 size 为负数或超过本行长度则读取至换行符, 否则读取规定长度的字符串. 返回这行字符串"""
        return "一行字符串, 若读取到行的末尾, 则包含换行符\n"
    def readlines(self, size=-1):
        """读取指定 size 的文本文件内容到内存中, 若 size 为负数则读取至 EOF. 将每行内容(包括换行符)存储到列表中. 若 size 为正数, 则读取规定长度的字符, 直到最近的下一个换行符, 存储到列表中. 返回这个列表. """
        return list("读取到的一行\n", "读取到的下一行\n", "读取到的最后一行\n", "")
    def write(self, str):
        """将指定字符串 str 写入文件. 返回写入的字节数"""
        return len(str)
    def seek(self, cookie, whence=0):
        """移动文件读写指针, 由参考点向右移动 cookie 个字符.
whence: 0, 文件开头; 1, 当前位置; 2, 文件末尾
对于文本文件, 只允许从文件开头向右移动(cookie >= 0, whence == 0), 唯一的例外是移动到文件末尾 seek(0, 2). 返回从文件开头到目的地的字符数.
"""

class BinaryFile():
    def close(self):
        """关闭文件"""
        return
    def read(self):
        pass

