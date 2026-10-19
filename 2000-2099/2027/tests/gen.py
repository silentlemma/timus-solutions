"""Usage: seed mode. Full official tick and register bounds.
Modes: no_output_loop, zero_output_cycle, positive_read_cycle, negative_read_max_inputs,
registers_max_board, positive_overflow, negative_overflow, max_input_halt, max_board_output.
"""

import random
import string
import sys

SIDE = 100
MAX_INPUT = 100000
VALUE_LIMIT = 100000


def generate(seed, mode):
    rng = random.Random(seed)
    values = [0]
    if mode == "no_output_loop":
        grid = [">v", "^<"]
    elif mode in ("zero_output_cycle", "positive_overflow", "negative_overflow"):
        opcode = {"zero_output_cycle": "!", "positive_overflow": "+", "negative_overflow": "-"}[
            mode
        ]
        grid = [">" + opcode * (SIDE - 2) + "v", "^" + opcode * (SIDE - 2) + "<"]
    elif mode in ("positive_read_cycle", "negative_read_max_inputs"):
        grid = [">" + "?!" * ((SIDE - 2) // 2) + "v", "^" + "!?" * ((SIDE - 2) // 2) + "<"]
        values = [VALUE_LIMIT]
        if mode == "negative_read_max_inputs":
            grid = [">" + "?!" * ((SIDE - 2) // 2) + "v"]
            for row in range(1, SIDE - 1):
                left = "?" if row % 2 == 0 else "!"
                right = "?" if row % 2 == 1 else "!"
                grid.append(left + "." * (SIDE - 2) + right)
            grid.append("^" + "!?" * ((SIDE - 2) // 2) + "<")
            values = [i - MAX_INPUT // 2 for i in range(MAX_INPUT)]
            values[-1] = -VALUE_LIMIT
    elif mode in ("registers_max_board", "max_board_output", "max_input_halt"):
        letters = (string.ascii_uppercase * SIDE)[: SIDE - 2]
        fill = letters if mode == "registers_max_board" else "!" * (SIDE - 2)
        grid = [">" + fill + "v"]
        for row in range(SIDE - 2):
            left = (
                string.ascii_uppercase[row % len(string.ascii_uppercase)]
                if mode == "registers_max_board"
                else "!"
            )
            right = (
                string.ascii_uppercase[-1 - row % len(string.ascii_uppercase)]
                if mode == "registers_max_board"
                else "!"
            )
            grid.append(left + "." * (SIDE - 2) + right)
        grid.append("^" + fill + "<")
        if mode != "max_board_output":
            values = [rng.randint(-VALUE_LIMIT, VALUE_LIMIT) for _ in range(MAX_INPUT)]
        if mode == "max_input_halt":
            grid[0] = "#" + grid[0][1:]
    else:
        raise ValueError("unknown mode")
    return (
        f"{len(grid)} {len(grid[0])}\n"
        + "\n".join(grid)
        + "\n"
        + str(len(values))
        + "\n"
        + "".join(str(value) + "\n" for value in values)
    )


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
