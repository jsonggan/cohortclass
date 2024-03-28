from functools import reduce

def min(values):
    return reduce(lambda x, y: x if x < y else y, values)

def max(values):
    return reduce(lambda x, y: x if x > y else y, values)

# Sample test cases
if __name__ == "__main__":
    print(min([32, 63, 7, 10, 100]))  # Output: 7
    print(max([32, 63, 7, 10, 100]))  # Output: 100
