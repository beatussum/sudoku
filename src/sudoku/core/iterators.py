from collections.abc import Iterator
from typing import TypeVar

__all__ = ["column_iterator", "row_iterator", "square_iterator"]

T = TypeVar("T")

class column_iterator:
    def __init__(self, iter: Iterator[T]) -> None:
        self.iter  = iter
        self.start = True

    def __iter__(self: "column_iterator") -> "column_iterator":
        return self

    def __next__(self) -> T:
        if not self.start:
            for _ in range(8):
                next(self.iter)
        else:
            self.start = False

        return next(self.iter)

class row_iterator:
    def __init__(self, iter: Iterator[T]) -> None:
        self.iter    = iter
        self.counter = -1

    def __iter__(self: "row_iterator") -> "row_iterator":
        return self

    def __next__(self) -> T:
        if self.counter == 8:
            raise StopIteration

        self.counter += 1

        return next(self.iter)

class square_iterator:
    def __init__(self, iter: Iterator[T], counter: int = -1) -> None:
        self.iter    = iter
        self.counter = counter

    def __iter__(self: "square_iterator") -> "square_iterator":
        return self

    def __next__(self) -> T:
        if self.counter == 8:
            raise StopIteration

        self.counter += 1

        if ((self.counter % 3) == 0) and (self.counter != 0):
            for _ in range(6):
                next(self.iter)

        return next(self.iter)
