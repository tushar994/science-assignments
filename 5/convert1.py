import csv
import re
import sys

employee_file = open('info.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# employee_writer.writerow(['John Smith', 'Accounting', 'November'])
# employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

with open(sys.argv[1], "r") as f:
    reader = csv.reader(f, delimiter="\n")
    array = []
    employee_writer.writerow(["ox","oy","oz","h1x","h1y","h1z","h2x","h2y","h2z"])
    for i, line in enumerate(reader):
        splitted = re.split(" ",line[0])
        while('' in splitted):
            splitted.remove('')
        print(splitted)
        if(len(splitted)>9 and (splitted[2]=='OH2' or splitted[2]=='H2' or splitted[2]=='H1')):
            array.append(splitted[5])
            array.append(splitted[6])
            array.append(splitted[7])
            if(splitted[2]=='H2'):
                print(array)
                employee_writer.writerow(array)
                array = []