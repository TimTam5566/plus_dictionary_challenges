import csv
# This defines a function called grocery_calculator.
# It takes in one argument: groceries, which is expected to be a dictionary.
# In that dictionary:
# Keys are item names (strings)
# Values are item prices (floats)

def grocery_calculator(groceries: dict):
    """A function to add up grocery bills.

    Arguments:
        - groceries: a dict which has the names of grocery bill items as its 
        keys, and the cost of the items as its values.

    Returns: a float representing the total cost of the grocery bill.

    Example input: {
        "Baby Spinach 100g bag": 2.78,
        "Hot Chocolate 300g": 3.70,
        "Crackers 250g packet": 2.10,
        "Coffee 500g": 9.00,
        "Carrots 1kg bag": 0.56,
        "Oranges 1kg bag": 3.08
    } 
    Example output: 21.22
    """ 
    total = sum(groceries.values()) # gets all the prices from the dictionary.
    return (total) # Rounds the result to 2 decimal places.


def word_counter(word_list: list):
#This line defines a function named word_counter.
# It takes in one argument: word_list, which is expected to be a list of strings (like ["apple", "banana", "apple"]).
    """A function to count the occurrences of each word in a word list.

    Arguments: 
        - word_list: a list of strings

    Returns: a dictionary containing the number of occurrences of each word in
    word_list.

    Example input: ["apple", "banana", "apple", "cherry", "apple", "banana"]

    Example output: {"apple": 3, "banana": 2, "cherry": 1}
    """
    word_count = {}
    # Initializes an empty dictionary called word_count.
    # This will store each unique word as a key and the number of times it appears as the value.
    for word in word_list:
    # This loop goes through each word in the word_list.
    # For each word, it checks if the word is already in the word_count dictionary.
        if word in word_count:
        # If the word is already in the dictionary, it increments its count by 1.
            word_count[word] += 1
            # This means the word has been seen before, so we add one to its count.
        else:
            word_count[word] = 1
            # If the word is not already in the dictionary, it adds the word with a count of 1
    return word_count
    # After the loop finishes going through all the words, it returns the completed dictionary.

def create_colour_dict(file_path: str):
    """A function that accesses an indicated csv file of colour values and 
    converts it into a dictionary.
    
    Arguments:
        - file_path: a string representing the location of a .csv file
        
    Returns: a dictionary whose keys are the plain English names of the colours
    described in the .csv file, and whose values are the hex codes of those 
    colours.
    
    Example input: "./data/colours_3_very_simple.csv"
    Example output: {"White": "#FFFFFF", "Black": "#000000", "Red": "#FF0000"}
    """
    colour_dict = {}  # Step 1: Create an empty dictionary to hold colour data

    with open(file_path, mode='r', newline='', encoding='cp1252') as file:  
        # Step 2: Open the CSV file safely using a context manager
        reader = csv.DictReader(file)  
        # Step 3: Use DictReader to read each row as a dictionary
        for row in reader:
            name = row['English']        # Step 4: Extract the plain English colour name
            hex_value = row['HEX']    # Step 5: Extract the hex code
            colour_dict[name] = hex_value  # Step 6: Store in the dictionary
    return colour_dict
   
    
        