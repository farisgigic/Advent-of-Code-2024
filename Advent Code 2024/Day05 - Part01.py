def parse_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines() # citamo fajlove kroz linije

    rules = []
    updates = []
    parsing_rules = True

    for line in lines:
        line = line.strip() # brisanje whitespace karaktere, tab karaktere (\t) i sve \n
        if not line:  # preskacemo prazne linije
            continue
        if parsing_rules:
            if "|" in line:  # Parse rules
                x, y = map(int, line.split("|"))
                rules.append((x, y))
            else:
                parsing_rules = False
        if not parsing_rules:  # Parse updates
            updates.append(list(map(int, line.split(","))))

    return rules, updates


def is_correct_order(update, rules):

    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def middle_page(update):

    return update[len(update) // 2]



filename = ("Lists/data5.txt")
rules, updates = parse_file(filename)

correct_updates = []
for update in updates:
    if is_correct_order(update, rules):
        correct_updates.append(update)

# Calculate the sum of middle pages
middle_sum = sum(middle_page(update) for update in correct_updates)

# Output the result
print("Sum of middle pages:", middle_sum)
