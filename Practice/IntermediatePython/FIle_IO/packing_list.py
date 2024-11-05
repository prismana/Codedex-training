import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

# Try to make csv file from data above
try:
    file = open('packing_list.csv', 'r', newline='')
    writer = csv.reader(file)

    for row in writer:
        print(row)

except FileNotFoundError:
    print("Packing list file not found, Creating a new one")

    with open('packing_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    
finally:
    file.close()