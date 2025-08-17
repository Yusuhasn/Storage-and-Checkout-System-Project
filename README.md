Store Management System (Admin & Customer Menu)

This Python-based project demonstrates store management system that allows Admin and Customers to interact with an inventory of products. This is just a simple CLI based application that relates to some product management, searching/purchasing for customers, and basic tracking of sales.


**Features**
**Admin Functions**
Add new products with unique IDs

Edit existing product prices

Delete products from inventory

View full inventory

Count product additions

Switch to Customer Menu

**Customer Functions**
Search for products by name

Count most searched product

View inventory

Add items to shopping cart

Checkout with tax calculation (13%)

Switch to Admin Menu

**How it Works**
Inventory Format
Each product is a list:
[product_ID, product_name, price]
which is stored in the inventory list.

Cart Format
Each cart item is a list:
[product_ID, quantity]

Searching Tracking
Products that are searched by customer are counted with counters, where the most searched product can be shown at any time.

Counting Quantity
Admin product entries are counted with nameCounter, to avoid repeated entries of added products.  

**File Structure**

This is a single file application and does not require any external files or additional dependencies.

**How to Run**

Make sure Python 3.x is installed.

Save the code in a .py file, for example:
store_management.py

Then, open it in your terminal or IDE and run the file:

python3 store_management.py

**Sample Flow**

When it is first launched, the Admin Menu will be shown.

The Admin can Add/Edit/Delete products.

Then you can switch to the Customer Menu to:

Search for products

Add to a cart

Checkout and pay

Switch back to Admin if needed!

**Notes**

When you add new items, Product IDs will need to be unique.

Product names are case insensitive when searching or editing.

The checkout process has a fixed 13% tax.

The data is stored in-memory, so closing the program will reset the inventory and cart.

**Example Output**
Welcome to the Store!
    Admin    
1> Add product
2> Edit
3> Delete
4> Display Inventory
5> Customer Menu
6> EXIT
Select option: 1
Enter ID: 101
Enter Product Name: Apple
Enter price: 0.99
Product Added!

**License**

This is an open-source project and can be used for educational or personal use.
