def parse_map(map_lines):
    """Parse the map and return antenna positions grouped by frequency."""
    antennas = {}
    for y, line in enumerate(map_lines):
        for x, char in enumerate(line.strip()):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def calculate_antinodes(antennas):
    """Calculate all unique antinodes based on antenna positions."""
    antinodes = set()

    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Check for antinodes
                dx, dy = x2 - x1, y2 - y1

                # Antinode on the near side
                near_x, near_y = x1 - dx, y1 - dy
                if 0 <= near_x < map_width and 0 <= near_y < map_height:
                    antinodes.add((near_x, near_y))

                # Antinode on the far side
                far_x, far_y = x2 + dx, y2 + dy
                if 0 <= far_x < map_width and 0 <= far_y < map_height:
                    antinodes.add((far_x, far_y))

    return antinodes

# Example Input
map_lines = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............",
]

# Parse the map and calculate dimensions
antennas = parse_map(map_lines)
map_width = len(map_lines[0])
map_height = len(map_lines)

# Calculate antinodes
unique_antinodes = calculate_antinodes(antennas)

# Output the result
print(f"Total unique antinode locations: {len(unique_antinodes)}")
