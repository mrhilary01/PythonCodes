# Simple Calculator for Total, Average, and Grade

# Function to calculate the total
def calculate_total(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Function to calculate the average
def calculate_average(numbers):
    total = calculate_total(numbers)
    average = total / len(numbers)
    return average


# Function to determine the grade
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


# Main program
def main():
    print("Welcome to the Simple Calculator!")
    print("This program calculates the total, average, and grade of a list of numbers.")

    # Get input from the user
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]  # Convert input to a list of numbers

    # Perform calculations
    total = calculate_total(numbers)
    average = calculate_average(numbers)
    grade = calculate_grade(average)

    # Display results
    print("\nResults:")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


# Run the program
if __name__ == "__main__":
    main()