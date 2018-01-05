file_path = "C:\Temp\example.txt"

# open file in read mode and assign handler to file variable
file = open(file_path, 'r')

#  read file contents
contents = file.read()
print(contents)

#  move file pointer back to position 0
file.seek(0)

#  read file lines
lines = file.readlines()
#  right strip \n from each line
lines = ([l.rstrip('\n') for l in lines])

print(lines)

#  always remember to close the file
file.close()


# write over a file

file_path_2 = r"C:\Users\rjakowenko\Documents\700_PYTHON\PyCode\Udemy Python Mega Course\example_2.txt"

file = open(file_path_2, 'w')

for _ in range(5):
    file.write('Line ' + str(_ + 1) + '\n')

file.close()

# append to a file

file_path_2 = r"C:\Users\rjakowenko\Documents\700_PYTHON\PyCode\Udemy Python Mega Course\example_2.txt"

file = open(file_path_2, 'a')

for _ in range(6,10):
    file.write('Line ' + str(_ + 1) + '\n')


# with statement

with open(file_path_2,'a+') as file:
    file.seek(0)
    contents = file.read()
    file.write('\n the last line')

# note there is no need to close the file


#  exercise: merge files

folderpath = r'C:\Users\rjakowenko\Documents\700_PYTHON\PyCode\Udemy Python Mega Course\files'

import os
import datetime

contents = ''
for f in os.listdir(folderpath):
    filepath = folderpath + '\\' + f
    print('file path for file '+f+'is '+filepath)

    with open(filepath, 'r') as file:
        contents = contents + file.read() + '\n'
    print('contents after reading ' + f + ' file are \n' + contents)

outputfile = folderpath + '\output_'+(datetime.datetime.now()).strftime('%Y-%m-%d_%H-%M-%S')+'.txt'
output = open(outputfile, 'w')
output.write(contents)
output.close()

with open(outputfile, 'r') as output:
    result = output.read()

print('file '+outputfile+' contains following :\n')
print(result)
