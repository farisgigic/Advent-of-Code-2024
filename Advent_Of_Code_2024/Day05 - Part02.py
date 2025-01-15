from collections import defaultdict, deque


def parse_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    rules = []
    updates = []
    parsing_rules = True

    for line in lines:
        line = line.strip()
        if not line:  # Skip empty lines
            continue
        if parsing_rules:
            if "|" in line:  # Parse rules
                x, y = map(int, line.split("|"))
                rules.append((x, y))
            else:
                parsing_rules = False
        if not parsing_rules:
            updates.append(list(map(int, line.split(","))))

    return rules, updates


def is_correct_order(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def correct_order(update, rules):
    # Create a graph from the rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree[x] += 0  # Ensure all nodes are in in_degree

    # Perform topological sorting
    queue = deque(node for node in update if in_degree[node] == 0)
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Add remaining nodes (not in rules)
    remaining = [p for p in update if p not in sorted_update]
    sorted_update.extend(remaining)

    return sorted_update


def middle_page(update):
    return update[len(update) // 2]


file_path = input("Enter the path to your .txt file: ").strip()
rules, updates = parse_file(file_path)

incorrect_updates = []
corrected_updates = []

for update in updates:
    if not is_correct_order(update, rules):
        incorrect_updates.append(update)
        corrected_updates.append(correct_order(update, rules))

# Calculate the sum of middle pages for corrected updates
middle_sum = sum(middle_page(update) for update in corrected_updates)

# Output the result
print("Sum of middle pages for corrected updates:", middle_sum)
