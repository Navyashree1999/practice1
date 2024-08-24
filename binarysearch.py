# Search for a Number in a Sorted Array:

def binary_search(arr,target):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = len(arr)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high-=1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")


def binary_search_word(word_list, target):
    low = 0
    high = len(word_list)-1

    while low<=high:
        mid = len(word_list)//2
        if word_list[mid] == target:
            return mid
        elif word_list[mid] < target:
            low = mid+1
        else:
            high = mid-1

word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
target = 'grape'
result = binary_search_word(word_list, target)
if result != -1:
    print(f"Word '{target}' found at index {result}.")
else:
    print(f"Word '{target}' not found.")

class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

def binary_search_student(student_list, target_roll_no):
    low = 0
    high = len(student_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if student_list[mid].roll_no == target_roll_no:
            return mid
        elif student_list[mid].roll_no < target_roll_no:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # If the target is not found

# Example usage:
students = [Student(101, 'Alice'), Student(202, 'Bob'), Student(303, 'Charlie'), Student(404, 'David')]
target_roll_no = 202
result = binary_search_student(students, target_roll_no)
if result != -1:
    print(f"Student with roll number {target_roll_no} found. Name: {students[result].name}.")
else:
    print(f"Student with roll number {target_roll_no} not found.")