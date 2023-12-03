"""
Advent of Code Day One

The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that the
Elves now need to recover. On each line, the calibration value can be
found by combining the first digit and the last digit (in that order) 
to form a single two-digit number.

@author: Jordan Sinclair
"""

# Getting the artsy calibration data from data.txt
data = open("data.txt").read().splitlines()

########################## Part One ###################################

# Initial values
cal_val = 0

# Looping through each line 
for line in data:
    # Getting the digits from the line using list comprehension
    vals = [x for x in line if x.isdigit()]

    # Combining the values
    cal = int(vals[0] + vals[-1])

    # Adding to the final sum
    cal_val += cal


print(f"Part One Result: {cal_val}")


########################## Part Two ###################################

# Since we can now have values spelled out with letters, we need some
# kind of mapping, like a hash table, between the two. 

mapping = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

# Initial values
updated_val = 0

# Looping through each line 
for line in data:
    digits = []
    # Looping through each digit in the line
    for i in range(len(line)):
        # If the line is a digit, we can simply append as before
        if line[i].isdigit():
            digits.append(line[i])
        else:
            # Otherwise, we can loop through the hash table above
            for num in mapping:
                # and check if the line at the current index and onward matches
                if line[i:].startswith(num):
                    # If so, we append the mapped value
                    digits.append(str(mapping[num]))

    # Combining the values
    val = int(digits[0] + digits[-1])

    # Adding to the final sum
    updated_val += val


print(f"Part Two Result: {updated_val}")