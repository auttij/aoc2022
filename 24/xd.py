from math import lcm

# from lib.file_handling import get_file

dirs = {">": 1, "<": -1, "^": -1j, "v": 1j, "": 0}


def main() -> None:
    with open('24/input2.txt') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    rows, cols = len(grid), len(grid[0])
    time_wrap = lcm(rows - 2, cols - 2)

    start, end = grid[0].index("."), grid[-1].index(".") + (len(grid) - 1) * 1j

    safe_times = {
        x + y * 1j: set(range(time_wrap)) for y in range(rows) for x in range(cols)
    }

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            position = x + y * 1j

            if cell == "#":
                safe_times[position] = set()
                continue

            if cell == ".":
                continue

            direction = dirs[cell]

            for t in range(time_wrap):
                safe_times[position].discard(t)

                position += direction
                # wrap within internal grid
                position = complex(
                    (position.real - 1) % (cols - 2) + 1,
                    (position.imag - 1) % (rows - 2) + 1,
                )

    time = bfs(start, end, safe_times, time_wrap, 0)
    print(time)
    time2 = bfs(end, start, safe_times, time_wrap, time)
    time3 = bfs(start, end, safe_times, time_wrap, time2)
    print(time3)


def bfs(
    start: complex,
    end: complex,
    safe_times: dict[complex, set[int]],
    time_wrap: int,
    start_time: int,
) -> int:
    queue = [(start, start_time)]
    seen = set()

    while queue:
        pos, time = queue.pop(0)

        if pos == end:
            return time

        if (pos, time) in seen:
            continue

        seen.add((pos, time))
        new_time = time + 1

        for direction in dirs.values():
            new_pos = pos + direction

            if new_pos in safe_times and (new_time % time_wrap) in safe_times[new_pos]:
                queue.append((new_pos, new_time))

    raise ValueError("No path found")


if __name__ == "__main__":
    main()
