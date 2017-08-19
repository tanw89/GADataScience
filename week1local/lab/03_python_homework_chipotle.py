'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv

with open('C:/Users/tanw/Desktop/LocalCopy-GACourse/GA_DAT5_Local/week1/chipotle-master/chipotle-master/orders.tsv') as f:
    file_nested_list = [row for row in csv.reader(f, delimiter="\t")]
print file_nested_list[0]
'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''
header = file_nested_list[0]
data = file_nested_list[1:]

'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''
num_orders = len(set([row[0] for row in data]))
print num_orders
 # count the number of unique order_id's
# note: you could assume this is 1834 since that's the maximum order_id, but it's best to check

prices = [float(row[4][1:-1]) for row in data]
print prices
# create a list of prices
# note: ignore the 'quantity' column because the 'item_price' takes quantity into account
# strip the dollar sign and trailing space
average_price = round(sum(prices) / num_orders, 2)
print average_price 
# calculate the average price of an order and round to 2 digits
# $18.81

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''

# if 'item_name' includes 'Canned', append 'choice_description' to 'sodas' list
sodas = []
for row in data:
    if 'Canned' in row[2]:
        sodas.append(row[3][1:-1])
print sodas

# equivalent list comprehension (using an 'if' condition)
sodas = [row[3][1:-1] for row in data if 'Canned' in row[2]]

# create a set of unique sodas
unique_sodas = set(sodas)
print unique_sodas

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

# keep a running total of burritos and toppings

burritos = 0
toppings = 0

# calculate number of toppings by counting the commas and adding 1
# note: x += 1 is equivalent to x = x + 1
for row in data:
    if 'Burrito' in row[2]:
        burritos += 1
        toppings += (row[3].count(',') + 1)

# calculate the average topping count and round to 2 digits
# 5.40
round(toppings/ float(burritos), 2)  

'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

# start with an empty dictionary
chips = {}

# if chip order is not in dictionary, then add a new key/value pair
# if chip order is already in dictionary, then update the value for that key
for row in data:
    if 'Chips' in row[2]:
        if row[2] not in chips:
            chips[row[2]] = int(row[1])     # this is a new key, so create key/value pair
        else:
            chips[row[2]] += int(row[1])    # this is an existing key, so add to the value

print chips

# defaultdict saves you the trouble of checking whether a key already exists

from collections import defaultdict
dchips = defaultdict(int)
for row in data:
    if 'Chips' in row[2]:
        dchips[row[2]] += int(row[1])

print dchips
'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
