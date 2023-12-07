"""
Advent of Code Day Three

The engine schematic (your puzzle input) consists of a visual 
representation of the engine. There are lots of numbers and 
symbols you don't really understand, but apparently any number 
adjacent to a symbol, even diagonally, is a "part number" and 
should be included in your sum. (Periods (.) do not count as a symbol.)
Of course, the actual engine schematic is much larger. What is 
the sum of all of the part numbers in the engine schematic?

@author: Jordan Sinclair
"""

# Get data
lines = open("data.txt").read().splitlines()

# Stores the resulting sum
result = 0

# Number of columns
n = len(lines)
# Number of rows
m = len(lines[0])

# Function to check if a cell contains a symbol or not
def is_symbol(i, j):
    if not (0 <= i < n and 0 <= j < m):
        return False

    return lines[i][j] != "." and not lines[i][j].isdigit()

def get_value(i, j):
    num = ""

    # Traverse left
    left = j
    while left >= 0 and lines[i][left].isdigit():
        num = lines[i][left] + num
        left -= 1

    # Traverse right
    right = j + 1
    while right < len(lines[i]) and lines[i][right].isdigit():
        num = num + lines[i][right]
        right += 1

    return int(num) if num else 0  # Return 0 if num is empty


def is_gear(i, j, processed_indices, processed_values):
    if not (0 <= i < n and 0 <= j < m) or lines[i][j] != "*":
        return 0

    # Check if adjacent to two numbers
    nums = []
    for x in range(max(0, i-1), min(n, i+2)):
        for y in range(max(0, j-1), min(m, j+2)):
            index = (x, y)
            value = get_value(x, y)
            if index != (i, j) and lines[x][y].isdigit() and index not in processed_indices and value not in processed_values:
                nums.append((value, index))
                processed_indices.add(index)
                processed_values.add(value)

    nums.sort(key=lambda x: x[1])  # Sort by column index
    nums.sort(key=lambda x: x[0])  # Sort by value
    
    if len(nums) == 2:
        return nums[0][0] * nums[1][0]
    else:
        return 0

    
if __name__ == "__main__":
    for i, line in enumerate(lines):
        start = 0

        j = 0

        while j < m:
            start = j # Updates start
            num = "" # Variable to store the num string
            
            # Loops until line[j] is no longer a digit or until the end of the row
            while j < m and line[j].isdigit():
                num += line[j]
                j += 1

            # If there was no number found,
            if num == "":
                j += 1 # increment by one
                continue

            num = int(num) # Cast num to an integer

            # Now that we know the value, we need to check around it
            if is_symbol(i, start-1) or is_symbol(i, j):
                result += num
                continue

            for k in range(start-1, j+1):
                if is_symbol(i-1, k) or is_symbol(i+1, k):
                    result += num
                    break

    # Part two
    gear_ratios = []
    processed_indices = set()
    processed_values = set()

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            gear_ratio = is_gear(i, j, processed_indices, processed_values)
            print(f"Gear ratio at ({i}, {j}): {gear_ratio}")
            gear_ratios.append(gear_ratio)

    print("Total sum:", sum(gear_ratios))
