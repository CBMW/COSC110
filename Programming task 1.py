#COSC110 ASSIGNMENT 2 - PROGRAMMING TASK 1
#DEVELOPER: CODY WILLIAMS
#STUDENT NUMBER: 220250934

## Global variables
input_confirmed = False #Added this for error handling in num_patients() function

## Functions
def num_patients(): # Function to ask user how many patients require calculation
    global input_confirmed #Added global variable after debugging
    while not input_confirmed:
        try:#This try block takes input from user for number of patients with some error handling
            x_patients = int(input('Enter the number of patients: '))
            print("Number of patients entered = ", x_patients)
            if x_patients <= 0:#Error handling (must enter positive int)
                print("Please enter a positive integer for the number of patients.")
            else:
                input_confirmed = True#Global int to fix endless loop error
                return x_patients
        except ValueError:#Except block for error handling
            print("Invalid input. Please enter a positive number.")

def collect_dietary_requirements(num_patients): #Function to loop through patients and ask for dietary reqs
    total_protein = 0
    total_carbohydrates = 0 #Declaring variables outside of loop
    total_fat = 0

    for i in range(num_patients):#For each number of patients, replay this loop
        print(f"\nEntering data for patient {i + 1}:")#i+1 ensures we wont ask for data for the same patient twice
        while True:
            try: #Try block to handle Exceptions
                protein = float(input("Enter the amount of protein (in grams): "))#ask user for protein input in float type
                if protein >= 0:#If input greater than 0, continue, else ask for positive number
                    break
                else:
                    print("Please enter a non-negative number for protein.")
            except ValueError:
                print("Invalid input. Please enter a non-negative number.")

        while True: #Same loop now for carbs
            try:
                carbohydrates = float(input("Enter the amount of carbohydrates (in grams): "))
                if carbohydrates >= 0:
                    break
                else:
                    print("Please enter a non-negative number for carbohydrates.")
            except ValueError:
                print("Invalid input. Please enter a non-negative number.")

        while True: #Final loop for fat
            try:
                fat = float(input("Enter the amount of fat (in grams): "))
                if fat >= 0:
                    break
                else:
                    print("Please enter a non-negative number for fat.")
            except ValueError:
                print("Invalid input. Please enter a non-negative number.")

        total_protein += protein #Concatonate and calculate total protein,cabs and fat
        total_carbohydrates += carbohydrates
        total_fat += fat

    avg_protein = total_protein / num_patients #Divide totals by num_patients to find average
    avg_carbohydrates = total_carbohydrates / num_patients
    avg_fat = total_fat / num_patients

    avg_kilojoules = 4.18 * (4 * avg_protein + 4 * avg_carbohydrates + 9.30 * avg_fat) #calculate Kj using energy conversion factors

    print("\nAverage nutritional requirements per patient:") #Newline and f string type for cleaner terminal output
    print(f"Protein: {avg_protein:.2f} grams") #Displaying output of results
    print(f"Carbohydrates: {avg_carbohydrates:.2f} grams")
    print(f"Fat: {avg_fat:.2f} grams")
    print(f"Kilojoules: {avg_kilojoules:.2f} kJ")

def get_non_negative_float(prompt):#Prompt user for a positive float. This function was added for errorhandling
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a non-negative number.")
## End of functions

## Program start
num_patients = num_patients() #Turn function call into variable to add as argument
collect_dietary_requirements(num_patients)#Collect_dietary_requirements function called with the output of num_patients() as the input argument
## Program end
