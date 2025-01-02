def predict_guard_path_from_file(filename):
    # Read the map data from the file
    try:
        with open(filename, 'r') as file:
            map_data = file.read().strip()
            if not map_data:
                print("The file is empty!")
                return
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return

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
                grid[r][c] = "."  # Replace guard symbol with empty space
                break
        if direction:
            break

    # Function to turn the guard 90 degrees to the right
    def turn_right(current_dir):
        dir_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # ^ > v <
        index = dir_list.index(current_dir)
        return dir_list[(index + 1) % 4]

    # Set to track visited positions
    visited = set()
    visited.add(guard_pos)

    # Simulate the guard's movement
    while True:
        # Compute next position
        next_pos = (guard_pos[0] + direction[0], guard_pos[1] + direction[1])

        # Check if the guard leaves the grid
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        # Check if next position is within bounds and not an obstacle
        if grid[next_pos[0]][next_pos[1]] == ".":
            guard_pos = next_pos
            visited.add(guard_pos)
        else:
            # Turn right if there's an obstacle
            direction = turn_right(direction)

    # Return the number of distinct positions visited
    return len(visited)


# Example usage
filename = "Lists/data6.txt"  # Replace with your file name
result = predict_guard_path_from_file(filename)

if result is not None:
    print(f"Number of distinct positions visited: {result}")
