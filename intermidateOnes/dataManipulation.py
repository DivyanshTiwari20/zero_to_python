import csv
import os

def calculate_total_sales(csv_file_path):
    if not os.path.isfile(csv_file_path):
        print(f"File not found: {csv_file_path}")
        return 0.0
    
    total_sales = 0.0
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                quantity = int(row['Quantity'])
                price = float(row['Price'])
                row_sales = quantity * price
                total_sales += row_sales
                print(f"Processed row: {row}, Row Sales: ${row_sales:.2f}")
            except ValueError as e:
                print(f"Error processing row: {row}. Error: {e}")
    return total_sales

# Specify the path to your CSV file
csv_file_path = r'D:\python\masteringPython\intermidateOnes\sample.csv'

# Calculate the total sales
total_sales = calculate_total_sales(csv_file_path)

print(f"Total Sales: ${total_sales:.2f}")
