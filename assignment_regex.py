# This program reads through a text file, extract all of the digits 
# and calculates the sum


# sample data: There are 90 values with a sum=445833
# actual data: There are 100 values and the sum ends with 804


# The program is unnescessarily long, it has been done to practice my knowledge on functions and list

def number_extractor(data):                     # Define the function
    import re                   
    all_digits_str = list()                     # Define the lists
    all_digits = list()

    for line in data:                           # loop to extract all digits
        words = line.rstrip()
        x = re.findall('[0-9]+', words)
        all_digits_str += x
    for val in all_digits_str:                  # Convert the digits from strings to intergers
        val = int(val)
        all_digits.append(val)                  # Add digits to a list
    return all_digits
    


file_name = input('Enter file name: ')          # Get the name of the file

try: 
    file2 = open(file_name)
except FileNotFoundError:
    print('File could not be found. Please try again!')
    quit()

results = number_extractor(file2)
print('The sum of all', len(results), 'values in the sample data is:', sum(results))