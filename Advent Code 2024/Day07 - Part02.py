from itertools import product

def evaluate_expression_with_concat(numbers, operators):
    """Evaluate the expression left-to-right with +, *, and || operators."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += numbers[i + 1]
        elif op == "*":
            result *= numbers[i + 1]
        elif op == "||":
            result = int(str(result) + str(numbers[i + 1]))
    return result

def parse_and_calculate_with_concat(filename):
    """Parse the input file and calculate the total calibration result with concatenation."""
    total_calibration_result = 0

    with open(filename, "r") as file:
        for line in file:
            # Parse each line
            target, numbers = line.strip().split(":")
            target = int(target)
            numbers = list(map(int, numbers.split()))

            # Generate all possible operator combinations
            num_operators = len(numbers) - 1
            all_combinations = product(["+", "*", "||"], repeat=num_operators)

            # Check if any combination matches the target
            valid = False
            for operators in all_combinations:
                if evaluate_expression_with_concat(numbers, operators) == target:
                    valid = True
                    break

            # If valid, add the target to the total result
            if valid:
                total_calibration_result += target

    return total_calibration_result

# Example usage
filename = "Lists/data7.txt"  # Replace with your file name
result = parse_and_calculate_with_concat(filename)
print(f"Total calibration result: {result}")
