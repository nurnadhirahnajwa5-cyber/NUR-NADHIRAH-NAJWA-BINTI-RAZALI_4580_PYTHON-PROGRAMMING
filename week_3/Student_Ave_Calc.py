choice = "y"

# Repeat the program while user enters 'y'
while choice == "y":

    # Input three quiz marks
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    # Calculate and display the average
    average = (quiz_1 + quiz_2 + quiz_3) / 3
    print("Average =", average)

    # Determine pass or fail
    if average >= 50:
        print("Pass")
    else:
        print("Fail")

    # Ask whether to continue
    choice = input("Continue? Select Y/N: ").lower()

print("Program Ended")
