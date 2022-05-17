from sudoku.core.iterators import *

from copy import deepcopy
import itertools

class sudoku_grid:
    str_grid = \
"""
+-----------+-----------+-----------+
| 0   0   0 | 0   0   0 | 0   0   0 |
|           |           |           |
| 0   0   0 | 0   0   0 | 0   0   0 |
|           |           |           |
| 0   0   0 | 0   0   0 | 0   0   0 |
+-----------+-----------+-----------+
| 0   0   0 | 0   0   0 | 0   0   0 |
|           |           |           |
| 0   0   0 | 0   0   0 | 0   0   0 |
|           |           |           |
| 0   0   0 | 0   0   0 | 0   0   0 |
+-----------+-----------+-----------+
| 0   0   0 | 0   0   0 | 0   0   0 |
|           |           |           |
| 0   0   0 | 0   0   0 | 0   0   0 |
|           |           |           |
| 0   0   0 | 0   0   0 | 0   0   0 |
+-----------+-----------+-----------+
"""

    def __init__(self, grid: list[int] = [0] * 81) -> None:
        for i in grid:
            if i > 9:
                raise ValueError(
                    "A sudoku grid must contain only numbers between 1 and " +
                    "9, or 0 (if the corresponding cell is empty)."
                )

        self.grid = grid

    def __str__(self) -> str:
        ret     = ""
        grid_it = iter(self.grid)

        for i in self.str_grid:
            if i == "0":
                ret += str(next(grid_it))
            else:
                ret += i

        return ret

    def get_column_iter(self, n: int) -> column_iterator:
        return column_iterator(itertools.islice(iter(self.grid), n % 9, None))

    def get_row_iter(self, n: int) -> row_iterator:
        return row_iterator(
            itertools.islice(iter(self.grid), (n // 9) * 9, None)
        )

    def get_square_iter(self, n: int) -> square_iterator:
        return square_iterator(
            itertools.islice(
                iter(self.grid), (n // 27) * 27 + ((n % 9) // 3) * 3, None
            )
        )

    def is_in_column(self, value: int, i: int) -> bool:
        if value > 9:
            return False
        else:
            return value in self.get_column_iter(i)

    def is_in_row(self, value: int, i: int) -> bool:
        if value > 9:
            return False
        else:
            return value in self.get_row_iter(i)

    def is_in_square(self, value: int, i: int) -> bool:
        if value > 9:
            return False
        else:
            return value in self.get_square_iter(i)

    def is_empty(self) -> bool:
        for i in self.grid:
            if i != 0:
                return False

        return True

    def is_finished(self) -> bool:
        for val in range(1, 10):
            for i in range(9):
                if not self.is_in_column(val, i):
                    return False

                if not self.is_in_row(val, i):
                    return False

                if not self.is_in_square(val, 27 * (i // 3) + 3 * (i % 3)):
                    return False

        return True

    def get_empty_cells(self) -> list[int]:
        ret = []

        for i in range(len(self.grid)):
            if self.grid[i] == 0:
                ret.append(i)

        return ret

    def get_number_of_empty_cells(self) -> int:
        counter = 0

        for i in self.grid:
            if i == 0:
                counter += 1

        return counter

    def solve(self) -> None:
        tmp = self

        allowed_values = {}

        for i in tmp.get_empty_cells():
            for val in range(1, 10):
                if (
                    not tmp.is_in_column(val, i) and
                    not tmp.is_in_row(val, i) and
                    not tmp.is_in_square(val, i)
                ):

                    allowed_values.setdefault(i, []).append(val)

        selected_cells = []

        for (i, allowed) in allowed_values.items():
            selected_cells.append([i, iter(allowed), iter(allowed)])

        i = 0

        while i != len(selected_cells):
            grid_index, _, allowed_begin = selected_cells[i]

            try:
                val = next(selected_cells[i][1])

                if (
                    not tmp.is_in_column(val, grid_index) and
                    not tmp.is_in_row(val, grid_index) and
                    not tmp.is_in_square(val, grid_index)
                ):

                    tmp.grid[grid_index] = val

                    i += 1
            except StopIteration:
                if i == 0:
                    raise RuntimeError("The sudoku has no solution.")
                else:
                    selected_cells[i][1] = deepcopy(allowed_begin)
                    tmp.grid[grid_index] = 0

                    i -= 1

        if not tmp.is_finished():
            raise RuntimeError("The sudoku has no solution.")

        self = tmp
