#Primitive data types
a = 10 #int value
y = "Hello world" #string value
b = 3.14 # float value
x = "c" # char value
isTrue = False #boolean value

#Complex data types
import array
int_array = array.array('faris',[1,2,3]) # array example
my_list = [1,2,3,4] #list example
my_tuple(1, "two", 3) #tuple example
my_dict = {"name":"Faris", "age":21} #dictionary example
my_set = {"IBU", "Faris", "Student"} #set example

# Task 2 -> add element to the list, remove element from list, update element, sort list, slice list

my_list.append(5) # adding into list element 5
my_list.remove(4) # removing element 4 from list
my_list[3] = 4 # updating element at index 3

new_list = my_list[1:] # slicing list

#Task 3
# Heterogeneous list with elements of different data types
heterogeneous_list = [1, "hello", 3.14, True]
for element in heterogeneous_list:
    print(f"Element: {element}, Type: {type(element)}")


#Task 4
from enum import Enum

class Days(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Function to print custom messages based on the input day
def print_day_message(day):
    if day == Days.MONDAY:
        print("Monday")
    elif day == Days.TUESDAY:
        print("Tuesday")
    elif day == Days.WEDNESDAY:
        print("Wednesday")
    elif day == Days.THURSDAY:
        print("Thursday")
    elif day == Days.FRIDAY:
        print("Friday")
    elif day == Days.SATURDAY:
        print("Saturday")
    elif day == Days.SUNDAY:
        print("Sunday")
    else:
        print("Invalid day!")

#Task 5
students = []


# Define a function to add a new student
def add_student(students, student_id, name, gpa):
    if student_id in students:
        print(f"Student ID {student_id} already exists. Try updating the GPA.")
    else:
        students[student_id] = (name, gpa)
        print(f"Student {name} added successfully.")


# Define a function to update the GPA of an existing student by ID
def update_gpa(students, student_id, new_gpa):
    if student_id in students:
        name, _ = students[student_id]
        students[student_id] = (name, new_gpa)
        print(f"GPA for student ID {student_id} updated successfully.")
    else:
        print(f"Student ID {student_id} not found.")

def display_students(students):
    if not students:
        print("No student records to display.")
    else:
        for student_id, (name, gpa) in students.items():
            print(f"ID: {student_id}, Name: {name}, GPA: {gpa:.2f}")


# Main program for task 5
def startTask5():
    students = {}  # Dictionary to store student records

    while True:
        print("\nMenu:")
        print("1. Add a new student")
        print("2. Update GPA of an existing student by ID")
        print("3. Display all student records")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            gpa = float(input("Enter student GPA: "))
            add_student(students, student_id, name, gpa)
        elif choice == '2':
            student_id = input("Enter student ID: ")
            new_gpa = float(input("Enter new GPA: "))
            update_gpa(students, student_id, new_gpa)
        elif choice == '3':
            display_students(students)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

#Task8
# Function to display the grades of all students
def display_grades(grades):
    print("Grades of all students:")
    for i, student_grades in enumerate(grades):
        print(f"Student {i + 1}: {student_grades}")

# Function to compute the average grade of each student
def compute_average(grades):
    for i, student_grades in enumerate(grades):
        average = sum(student_grades) / len(student_grades)
        print(f"Average grade of Student {i + 1}: {average:.2f}")

# Main program
def startTask8():
    # Define the 2D array for student grades
    grades = [
        [85, 90, 95],  # Student 1 grades
        [75, 80, 85],  # Student 2 grades
        [95, 100, 90]  # Student 3 grades
    ]

    # Display the grades and compute the average
    display_grades(grades)
    compute_average(grades)


#Task 9
def display_grades(grades):
    print("Grades of all students:")
    for i, student_grades in enumerate(grades):
        print(f"Student {i + 1}: {student_grades}")

def compute_student_averages(grades):
    student_averages = []
    for i, student_grades in enumerate(grades):
        average = sum(student_grades) / len(student_grades)
        student_averages.append(average)
        print(f"Average grade of Student {i + 1}: {average:.2f}")
    return student_averages

def compute_subject_averages(grades):
    num_subjects = len(grades[0])
    subject_averages = []
    for j in range(num_subjects):
        subject_total = sum(student_grades[j] for student_grades in grades)
        average = subject_total / len(grades)
        subject_averages.append(average)
        print(f"Average grade for Subject {j + 1}: {average:.2f}")
    return subject_averages


#Task 10
from math import pi

class ShapeType:
    CIRCLE = 1
    RECTANGLE = 2
    TRIANGLE = 3

class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type
        self.attributes = {}

    def set_circle(self, radius):
        self.attributes = {'radius': radius}

    def set_rectangle(self, length, width):
        self.attributes = {'length': length, 'width': width}

    def set_triangle(self, base, height):
        self.attributes = {'base': base, 'height': height}

    def calculate_area(self):
        if self.shape_type == ShapeType.CIRCLE:
            return pi * (self.attributes['radius'] ** 2)
        elif self.shape_type == ShapeType.RECTANGLE:
            return self.attributes['length'] * self.attributes['width']
        elif self.shape_type == ShapeType.TRIANGLE:
            return 0.5 * self.attributes['base'] * self.attributes['height']
        else:
            return None

    def display(self):
        if self.shape_type == ShapeType.CIRCLE:
            print(f"Shape: Circle\nRadius: {self.attributes['radius']}")
        elif self.shape_type == ShapeType.RECTANGLE:
            print(f"Shape: Rectangle\nLength: {self.attributes['length']}, Width: {self.attributes['width']}")
        elif self.shape_type == ShapeType.TRIANGLE:
            print(f"Shape: Triangle\nBase: {self.attributes['base']}, Height: {self.attributes['height']}")
        else:
            print("Unknown shape")
        print(f"Area: {self.calculate_area():.2f}")

def startTask10():
    print("Select a shape:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    choice = int(input("Enter your choice (1-3): "))

    if choice == ShapeType.CIRCLE:
        radius = float(input("Enter radius: "))
        shape = Shape(ShapeType.CIRCLE)
        shape.set_circle(radius)
    elif choice == ShapeType.RECTANGLE:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        shape = Shape(ShapeType.RECTANGLE)
        shape.set_rectangle(length, width)
    elif choice == ShapeType.TRIANGLE:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        shape = Shape(ShapeType.TRIANGLE)
        shape.set_triangle(base, height)
    else:
        print("Invalid choice!")
        return


