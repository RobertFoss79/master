import csv
import os

def save_to_file(data, filename):
    """
    Save the budget data to a CSV file.

    Parameters:
    - data: dictionary containing budget data
    - filename: string path to the file where data will be saved
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['category', 'amount', 'date'])
        writer.writeheader()

        for key, value in data.items():
            if isinstance(value, dict):
                value['amount'] = f"{value['amount']:.2f}"  # Format amount to 2 decimal places
                writer.writerow({'category': key, 'amount': value['amount'], 'date': value['date']})
            else:
                value = f"{value:.2f}"  # Format amount to 2 decimal places for non-dict values
                writer.writerow({'category': key, 'amount': value, 'date': ''})

def load_from_file(filename):
    """
    Load budget data from a CSV file.

    Parameters:
    - filename: string path to the file from which data will be loaded

    Returns:
    - dictionary containing the loaded budget data
    """
    data = {}
    if not os.path.exists(filename):
        print(f"File not found: {filename}. A new file will be created.")
        return data

    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = row['category']
                amount = float(row['amount'])
                date = row['date']
                data[key] = {'amount': amount, 'date': date}
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
    return data
