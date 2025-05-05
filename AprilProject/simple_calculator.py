def calculate_total(numbers):
    return sum(numbers)

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

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

def main():
    print("Simple Calculator for Total, Average, and Grade")
    input_str = input("Enter numbers separated by spaces: ")
    try:
        numbers = list(map(float, input_str.split()))
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")
        return

    total = calculate_total(numbers)
    average = calculate_average(numbers)
    grade = calculate_grade(average)

    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
