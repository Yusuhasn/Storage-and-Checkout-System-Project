"""Part III - Program (40 marks): """
 
inventory = [] 
searchCounter = [] 
cart = [] 
nameCounter = []

# Admin menu options, display these options in the menu
def Admin_Menu(): 
   while True:
     print("   Admin    ") 
     print("1> Add product") 
     print("2> Edit")
     print("3> Delete")
     print("4> Display Inventory") 
     print("5> Customer Menu") 
     print("6> EXIT ")

  #once the user selects an option through numbers, goes through different functions, such as to edit, insert, choose, display inventory 
     Admin_choose = input("Select option: ")  
     if Admin_choose == '1': 
      add_product() 
     elif Admin_choose == '2': 
      edit_product()
     elif Admin_choose == '3': 
      delete_product() 
     elif Admin_choose == '4': 
      Display_inventory() 
     elif Admin_choose == '5':
      Customer_menu() 
     elif Admin_choose == '6': 
      quit() 
   else: 
      print("Error") 
nameCounter = [] 
#The admin adds the product with a unique ID each time, with a counter for how much times the same product is typed in, so that when the customer adds quantity of that same product, the name counter is basically the quantity
def add_product(): 
	while True:
		product_ID = int(input("Enter ID: "))
		unique = True  
		for product in inventory: 
			if product[0] == product_ID: #the product is in the inventory, which originally inventory[0] is the ID number, 
				#so if the original ID = product ID, it is not unique and doesnt continue the code
				unique = False
				break
		if unique: 
			name = input("Enter Product Name: ")
			price = float(input("Enter price: "))
			newProduct = [product_ID, name, price] 
			inventory.append(newProduct)
			print("Product Added!")
			#this following code demonstrates a counter, where each time an product is repeatedly added into inventory, its counter adds up
			found = False 
			for product in nameCounter: 
				if product[0].lower() == name.lower(): #if product in all lowercases are the same, the code will add 1 to the counter each time its the same 
					product[1] += 1
					found = True
					break
			if not found: #checks if the product name was found throughout existing list 
				nameCounter.append([name, 1]) # appends a new list to the nameCounter list. where the product name was just added and with 1 because it is the start of the new items count, if i were to add the same product again, the number increases 
			break 
		else: 
			print("ID already exists")
			        
		
	
def edit_product(): 
	name = input("Enter Product to Edit: ")
	found = False 
	for product in inventory: 
		if product[1].lower() == name.lower(): #if the Admin inputs a name from the inventory, then the products price will change based on what the Admin changes it to
			product[2] = float(input("Enter New Price: ")) #changes price, product[2] because in the inventory, the 2nd index is the price
			found = True
	if found: 
		print("Price is Updated!") 
	else: 
		print("Product not found") 

def delete_product(): 
	product_ID = int(input("Enter product ID: "))
	for product in inventory: 
		if product[0] == product_ID: # if the Admin inputs an ID which = to the original ID from the inventory, the Admin will delete it and enter a new price
			inventory.remove(product) 
			print("Deleted successfully!")
			return 
	print("Product ID not found.")
			

def Display_inventory(): # the code displays the Inventory
	if len(inventory) == 0: # if the length of the Inventory is empty as in there are 0 things in the list, it displays the inventory is empty
		print("inventory empty") 
		return 
	print("     Inventory     ") 
	for product in inventory: 
		print("ID:", product[0])
		print("Name:", product[1])
		print("Price:", product[2]) 
		
		
def Customer_menu(): 
	while True: 
		print("Customer Menu")
		print("1>  Search item ")
		print("2>  Display Most Searched Item ")
		print("3>  Inventory ")
		print("4>  Add to Cart")
		print("5>  Checkout ")
		print("6>  Switch to Admin Menu")
		print("7>  Exit ")
		
		Customer_input = input("Enter option: ")
		if Customer_input == '1': 
			search_Item()  
		elif Customer_input == '2': 
			display_searched_item() 
		elif Customer_input == '3': 
			Display_inventory() 
		elif Customer_input == '4': 
			add_to_cart() 
		elif Customer_input == '5': 
			checkout_item() 
		elif Customer_input == '6': 
			Admin_Menu() 
		elif Customer_input == '7': 
			quit() 
		else: 
			print("Error")

	   

def search_Item(): # the customer searches for an Product
	name = input("Enter product: ")
	found = False 
	for product in inventory: 
		if product[1].lower() == name.lower(): #when the customer inputs a product from the inventory, it will display its price and id and name 
			print("ID:", product[0])
			print("Name:", product[1])
			print("price:", product[2])
			found = True 
	for item in searchCounter: #this code counts how many times the customer searched for an specific item
		if item[0].lower() == name.lower(): 
			item[1] += 1
			break 
	else: 
		searchCounter.append([name, 1]) # if a new product is searched that hasnt been searched, it counts that particular item to be searched once, starting its own counter
	if not found: 
		print("Product not found")
		
#to find the most searched product
def display_searched_item(): 
	if len(searchCounter) == 0: # if the searchCounter list is empty means that item hasnt been searched yet
		print("No searches yet!")
		return 
	Most_searched = searchCounter[0]  #searchCounter is a list full of different lists, with the name and its counter
	for item in searchCounter: 
		if item[1] > Most_searched[1]: #item is the lists inside of the searchCounter list, so item[1] is the second element of the inner list, which is the numbers (the counter)
			Most_searched = item 
	print("Most searched product: ", Most_searched[0], " ", Most_searched[1], "times")

def add_to_cart(): 
	product_ID = int(input("Enter Product ID: "))
	quantity = int(input("Enter quantity: "))
	for product in inventory: 
		if product[0] == product_ID: #once the customer searches for the products ID and is in inventory, it gets added into their cart (this loops goes through each product in the inventory list untill it finds the product, making sure it exists) 
			for item in cart: 
				if item[0] == product_ID: #if item[0] = product_ID, it means the product is already in the cart, incrementing the quantity of the item each time until it reaches the limit
					item[1] += quantity  
					break 
			else: 
				cart.append([product_ID, quantity]) #append the list product_ID and its quantity into the cart list
			print("Added to cart.")
			return 
		print("Product is not available ")
			
				
def checkout_item():   #the costumor checkouts the item
	if len(cart) == 0: # if the cart is empty, the list = 0 indexes. it doesnt print out anything
		print("Your cart is empty.")
		return 
	total = 0 
	for item in cart: 
		for product in inventory: 
			if product[0] == item[0]: # both product[0] and item[0] in cart are IDs, in product[0] is a product ID, and item[0] is a list that contains product_ID which is at index 0 and is the ID, and index 2 is the quantity
				total += product[2] * item[1] # total adds up = product[2] in inventory meaning the price from the inventory * the quantity from the item[1]. making the total price (without tax) but including quantity of the items in cart
	totalAndTax = total * 1.13 # the total amount * the tax (this is the finalized initial total amount)
	print("Total with tax: ", totalAndTax)
	payment = float(input("Enter Payment Amount: "))
	if payment >= totalAndTax: 
		change = payment - totalAndTax # if the customer payed more, they subtract the payment given from the customer to the initial total price.equaling to their change
		print("Transaction accepted! Your change is", change)
		cart.clear() # clears the cart after payed
	else: 
		print("Transaction not Accepted.")

  

def main(): 
	print("Welcome to the Store!") 
	Admin_Menu()

main()