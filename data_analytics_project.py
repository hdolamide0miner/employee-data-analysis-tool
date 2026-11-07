import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)   # show all columns, no truncation
pd.set_option('display.width', None)         # don't wrap/truncate based on terminal width

# =============================================
# LOAD DATA
# =============================================
# Read the CSV file into a DataFrame called df
df = pd.read_csv(r"C:\\Users\\ajibo\\.vscode\\propervs\\practice_data.csv")


# =============================================
# HELPER FUNCTION (used by option 2.4 and option 4)
# =============================================
def get_number(prompt):
    """Keep asking until the user types a valid number, then return it."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter numbers only.")


# =============================================
# DISPLAY MENU OPTIONS
# =============================================
print("Welcome to the data analysis program")
print("You have the following options to choose from:")
print("1 = Searching for specific data in a category")
print("2 = Calculations in specific categories")
print("3 = Showing the whole table in the CSV")
print("4 = advanced filtering options")
print("5 = Exit")


# =============================================
# GET VALID MENU OPTION FROM USER (must be a number)
# =============================================
while True:
    option = input("Input your option: ")

    try:
        option = int(option)  # Try converting input to an integer
        break                 # If successful, exit the loop
    except ValueError:
        print("The value has to be a number. e.g (1)")  # Runs if input isn't a number

# Keep asking until the option is within the valid range (1-5)
while option <= 0 or option >= 6:
    print("The option must be between 1 and 5")
    option = int(input("Input your option: "))


# =============================================
# OPTION 1: SEARCH FOR DATA BY CATEGORY
# =============================================
if option == 1:
    # Show the user all available columns to search by
    chosen = ['name', 'department', 'manager', 'employee_id', 'location', 'full-time']
    print(chosen)
    print("Choose from this table which category you want to search.")
    column = input("")

    # Keep asking until the user enters a valid column name
    while column not in chosen:
        print("It is not available. Below are the available columns:")
        print(chosen)
        column = input("")

    found = column  # Store the matched column name
    print(f"column = {found}")


    # --- Search by Employee ID ---
    def get_employee_id():
        """Keep asking until a valid whole number is entered."""
        while True:
            id_find = input("What ID are you looking for: ")
            try:
                id_find = int(id_find)
                return id_find
            except ValueError:
                print("You cannot use decimals or words")


    def search_employee_id():
        """Search for an employee by ID, with an option to try again."""
        while True:
            id_find = get_employee_id()

            # Check every row before deciding it's not found
            found_match = False
            for x in df["employee_id"]:
                if id_find == x:
                    found_match = True
                    break

            if found_match:
                print(f"{id_find} was found")
                print(df.loc[df["employee_id"] == id_find])
            else:
                print(f"The id {id_find} you were looking for doesn't exist")

            # Ask y/n, validated on its own loop
            while True:
                repeat = input("Do you want to try again? (y/n): ").lower()
                if repeat in ("y", "n"):
                    break
                print("The only options allowed are y or n")

            if repeat == "n":
                print("bye")
                break
            # if "y", the outer while loop just runs again

    # Usage:
    if found == 'employee_id':
        search_employee_id()


    # --- Search by Name ---
    def get_name():
        while True:
            name_to_find = input("Write the name you want to find: ")

            # Check whether the name exists
            while name_to_find not in df["name"].values:
                print("Name not found")

                # Validate the retry response
                while True:
                    retry = input("Do you want to try again? (y/n): ").lower()

                    if retry in ("y", "n"):
                        break

                    print("The only options allowed are y or n")

                if retry == "n":
                    print("Bye")
                    return

                # If retry == "y", ask for a name again
                name_to_find = input("Write the name you want to find: ")

            # Display matching rows
            print(df.loc[df["name"] == name_to_find])
            return

    # Usage:
    if found == 'name':
        get_name()


    # --- Search by Location ---
    def get_location():
        location_to_find = input("Write the location you want to find: ")

        # Only these locations exist in the dataset
        list3 = ['New York', 'Los Angeles', 'Chicago', 'Remote']

        # Keep asking until a valid location is entered
        while location_to_find not in list3:
            print("The location doesn't exist")
            location_to_find = input("Write the location you are looking for: ")
        return location_to_find


    def location_search():
        while True:
            location_to_find = get_location()

            # Print all employees in that location
            print(df.loc[df['location'] == location_to_find])

            while True:
                recall = input("Do you want to search for another location? (y/n): ").lower()

                if recall in ['y', 'n']:
                    break

                print("The only options allowed are y or n")

            if recall == "n":
                print("bye")
                break

    # Usage:
    if found == 'location':
        location_search()


    # --- Search by Manager ---
    def get_manager():
        manager_to_find = input("Write the manager you want to find: ")

        # Only these managers exist in the dataset
        list5 = ['Sarah Lee', 'James Carter', 'Linda Green']

        # Keep asking until a valid manager name is entered
        while manager_to_find not in list5:
            print("The manager doesn't exist")
            manager_to_find = input("Write the manager you are looking for: ")
        return manager_to_find


    def manager_search():
        while True:
            manager_to_find = get_manager()

            # Print all employees under that manager
            print(df.loc[df['manager'] == manager_to_find])

            while True:
                recall1 = input("Do you want to search for another manager? (y/n): ").lower()

                if recall1 in ['y', 'n']:
                    break
                print("The only options allowed are y or n")

            if recall1 == 'n':
                print("bye")
                break

    # Usage:
    if found == 'manager':
        manager_search()


    # --- Search by Department ---
    def get_department_input():
        """Keep asking until a valid department is entered."""
        # Only these departments exist in the dataset
        list2 = ['Engineering', 'Marketing', 'HR', 'Finance']
        dp_find = input("Write the department you are looking for: ")

        while dp_find not in list2:
            print("The department doesn't exist")
            dp_find = input("Write the department you are looking for: ")

        return dp_find


    def search_department():
        """Search for employees by department, with an option to try again."""
        while True:
            dp_find = get_department_input()
            print(df.loc[df['department'] == dp_find])

            while True:
                recall2 = input("Do you want to search for another department? (y/n): ").lower()
                if recall2 in ['y', 'n']:
                    break
                print("The only options allowed are y or n")

            if recall2 == 'n':
                print("bye")
                break

    # Usage:
    if found == 'department':
        search_department()


# =============================================
# OPTION 2: CALCULATIONS ON SALARY OR PERFORMANCE SCORE
# =============================================
if option == 2:
    print("You can only calculate two options here: salary and performance_score.")
    print("2.1 = Calculating mean of category")
    print("2.2 = Getting the max number in the category")
    print("2.3 = Getting the min number in the category")
    print("2.4 = getting the range of two different salaries")

    # Ask which column to calculate (must be salary or performance_score)
    col_choice = input("Which column do you want to calculate (salary / performance_score): ")
    calculation_list = ['salary', 'performance_score']

    # Keep asking until a valid column is chosen
    while col_choice not in calculation_list:
        print("You can only calculate salary or performance_score.")
        col_choice = input("Which column do you want to calculate: ")

    # Ask which calculation to perform
    calc = input("What calculation do you pick (2.1 / 2.2 / 2.3 /2.4): ")
    try:
        calc = float(calc)  # Convert to float for comparison
    except ValueError:
        print("Invalid input. Please enter a number like 2.1, 2.2, or 2.3.")
        exit()  # Exit the program if the input is invalid

    # --- Calculate Mean ---
    if calc == 2.1:
        number = df[col_choice].mean()   # Get the average value
        number = round(number, 2)        # Round to 2 decimal places
        print(f"The mean is {number}")

    # --- Calculate Maximum ---
    if calc == 2.2:
        number1 = df[col_choice].max()   # Get the highest value
        number1 = round(number1, 2)
        print(f"The max is {number1}")

    # --- Calculate Minimum ---
    if calc == 2.3:
        number2 = df[col_choice].min()   # Get the lowest value
        number2 = round(number2, 2)
        print(f"The min is {number2}")

    # --- Range between two values ---
    if calc == 2.4:
        while True:
            low = get_number(f"Minimum {col_choice}: ")
            high = get_number(f"Maximum {col_choice}: ")

            if low > high:
                print("Minimum can't be higher than maximum. Try again.")
            elif col_choice == "performance_score" and (low < 0 or high > 10):
                print("Performance score must be between 0 and 10. Try again.")
            else:
                break  # valid input, leave the loop

        in_range = df[df[col_choice].between(low, high)]

        if in_range.empty:
            print(f"No employees have a {col_choice} between {low} and {high}.")
        else:
            print(f"Employees with a {col_choice} between {low} and {high}:")
            print(in_range)
            print(f"({len(in_range)} employees found)")


# =============================================
# OPTION 3: SHOW THE ENTIRE CSV TABLE
# =============================================
if option == 3:
    # to_string() removes pandas' default row/column limits so everything is visible
    print(df.to_string())


# =============================================
# OPTION 4: ADVANCED FILTERING OPTIONS
# =============================================
if option == 4:
    print("welcome to advanced options filtering where you can combine up to 5 of the filtering options in the table")

    advanced = ["name", "location", "department", "salary", "performance_rating", "manager", "full_time", "hire_date"]

    # Safety check: drop any name that isn't a real column in the CSV
    advanced = [c for c in advanced if c in df.columns]

    print("our options are :")
    print(advanced)
    print("you will be asked to write the category of the table you want to filter, it will continue to asked until you have used all 5 required spaces or if you enter (none)")

    chosen = []   # the categories the user picks, e.g. ['department', 'salary']

    # --- STEP 1: choose the categories ---
    def get_category():
        while True:
            pick = input("what category do you want to filter:").lower()

            if pick == "none":
                return pick
            elif pick not in advanced:
                print(f"please choose one of: {', '.join(advanced)}")
            elif pick in chosen:
                print("its already there")
            else:
                return pick  # valid and new

    while len(chosen) < 5:
        choices = get_category()

        if choices == "none":
            break
        else:
            chosen.append(choices)

    print(chosen)

    # --- STEP 2: filter by each chosen category, one after another ---
    if len(chosen) == 0:
        print("No categories chosen.")
    else:
        result = df   # start with the full table

        for col in chosen:

            # Number columns (like salary): ask for a minimum and maximum
            if df[col].dtype in ["int64", "float64"]:
                while True:
                    low = get_number(f"Minimum {col}: ")
                    high = get_number(f"Maximum {col}: ")

                    if low > high:
                        print("Minimum can't be higher than maximum. Try again.")
                    elif col.startswith("performance") and (low < 0 or high > 10):
                        print("Performance score must be between 0 and 10. Try again.")
                    else:
                        break

                # keep only the rows between low and high
                result = result[result[col].between(low, high)]

            # Text columns (like department): ask for one value
            else:
                value = input(f"Enter the {col} you want: ").strip().lower()

                # keep only the rows that match (capitals ignored)
                result = result[result[col].astype(str).str.lower() == value]

        # --- STEP 3: show the final table ---
        if result.empty:
            print("No employees match all of those filters.")
        else:
            print("Employees matching all of your filters:")
            print(result)
            print(f"({len(result)} employees found)")