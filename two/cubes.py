"""
Advent of Code Day Two

As you walk, the Elf shows you a small bag and some cubes 
which are either red, green, or blue. Each time you play 
this game, he will hide a secret number of cubes of each 
color in the bag, and your goal is to figure out 
information about the number of cubes.

Determine which games would have been possible if the bag
had been loaded with only 12 red cubes, 13 green cubes, and 
14 blue cubes. What is the sum of the IDs of those games?

@author: Jordan Sinclair
"""

# This function recieves a list of tables of cube colors where the entries
# are the number of times each color was pulled from a bag. It checks to 
# see if those values are within a given threshold for each entry in the 
# list. If any of them are outside the given threshold, this function returns
# false. 
def checkCubes(colorsList):
    for colors in colorsList:
        if colors["red"] > 12 or colors["green"] > 13 or colors["blue"] > 14:
            return False
    return True

# calcPower takes a list of dictionaries, like above, and calculates essentially
# the maximum value of red, green, and blue cubes across all list entries. 
def calcPower(colorsList):
    mr = 0
    mg = 0
    mb = 0

    for colors in colorsList:
        if colors["red"] > mr:
            mr = colors["red"]
        if colors["green"] > mg:
            mg = colors["green"]
        if colors["blue"] > mb:
            mb = colors["blue"]
    
    power = mr*mg*mb
    return power
        
# Populates the cubes table by finding each of the keywords, 
# and getting the necessary values from the string. 
def getValues(draw):
    cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for cube in cubes:
        for i in range(len(draw)):
            if draw[i:].startswith(cube):
                # Now we need to get the value
                x = i - 1
                digitLength = 0
                while draw[x-1].isdigit():
                    digitLength += 1
                    x -= 1
                cubes[cube] = int(draw[x:x+digitLength])
    
    return cubes


if __name__=="__main__":
    # Loading in each line of data into a list
    data = open("data.txt").read().splitlines()

    # Initial values:
    ids = 0
    totalPower = 0

    # Looping through all of the lines
    for game in range(len(data)):
        # Since each game contains an unknown subset of demonstrations,
        # we need to loop through the strings after splitting on ;
        g = data[game].split(":")[1] # Removes Game n:
        run = g.split(";")

        results = []

        for draw in run:
            results.append(getValues(draw))
        
        ## Now that we have a list of cube color values, we can check each one
        ## for the conditions given
        if checkCubes(results):
            ids += game + 1
        
        totalPower += calcPower(results)

    print(f"The sum of valid game ids is: {ids}")
    print(f"The total power is: {totalPower}")