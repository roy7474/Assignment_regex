# This program reads through a text file, extract all of the digits 
# and calculates the sum


# sample data: There are 90 values with a sum=445833
# actual data: There are 100 values and the sum ends with 804


#fhandle = open('sample_data.txt')

def number_extractor(data):
    import re                   
    all_digits_str = list()
    all_digits = list()
    #open(data)
    for line in data:
        words = line.rstrip()
        x = re.findall('[0-9]+', words)
        all_digits_str += x
    for val in all_digits_str:
        val = int(val)
        all_digits.append(val)
    return all_digits
    
# print('The sum of all', len(all_digits), 'values in the sample data is:', sum(all_digits))
results = number_extractor(open('sample_data.txt'))


print('The sum of all', len(results), 'values in the sample data is:', sum(results))
'''
#ope file directly for esier testing of the program
fhandle = open('sample_data.txt')
for line in fhandle:
    words = line.rstrip()
    x = re.findall('[0-9]+', words)
    all_digits_str += x
for val in all_digits_str:
    val = int(val)
    all_digits.append(val)
    
print('The sum of all', len(all_digits), 'values in the sample data is:', sum(all_digits))'''