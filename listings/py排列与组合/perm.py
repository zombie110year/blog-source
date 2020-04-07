from typing import *

T = TypeVar("T")


def perm(iterable: Iterable[T], r: Optional[int] = None) -> Iterator[tuple]:
    """输入一个可迭代对象 iterable 和 排列长度，返回可迭代的排列"""
    if r is None:
        # 全排列
        yield from full_perm(iterable)
    else:
        # 指定长度的排列
        yield from partial_perm(iterable, r)


def full_perm(iterable: Iterable[T]) -> Iterable[tuple]:
    "全排列"
    pass


def partial_perm(iterable: Iterable[T], r: int) -> Iterable[tuple]:
    "指定长度的排列"
    pass
