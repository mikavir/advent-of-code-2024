def parse_input(path):
    """
    Parse input from a file, removing any empty lines.
    
    Args:
        path (str): Path to the input file.
    Returns:
        List[str]: A list of non-empty lines from the file.
    """
    # https://github.com/breddy-one99/advent-of-code/blob/main/day2/part1.py
    with open(path, 'r') as file:
        return [list(map(int, line.split())) for line in file if line.strip()]



def is_increasing(a):
    """
    https://www.geeksforgeeks.org/python-check-if-list-is-sorted-or-not/
    Return boolean: True if it is increasing and more than the other one
    """
    return all(a[i] < a[i + 1] for i in range(len(a) - 1))

def is_decreasing(b):
    """
    https://www.geeksforgeeks.org/python-check-if-list-is-sorted-or-not/
    Return boolean: True if it is decreasing and more than the other one
    """
    return all(b[i] > b[i + 1] for i in range(len(b) - 1))




    
def part1(data):
    """
    return: Quantity of number of safe reports
    considered as 'safe' if : 
        - the levels are either all increasing or all decreasing.
        - Any two adjacent levels differ by at least one and at most three.
    each line type = list
        - item in sublist is a string
    """
    safe_reports = 0

    i = 0

    for report in data:
        if is_increasing(report) or is_decreasing(report):
            safe_num = 0
            if all(abs(report[i+1] - report[i]) in [1,2,3] for i in range(len(report) - 1)) :
                    safe_reports +=1
                    safe_num +=1
            
    
    return safe_reports





def part2(data):
    """
    return: Quantity of number of safe reports
    considered as 'safe' if :
        - one bad level
        - the levels are either all increasing or all decreasing.
        - Any two adjacent levels differ by at least one and at most three.
    each line type = list
        - item in sublist is a string
    
    """
    safe_reports = 0
    i = 0
    n = 0

    for report in data:
        # Iterate through each index to create a temporary report
        for n in range(len(report)):
            # Create a new list excluding the element at index `n`
            temp_report = report[:n] + report[n+1:]

            # Check if the temp_report is safe
            if is_increasing(temp_report) or is_decreasing(temp_report):
                if all(abs(temp_report[j+1] - temp_report[j]) in [1, 2, 3] for j in range(len(temp_report) - 1)):
                    safe_reports += 1
                    break  # Stop further checks for this report

    return safe_reports 


def main():
    input_path = 'day02/input.txt'
    data = parse_input(input_path)

    # Solve the puzzle
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == '__main__':
    main()