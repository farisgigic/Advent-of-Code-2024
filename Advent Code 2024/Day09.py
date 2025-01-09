def parse_disk_map(disk_map):
    if len(disk_map) % 2 != 0:
        raise ValueError("Disk map length must be even.")

    result = []
    file_id = 0
    for i in range(0, len(disk_map), 2):
        file_len = int(disk_map[i])
        free_space = int(disk_map[i + 1])
        result.extend([file_id] * file_len)  # Add file blocks
        result.extend(['.'] * free_space)  # Add free space
        file_id += 1
    return result


def compact_disk(disk):
    compacted = []
    for block in disk:
        if block != '.':
            compacted.append(block)
    compacted.extend(['.'] * (len(disk) - len(compacted)))
    return compacted


def calculate_checksum(disk):
    checksum = 0
    for position, block in enumerate(disk):
        if block != '.':
            checksum += position * int(block)
    return checksum


def main():
    try:
        with open("Lists/data9.txt", "r") as file:
            disk_map = file.read().strip()

        if not disk_map:
            raise ValueError("Disk map cannot be empty.")

        disk = parse_disk_map(disk_map)
        print("Initial Disk:", ''.join(map(str, disk)))

        disk = compact_disk(disk)
        print("Compacted Disk:", ''.join(map(str, disk)))

        checksum = calculate_checksum(disk)
        print("Checksum:", checksum)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
