def count_loop_positions(filename):
    # Read the map data from the file
    with open(filename, 'r') as file:
        map_data = file.read().strip()

    # Parse the map into a grid
    grid = [list(row) for row in map_data.split("\n")]
    rows, cols = len(grid), len(grid[0])

    # Define directions and find the starting position
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    guard_pos = None
    direction = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                direction = directions[grid[r][c]]
                break
        if direction:
            break

    # Function to turn the guard 90 degrees to the right
    def turn_right(current_dir):
        dir_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # ^ > v <
        index = dir_list.index(current_dir)
        return dir_list[(index + 1) % 4]

    # Function to simulate the guard's movement
    def simulate(grid, start_pos, start_dir):
        guard_pos = start_pos
        direction = start_dir
        visited = set()

        while True:
            # Compute next position
            next_pos = (guard_pos[0] + direction[0], guard_pos[1] + direction[1])

            # Check if the guard leaves the grid
            if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
                return False  # Guard exits the grid

            # Check if next position is an obstacle
            if grid[next_pos[0]][next_pos[1]] == "#":
                direction = turn_right(direction)
            else:
                # Move to the next position
                guard_pos = next_pos
                if guard_pos in visited:
                    return True  # Guard enters a loop
                visited.add(guard_pos)

    # Count positions where an obstruction causes a loop
    loop_positions = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "." and (r, c) != guard_pos:
                # Place a temporary obstruction
                grid[r][c] = "#"
                if simulate(grid, guard_pos, direction):
                    loop_positions += 1
                # Remove the temporary obstruction
                grid[r][c] = "."

    return loop_positions


# Example usage
filename = "Lists/data6.txt"  # Replace with your file name
result = count_loop_positions(filename)
print(f"Number of positions to place an obstruction: {result}")
