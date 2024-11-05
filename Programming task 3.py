# COSC110 ASSIGNMENT 2 - PROGRAMMING TASK 2
# AUTHOR: CODY WILLIAMS
# STUDENT ID: 220250934

'''Import necessary modules for the GUI application'''
from tkinter import *  # Import tkinter module
from tkinter import ttk  # Import ttk module

'''Dictionary to store dietary information'''
diets = {
    "Normal": {"Protein": 32.50, "Carbohydrates": 60.00, "Fat": 40.86, "description": "Normal diet"},
    "Oncology": {"Protein": 35.00, "Carbohydrates": 52.50, "Fat": 37.63, "description": "Oncology diet"},
    "Cardiology": {"Protein": 32.50, "Carbohydrates": 30.00, "Fat": 26.88, "description": "Cardiology diet"},
    "Diabetes": {"Protein": 20.00, "Carbohydrates": 27.50, "Fat": 27.95, "description": "Diabetes diet"},
    "Kidney": {"Protein": 15.00, "Carbohydrates": 55.00, "Fat": 23.65, "description": "Kidney diet"}
}

'''Function to display diet information based on the selected diet'''
def display_diet_info(diet_name):
    diet = diets[diet_name]  # Get selected diet's data from the diets dictionary
    info = f"Diet: {diet_name}\n" # Display diet name
    info += f"Protein: {diet['Protein']:.2f}g\n" # Display protein amount
    info += f"Carbohydrates: {diet['Carbohydrates']:.2f}g\n" #Display carbohydrates amount
    info += f"Fat: {diet['Fat']:.2f}g\n" # Display fat amount
    diet_info_display.config(text=info)  # Update the label with formatted diet info when clicked

'''GUI CONFIGURATION'''
root = Tk()  # Create the root window
root.title("Meal Nutrition")  # Set window title
root.configure(background="lightgrey")  # Set background color
root.minsize(450, 300)  # Set min size of the window
root.maxsize(600,700)  # Set max size of the window
root.geometry("500x400")  # Set default size of the window
frame = ttk.Frame(root, padding="10 10 20 20") # Create a main frame with padding inside the root window
frame.grid(column=0, row=0, sticky=(N, W, E, S))  # Set grid position and stretch options
root.columnconfigure(0, weight=1) # Configure root window grid weights for resizing behavior
root.rowconfigure(0, weight=1)

'''Allow resizing'''
frame.columnconfigure(0, weight=1)  # Column for buttons resizes equally
frame.columnconfigure(1, weight=3)  # Column for diet info resizes more
frame.rowconfigure(1, weight=1)  # Row configuration for resizing behavior

'''Create buttons for each diet, placed in the first column of the grid'''
for i, (diet_name, diet_info) in enumerate(diets.items()):
    button = ttk.Button(frame, text=diet_name, command=lambda dn=diet_name: display_diet_info(dn))
    button.grid(column=0, row=i+1, padx=10, pady=5, sticky="nsew")  # Position buttons in grid
    button.config(width=15)  # Set button width

'''Create a label for displaying diet information in the second column'''
diet_info_display = ttk.Label(
    frame,
    text="Select a diet...",  # Default text for the label
    font=("Arial", 14),  # Set fixed larger font size
    background="white",  # Background color for the label
    relief="solid",  # Border style for the label
    padding="10"  # Padding inside the label
)
'''Set the location for our diet information label'''
diet_info_display.grid(
    column=1, 
    row=1, 
    rowspan=len(diets), 
    padx=20, pady=5, 
    sticky=(N, S, E, W)
)

for i in range(1, len(diets) + 1): # Allow rows to resize proportionally to make the layout flexible
    frame.rowconfigure(i, weight=1)  # Make buttons and label scale with window size

root.mainloop() # Start the main loop
