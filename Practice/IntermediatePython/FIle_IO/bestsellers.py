import csv

# Read csv
with open('Bestseller-Sheet.csv', 'r') as file:
    header = csv.reader(file)
    
    for row in header:
        print(row)


# Try to add a row
try:
    file = open('Bestseller-Sheet.csv', 'w')
    writer = csv.writer(file)

    writer.writerow(['Make a million in month', 'Prismana', 'English', '2025', '20','Financial'])
finally:
    file.close()