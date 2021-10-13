import csv


# Function to read the csv files and put them in lists of dictionaries.
def read_data(path):
    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)
        header = next(reader)
        data = [dict(zip(header, map(str, row))) for row in reader]
        #print(data)
    return data


# Assign csv files to list of dictionaries
doctors = read_data('doctors.csv')
patients = read_data('patients.csv')
appointments = read_data('appointments.csv')


# Function to add patients
def add_patient(id, fname, lname):
    line = "{},{},{}".format(id, fname, lname)
    with open('patients.csv', 'a') as f:
        f.write("\n")  # Append a new line
        f.write(line)  # Append the new string
    _ = read_data('patients.csv')
    #print(new_patients)

# Function to set an appointment
def set_appointment(fname, lname, dr, date, time):
    line = "{},{},{}".format(id, fname, lname)
    with open('patients.csv', 'a') as f:
        f.write("\n")  # Append a new line
        f.write(line)  # Append the new string
    new_patients = read_data('patients.csv')


# Function to print the appointments to the console
def print_appointment(name):
    for appointment in appointments:
        if appointment['Patient'] == name:
            print(
                "{} has an appointment for Dr. {} in {} at {}."
                    .format(
                    appointment['Patient'],
                    appointment['Doctor'],
                    appointment['Date'],
                    appointment['Time']))
        else:
            print("Could not find an appointment for {}".format(name))
    return


# ---------------------------------------------------------------
# Considering final assignment make it a program and not a script.

# The assignment is to complete the while loop
# assignment:
# 1. add a function which won't let to set an appointment
#    for the same doctor on the same date.
# 2. ID must be presented as exactly 4 numbers.
# 3. The program can only accept .csv files and no other extension.
# 4. Cant register the same user twice. (trick here, can have same fname and lname, but not id.)
# 5. Prevent the user from clicking another button.
#    Valid inputs are only 1 2 3 4.
#    If the user clicks another option,
#    print "Please choose an option between 1-4."
# 6. Add a feature which supports lower case name conversion.
# need to think more.
# ---------------------------------------------------------------

if __name__ == '__main__':

    while True:
        # Main menu
        print("\nWelcome to Ariel medical appointments system\n" \
              "Please Choose one of the following:\n" \
              "1. Set an appointment\n" \
              "2. Observe an existing appointment\n" \
              "3. Register as a new user\n" \
              "4. Exit")
        x = input()
    #   -----------------------------------------------
    #   y does x == 1 won't work and '1' will work.
        #print("your input is {} and of type {}".format(x, type(x)))
        # Set an appointment menu
        if x == '1':
            pass
        # Observe an existing appointment menu
        elif x == '2':
            print("\nIn order to observe your appointment,\nPlease enter your Full name:")
            name = input()
            print_appointment(name)
        # Register as a new user menu
        elif x == '3':
            pass
        # Exit the program
        elif x == '4':
            print("\nThanks for using Ariel medical center app.\n Have a nice day!")
            break
        else:
            pass
        # What happens if the user click on something which is not 1-4?

