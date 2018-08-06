def find_reverse(numbers):
    print(numbers[::-1])
    return numbers[::-1]

def find_max(numbers):
    print(max(numbers))
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def find_sum(numbers):
    return sum(numbers)

def find_average(numbers):
    list_average = find_sum(numbers)/ len(numbers)
    return list_average

def find_descending(numbers):
    return sorted(numbers, key=int, reverse=True)

def second_smallest(numbers):
    second_smallest = sorted(numbers, key=int, reverse=False)
    return second_smallest[1]
'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k'
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
    second_smallest = sorted(numbers, key=int, reverse=False)
    return second_smallest[k]
