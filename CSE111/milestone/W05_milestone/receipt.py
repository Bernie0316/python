import csv
key_column_index = 0

def main():
    products_dict = read_dictionary("W05/products.csv", key_column_index)
    print("All Products")
    print(products_dict)
    request = open ("request.csv", "rt")
    request = csv.reader(request)
    next(request)
    print("\nRequested Items")
    for lines in request:
        product_number = lines[0]
        quantity = lines[1]
        if product_number in products_dict:
            item = products_dict[product_number]
            item_name = item[1]
            item_price = item[2]
            result = f"{item_name}: {quantity} @ {item_price}"
            print(result)

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
    with open(filename, mode="rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                dictionary[key] = row
        return dictionary
    
if __name__ == "__main__":
    main()    



