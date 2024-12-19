import csv
key_column_index = 0

def main():
    num_of_items = 0
    subtotal = 0
    try:
        products_dict = read_dictionary("products.csv", key_column_index)
    except:
        return print("Error: missing file\n[Errno 2] No such file or directory: 'products.csv'")     
    request = open_request()
    print("Inkom Emporium\n")
    for lines in request:
        product_number = lines[0]
        quantity = int(lines[1])
        try:
            item = products_dict[product_number]
        except:
            return print("Error: unknown product ID in the request.csv file\n'R002'")
        #if product_number in products_dict:
        #    item = products_dict[product_number]
        item_name = item[1]
        item_price = item[2]
        print(f"{item_name}: {quantity} @ {item_price}")
        num_of_items += quantity
        subtotal += (quantity * float(item_price))
        tax = subtotal * 0.06
        total = subtotal + tax
    print(f"\nNumber of Items: {num_of_items}")
    print(f"Subtotal: {subtotal:.2f}") 
    print(f"Sales Tax: {tax:.2f}")
    print(f"Total: {total:.2f}")
    print('\nThank you shopping at the Inkom Emporium.')
    current_date_and_time = time()
    print(f"{current_date_and_time:%c}")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                dictionary[key] = row
    return dictionary

def open_request():
    request = open("request.csv", "rt")
    request = csv.reader(request)
    next(request)
    return request

def time():
    from datetime import datetime
    current_date_and_time = datetime.now()
    return current_date_and_time 

if __name__ == "__main__":
    main()    