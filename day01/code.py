def parse_input(path):
    """
    Parse input from a file, removing any empty lines.
    
    Args:
        path (str): Path to the input file.
    Returns:
        List[str]: A list of non-empty lines from the file.
    """
    with open(path, 'r') as file:
        return [line for line in file.read().splitlines() if line.strip()]


def part1(data):
    """
    Solve part 1 of the problem.
    Args:
        data (List[str]): The parsed input data.
    Returns:
        Any: The solution for part 1.
    """
    # Example: Replace with actual logic
    # Split right and left list
    # Pair up the smallest number in the left list with the smallest number in the right list,
    # how far apart the two numbers are; you'll need to add up all of those distances
    # 1) Write a for loop comparing the right_list and left_list
    # 2) Make a hashmap to remember the index of the of the smallest number
    # 3) Make an array of the distance

    left_list = []
    right_list = []

    distance = 0
    difference = 0

    # Split right and left list
    for each_line in data:
        # Input string would be data[0] = "28186   35627"
        input_str = each_line

        #  Split the input string by spaces
        left_str, right_str = input_str.split()


        # Convert string to integers
        left_integer = int(left_str)
        right_integer = int(right_str)

        # Append to left and right list
        left_list.append(left_integer)
        right_list.append(right_integer)
    
    # sort to smallest number
    left_list.sort()
    right_list.sort()
    
    #  write a for loop to compare left and right list
    for num in range(len(left_list)):
        if left_list[num] < right_list[num]:
            difference = right_list[num] - left_list[num]
            distance+=difference
        else:
            difference = left_list[num] - right_list[num]
            distance+=difference
    return distance


def part2(data):
    """
    Solve part 2 of the problem.
    Args:
        data (List[str]): The parsed input data.
    Returns:
        Any: The solution for part 2.
    """
    # Split into two columns:
    left_list = []
    right_list = []
    # Split right and left list
    for each_line in data:
        # Input string would be data[0] = "28186   35627"
        input_str = each_line

        #  Split the input string by spaces
        left_str, right_str = input_str.split()


        # Convert string to integers
        left_integer = int(left_str)
        right_integer = int(right_str)

        # Append to left and right list
        left_list.append(left_integer)
        right_list.append(right_integer)

    # Create a hashmap
        hash_map = {}
        total = 0
        product = 0
        
        # nested for loop to check for left_list against right_list
        for left in range(len(left_list)):
            for right in range(len(left_list)):
                #  if left_list value is equals to right_right list
                if  left_list[left] == right_list[right]:
                    # check to see if it's in the hashmap then increment to 1
                    if left_list[left] in hash_map:
                    # Add the number of times it has been checked
                        hash_map[left_list[left]] += 1
                    else:
                        #  if not in the hash map to set it as key with value of 1
                        hash_map[left_list[left]] = 1 


        # iterate through the hash map and multiply
        for pair in hash_map:
            product = pair*hash_map[pair]
            total +=product

    return total


def main():
    input_path = 'day01/input.txt'
    data = parse_input(input_path)

    # Solve the puzzle
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == '__main__':
    main()