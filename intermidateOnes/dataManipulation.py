#importing csv because we are working with csv files
import csv



def calculate_total_sales(csv_file_path):

    #Initial sales are 0
    total_sales = 0.0

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            quantity = int(row['Quantity'])
            price = float(row['Price'])
            total_sales += quantity * price
    return total_sales

# Specify the path to your CSV file and r is used in address to read.
csv_file_path = r'D:\python\masteringPython\intermidateOnes\sample.csv'

# Calculate the total sales
total_sales = calculate_total_sales(csv_file_path)

print(f"Total Sales: ${total_sales:.2f}")
