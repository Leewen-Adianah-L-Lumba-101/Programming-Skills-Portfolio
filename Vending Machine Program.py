# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3   # This library accesses the SQL Browser program
                 
import time as t # This import will be used purely for aesthetic purposes.
                 # 'time' library will access timing-based functions that delay code by seconds.
                 # This the Vending Machine Program feel more authentic by imitating--
                 # delays, like how machines make you wait before they give you an output.

con = sqlite3.connect("Vending Machine.db") # This is the database where all the products are stored

# Initializing Variables 1
final = False       # An indicator that will help decide if the program ends or not
cart = []           # A shopping cart used to store the name(s) of the product(s) the User picks
cart2 = 0           # A counter, calculating the total of all products from 'cart'
cart3 = []          # A cart for storing all the codes of the products from 'cart'
cart4 = []          # A cart for storing the prices of all products from 'cart'
discount = False    # An indicator if the 30% discount should be added at checkout/payment

# Initializing Variables 2
# These lists are for checking if product code entered is in the bundles (refer to documentation)
bundles = ["A1", "A2", "A3", "A4", "A5", "A6", "B4", "C1", "C2", "C4", "C5", "D1", "D2", "D3", "D4"]
complim = ["E1", "E2", "B4", "B5"]

# Defining Functions
# As the name 'displaydata' suggests, this connects to the sql database called 'VMD'--
# and selects the entire table by 'reading' each row and its contents
# The database is stored within the variabe 'result'
def displaydata():
    qry = "select * from VMD;" # SQL uses a different syntax
    result = con.execute(qry)  # This executes the variable 'qry' in the SQL browser
    print("")
    for row in result:         # This reads the data row by row and prints the menu items line by line
        print(f"""{row[1]}
              {row[2]} || {row[3]} ({row[4]}) 
              Amount Left: {row[5]}""")
    t.sleep(3) # This function delays output on the console (next set of code)
    
# The function displays a string message of all the available bundles when called
def bundlemenu():
    print("""
          30% Off The Wazoo!
          ==================
          
          1. Gamer's Choice Award;
          Any one of Doritos chips + Mountain Dew Can 330ml (2.5)
          
          2. Is It Choco-late For Suggestions?;
          Snickers Peanut Chocolate Bar (3.0) + M&M's Milk Chocolate (3.0) +
          Reese's Peanut Butter Cups (3.0) + Galaxy White Chocolate (2.75)
          
          3. Neat Freak; 
          Any food item + Fine Pocket Facial Tissues Pack 10 Sheets (2.5) +
          Cool & Cool Disinfectant 10 Wipes (3.75)
          
          4. Refresher's Party;
          Lipton Lemon Ice Tea Drink 320ml (3.75) + Any Snack item
          
          """)
    t.sleep(3) # The next code is delayed so users have time to read/look at the bundles

# This function is neccessary for when users make payments/edit their cart
# Thus it's crucial to make it seem like the items are all purchased or
# that they are 'cleared' from the cart
def cartclear(cart,cart3,cart4):
    cart.clear()
    cart3.clear()
    cart4.clear()

# This function makes sure the amount available to the User is reduced by the amount added to cart
# It does this by searching for the row the product is by code and update the quantity
# By fetching the value, subtracting it in Python and then returning the value by
# updating the amount column of a product with the new subtracted value.
def decrease(code):
    cur = con.cursor()
    qry = cur.execute("SELECT Amount FROM VMD WHERE Code=?", (code,))
    res = qry.fetchone()
    amount = res[0] - 1
    qry = "UPDATE VMD SET Amount=? where Code=?;"
    con.execute(qry,(amount, code))
    con.commit()

# It is the same as decrease, except it adds to the Amount row.
# This is important when users decide to remove an item or clear all items from their cart
def increase(code):
    cur = con.cursor()
    qry = cur.execute("SELECT Amount FROM VMD WHERE Code=?", (code,))
    res = qry.fetchone()
    amount = res[0] + 1
    qry = "UPDATE VMD SET Amount=? where Code=?;"
    con.execute(qry,(amount, code))
    con.commit()

# The restock function makes use of the UPDATE function of the SQL browser
# It essentially replaces all values in the Amount column with 10
# So it mimics the act of replacing items with more items (restocking)
def restock():
    qry = ("UPDATE VMD SET Amount= 10;")
    con.execute(qry,)
    con.commit()

# As long as the 'ask1' input is not 7 the program will continously repeat
# This makes functions like 
while final == False: 
    check2 = False  # A variable(indicator) that helps check User input for choosing menu options

    print("""
                        ──────────────────── ⋆⋅☼⋅⋆ ─────────────────────
                          W e l c o m e  t o  T h e  Z n a c k  Z o n e.
                                      ────── ⋆⋅☼⋅⋆ ──────
                               
                                  ╭────────────────.★..───╮
                                    1. Purchase an item
                                    2. View bundles 
                                    3. View menu
                                    4. View cart
                                    5. Proceed to payment
                                    6. Restock
                                    7. Quit
                                  ╰───..★.────────────────╯
                             
    ✦　           ✦          ˚　　　　　　.　　. 　 ˚　.　　　　　 .   ✦　　　 　˚　　　　 . 
　　　.   　　˚　　 　　*　　 　　✦　　　.　　.　　　✦　˚ 　　　　 ˚　.˚　　　　✦　　　.　　. 　 ˚　.
                                  """)
                                  
    while check2 == False:
        
        ask1 = int(input("What would you like to do today? "))
        
        if ask1 == 1:
            # Initializing Variables 3
            # If I were to initialize them outside of any while loop, the changes--
            # That take place (assiging True to them) will be forever altered
            # So they need to return to False here so the input checks work continously
            # Also if they were outside, the menu is looping forever, it crashes the program.
            check = False
            check2 = True
            check3 = False
            check4 = False
            check5 = False
            check6 = False
            check7 = False
            check8 = False
            check9 = False
            check10 = False

            displaydata()
            
            # In order to separate details of a single product, dictionary can--
            # be used to filter the code, product, price and then 
            # add them to the associated carts:
            # code is for cart3, product for cart, price for cart2
            # amount is purely for decreasing/increasing the amount available to the User
            filters = {'code' : '',
                       'product' : '',
                       'price' : 0,
                       'amount' : '',}

            cur = con.cursor()
            qry = cur.execute("SELECT Code FROM VMD;")
            res = qry.fetchall()
            vmd = [x[0] for x in res]
            
            while check == False:
                print("\n╭──────── · ·  · · ─────────╮")
                productcode = str(input(" Enter the product code: "))
                print("╰──────── · ·  · · ─────────╯")
                
                if productcode in vmd:
                    cur = con.cursor()
                    qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (productcode,))
                    res = qry.fetchone()
                    
                    filters['amount'] = res[3]
                    filters['code'] = res[0]
                    filters['product'] = res[1]
                    filters['price'] = res[2]
                    check = True
            
                    if filters['amount'] > 0:
                        cart.append(filters['product'])
                        cart3.append(filters['code'])
                        cart4.append(filters['price'])
                        decrease(productcode)
                        cart2 += filters['price']
                        print(f"\n{filters['product']} has been added to the cart!")
                
                        if filters['code'] in bundles:
                            ask2 = int(input("""
              ╭─────────────────────────── · ·  · · ───────────────────────────────╮
               * There is a bundle associated with your order. Would you like to...
              ╰─────────────────────────── · ·  · · ───────────────────────────────╯
                                    ╭────────────.★..────╮
                                      1. View it first?
                                      2. View all bundles?
                                      3. Reject bundle. 
                                    ╰────..★.────────────╯
                                       ══════════════════ 
                                               """))
                            # Anything below the 'if ask9 == 1:' is a pattern of:
                            # Telling the User what bundle/bundles is/are associated with their product 
                            # Asking the User if they want to purchase the first or second or cancel
                            # If purchased, the product(s) are accessed in the VMD and retrieved, then added to cart
                            # If cancelled, the bundle is not purchased and there is no discount
                            if ask2 == 1:
                                print("")
                                if filters['code'] == bundles[2] or filters['code'] == bundles[3] :
                                    print("""\nThe available bundle offers are:
                                       ══════════════════ 
                                   1. Gamer's Choice Award;
                     Any one of Doritos chips + Mountain Dew Can 330ml (2.5)
                                          
                                        2. Neat Freak;
                     Any food item + Fine Pocket Facial Tissues Pack 10 Sheets (2.5) 
                             + Cool & Cool Disinfectant 10 Wipes (3.75)
                                       ══════════════════ 
                                       """)
                                    while check3 == False:
                                        ask6 = int(input("Would you like to add the first or second bundle? (To cancel, press 3) "))
                                        
                                        if ask6 == 1:
                                            print("You chose the Gamer's Choice Award bundle.")
                                               
                                            # One may be wondering, how come this section couldn't have been a function?
                                            # For whatever reason, the function does not run the "cart2 +=" increment line--
                                            # unless it's within the program, please refer to the documentation on more notes.
                                            cur = con.cursor()
                                            qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (complim[2],))
                                            res = qry.fetchone()

                                            filters['amount'] = res[3]
                                            filters['code'] = res[0]
                                            filters['product'] = res[1]
                                            filters['price'] = res[2]
                                
                                            if filters['amount'] > 0:
                                                cart.append(filters['product'])
                                                cart3.append(filters['code'])
                                                cart4.append(filters['price'])
                                                cart2 += filters['price']
                                                print(f"\n{filters['product']} has been added to the cart!")
                                                decrease(complim[2])
                                    
                                            else:
                                                print(f"\n{filters['product']} has run out of stock.")
                                            
                                            discount = True
                                            check3 = True
                                                   
                                        elif ask6 == 2:
                                            print("You chose the Neat Freak bundle.")
                                            cur = con.cursor()
                                            qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (complim[0],))
                                            res = qry.fetchone()

                                            filters['amount'] = res[3]
                                            filters['code'] = res[0]
                                            filters['product'] = res[1]
                                            filters['price'] = res[2]
                                
                                            if filters['amount'] > 0:
                                                cart.append(filters['product'])
                                                cart3.append(filters['code'])
                                                cart4.append(filters['price'])
                                                cart2 += filters['price']
                                                print(f"\n{filters['product']} has been added to the cart!")
                                                decrease(complim[0])
                                    
                                            else:
                                                print(f"\n{filters['product']} has run out of stock.")
                                            
                                            cur = con.cursor()
                                            qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (complim[1],))
                                            res = qry.fetchone()

                                            filters['amount'] = res[3]
                                            filters['code'] = res[0]
                                            filters['product'] = res[1]
                                            filters['price'] = res[2]
                                
                                            if filters['amount'] > 0:
                                                cart.append(filters['product'])
                                                cart3.append(filters['code'])
                                                cart4.append(filters['price'])
                                                cart2 += filters['price']
                                                print(f"\n{filters['product']} has been added to the cart!")
                                                decrease(complim[1])
                                    
                                            else:
                                                print(f"\n{filters['product']} has run out of stock.")
                                            
                                            discount = True
                                            check3 = True
                                            
                                        elif ask6 == 3:
                                            check3 = True
                                            break
                                            
                                        else:
                                            print("\nError. Please enter your choice again.")
                                            
                                elif filters['code'] == bundles[6]:
                                    print("""\nThe available bundle offers are 
                                       ══════════════════ 
                                     1. Gamer's Choice Award;
                       Any one of Doritos chips + Mountain Dew Can 330ml (2.5)
                                       ══════════════════
                                       """)
                                    while check4 == False:
                                        ask6 = input("Would you like to add the bundle? (y/n) ")
                                        
                                        if ask6.lower() == "y":
                                            check4 = True
                                            while check5 == False:
                                                ask7 = input("""Choose your preferred item from the bundle:
                                       ══════════════════ 
                             A3 || Doritos Nacho Cheese Chips (2.75)
                
                             A4 || Doritos Spicy Nacho Chips (2.75)
                                       ══════════════════
                                                """)
                                                
                                                if ask7 == "A3":
                                                    print("You chose the Gamer's Choice Award bundle.")
                                                    cur = con.cursor()
                                                    qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (bundles[2],))
                                                    res = qry.fetchone()

                                                    filters['amount'] = res[3]
                                                    filters['code'] = res[0]
                                                    filters['product'] = res[1]
                                                    filters['price'] = res[2]
                                        
                                                    if filters['amount'] > 0:
                                                        cart.append(filters['product'])
                                                        cart3.append(filters['code'])
                                                        cart4.append(filters['price'])
                                                        cart2 += filters['price']
                                                        print(f"\n{filters['product']} has been added to the cart!")
                                                        decrease(bundles[2])
                                            
                                                    else:
                                                        print(f"\n{filters['product']} has run out of stock.")
                                                        
                                                    discount = True
                                                    check5 = True
                                                    
                                                elif ask7 == "A4":
                                                    print("You chose the Gamer's Choice Award bundle.")
                                                    cur = con.cursor()
                                                    qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (bundles[3],))
                                                    res = qry.fetchone()

                                                    filters['amount'] = res[3]
                                                    filters['code'] = res[0]
                                                    filters['product'] = res[1]
                                                    filters['price'] = res[2]
                                        
                                                    if filters['amount'] > 0:
                                                        cart.append(filters['product'])
                                                        cart3.append(filters['code'])
                                                        cart4.append(filters['price'])
                                                        cart2 += filters['price']
                                                        print(f"\n{filters['product']} has been added to the cart!")
                                                        decrease(bundles[3])
                                            
                                                    else:
                                                        print(f"\n{filters['product']} has run out of stock.")
                                                        
                                                    discount = True
                                                    check5 = True
                                                
                                                else:
                                                    print("\nError. Please enter the code again.")
                                                    
                                        elif ask6.lower() == "n":
                                            print("")
                                            check4 = True
                                        
                                        else:
                                            print("\nError. Please enter your choice again.")
                                 
                                elif filters['code'] == bundles[7] or filters['code'] == bundles[8] or filters['code'] == bundles[9] or filters['code'] == bundles[10]:
                                    print("""\nThe available bundle offers are:
                                       ══════════════════
                             1. Is It Choco-late For Suggestions?;
                 Snickers Peanut Chocolate Bar (3.0) + M&M's Milk Chocolate (3.0)
                + Reese's Peanut Butter Cups (3.0) + Galaxy White Chocolate (2.75)
                                                
                                         2. Neat Freak;
                  Any food item + Fine Pocket Facial Tissues Pack 10 Sheets (2.5) 
                             + Cool & Cool Disinfectant 10 Wipes (3.75)
                                       ══════════════════
                                       """)
                                       
                                    while check6 == False:
                                        ask8 = int(input("Would you like to add the first or second bundle? (To cancel, press 3) "))
                                         
                                        if ask8 == 1:
                                            if filters['code'] == bundles[7]:
                                                print("You chose the Is It Choco-late For Suggestions? bundle.")
                                                for i in range(8,11):
                                                    cur = con.cursor()
                                                    qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (bundles[i],))
                                                    res = qry.fetchone()

                                                    filters['amount'] = res[3]
                                                    filters['code'] = res[0]
                                                    filters['product'] = res[1]
                                                    filters['price'] = res[2]
                                        
                                                    if filters['amount'] > 0:
                                                        cart.append(filters['product'])
                                                        cart3.append(filters['code'])
                                                        cart4.append(filters['price'])
                                                        cart2 += filters['price']
                                                        print(f"\n{filters['product']} has been added to the cart!")
                                                        decrease(bundles[i])
                                            
                                                    else:
                                                        print(f"\n{filters['product']} has run out of stock.")
                                                        
                                                discount = True
                                                check6 = True
                                                
                                            elif filters['code'] == bundles[8]:
                                                print("You chose the Is It Choco-late For Suggestions? bundle.")
                                                cur = con.cursor()
                                                qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (bundles[7],))
                                                res = qry.fetchone()

                                                filters['amount'] = res[3]
                                                filters['code'] = res[0]
                                                filters['product'] = res[1]
                                                filters['price'] = res[2]
                                    
                                                if filters['amount'] > 0:
                                                    cart.append(filters['product'])
                                                    cart3.append(filters['code'])
                                                    cart4.append(filters['price'])
                                                    cart2 += filters['price']
                                                    print(f"\n{filters['product']} has been added to the cart!")
                                                    decrease(bundles[7])
                                        
                                                else:
                                                    print(f"\n{filters['product']} has run out of stock.")
                                                    
                                                for i in range(9,11):
                                                    cur = con.cursor()
                                                    qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (bundles[i],))
                                                    res = qry.fetchone()

                                                    filters['amount'] = res[3]
                                                    filters['code'] = res[0]
                                                    filters['product'] = res[1]
                                                    filters['price'] = res[2]
                                        
                                                    if filters['amount'] > 0:
                                                        cart.append(filters['product'])
                                                        cart3.append(filters['code'])
                                                        cart4.append(filters['price'])
                                                        cart2 += filters['price']
                                                        print(f"\n{filters['product']} has been added to the cart!")
                                                        decrease(bundles[i])
                                            
                                                    else:
                                                        print(f"\n{filters['product']} has run out of stock.")
                                                    
                                                discount = True
                                                check6 = True
                                            
                                            elif filters['code'] == bundles[9]:
                                                print("You chose the Is It Choco-late For Suggestions? bundle.")
                                                cur = con.cursor()
                                                qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (bundles[10],))
                                                res = qry.fetchone()

                                                filters['amount'] = res[3]
                                                filters['code'] = res[0]
                                                filters['product'] = res[1]
                                                filters['price'] = res[2]
                                    
                                                if filters['amount'] > 0:
                                                    cart.append(filters['product'])
                                                    cart3.append(filters['code'])
                                                    cart4.append(filters['price'])
                                                    cart2 += filters['price']
                                                    print(f"\n{filters['product']} has been added to the cart!")
                                                    decrease(bundles[10])
                                        
                                                else:
                                                    print(f"\n{filters['product']} has run out of stock.")
                                                
                                                for i in range(7,9):
                                                    cur = con.cursor()
                                                    qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (bundles[i],))
                                                    res = qry.fetchone()

                                                    filters['amount'] = res[3]
                                                    filters['code'] = res[0]
                                                    filters['product'] = res[1]
                                                    filters['price'] = res[2]
                                        
                                                    if filters['amount'] > 0:
                                                        cart.append(filters['product'])
                                                        cart3.append(filters['code'])
                                                        cart4.append(filters['price'])
                                                        cart2 += filters['price']
                                                        print(f"\n{filters['product']} has been added to the cart!")
                                                        decrease(bundles[i])
                                            
                                                    else:
                                                        print(f"\n{filters['product']} has run out of stock.")
                                                    
                                                discount = True
                                                check6 = True
                                            
                                            else:
                                                print("You chose the Is It Choco-late For Suggestions? bundle.")
                                                for i in range(7,10):
                                                    cur = con.cursor()
                                                    qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (bundles[i],))
                                                    res = qry.fetchone()

                                                    filters['amount'] = res[3]
                                                    filters['code'] = res[0]
                                                    filters['product'] = res[1]
                                                    filters['price'] = res[2]
                                        
                                                    if filters['amount'] > 0:
                                                        cart.append(filters['product'])
                                                        cart3.append(filters['code'])
                                                        cart4.append(filters['price'])
                                                        cart2 += filters['price']
                                                        print(f"\n{filters['product']} has been added to the cart!")
                                                        decrease(bundles[i])
                                            
                                                    else:
                                                        print(f"\n{filters['product']} has run out of stock.")

                                                discount = True
                                                check6 = True
                                              
                                        elif ask8 == 2:
                                            print("You chose the Neat Freak bundle.")
                                            cur = con.cursor()
                                            qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (complim[0],))
                                            res = qry.fetchone()

                                            filters['amount'] = res[3]
                                            filters['code'] = res[0]
                                            filters['product'] = res[1]
                                            filters['price'] = res[2]
                                
                                            if filters['amount'] > 0:
                                                cart.append(filters['product'])
                                                cart3.append(filters['code'])
                                                cart4.append(filters['price'])
                                                cart2 += filters['price']
                                                print(f"\n{filters['product']} has been added to the cart!")
                                                decrease(complim[0])
                                    
                                            else:
                                                print(f"\n{filters['product']} has run out of stock.")
                                            
                                            cur = con.cursor()
                                            qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (complim[1],))
                                            res = qry.fetchone()

                                            filters['amount'] = res[3]
                                            filters['code'] = res[0]
                                            filters['product'] = res[1]
                                            filters['price'] = res[2]
                                
                                            if filters['amount'] > 0:
                                                cart.append(filters['product'])
                                                cart3.append(filters['code'])
                                                cart4.append(filters['price'])
                                                cart2 += filters['price']
                                                print(f"\n{filters['product']} has been added to the cart!")
                                                decrease(complim[1])
                                    
                                            else:
                                                print(f"\n{filters['product']} has run out of stock.")
                                                
                                            discount = True
                                            check6 = True
                                            
                                        elif ask8 == 3:
                                            check6 = True
                                        
                                        else:
                                            print("\nError. Please enter your choice again.")
                                
                                elif filters['code'] == bundles[11] or filters['code'] == bundles[12] or filters['code'] == bundles[13] or filters['code'] == bundles[14]:
                                        print("""\nThe available bundle offers are:
                                        ══════════════════ 
                                      1. Refresher's Party;
                      Lipton Lemon Ice Tea Drink 320ml (3.75) + Any Snack item
                      
                                          2. Neat Freak;
                  Any food item + Fine Pocket Facial Tissues Pack 10 Sheets (2.5) 
                          + Cool & Cool Disinfectant 10 Wipes (3.75)
                                        ══════════════════
                                        """)
                                        
                                        while check7 == False:
                                            ask9 = int(input("Would you like to add the first or second bundle (To cancel, press 3) "))
                                            
                                            if ask9 == 1:
                                                print("You chose the Refresher's Party bundle.")
                                                cur = con.cursor()
                                                qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (complim[3],))
                                                res = qry.fetchone()

                                                filters['amount'] = res[3]
                                                filters['code'] = res[0]
                                                filters['product'] = res[1]
                                                filters['price'] = res[2]
                                    
                                                if filters['amount'] > 0:
                                                    cart.append(filters['product'])
                                                    cart3.append(filters['code'])
                                                    cart4.append(filters['price'])
                                                    cart2 += filters['price']
                                                    print(f"\n{filters['product']} has been added to the cart!")
                                                    decrease(complim[3])
                                        
                                                else:
                                                    print(f"\n{filters['product']} has run out of stock.")
                                                    
                                                discount = True
                                                check7 = True
                                                
                                            elif ask9 == 2:
                                                print("You chose the Neat Freak bundle.")
                                                cur = con.cursor()
                                                qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (complim[0],))
                                                res = qry.fetchone()

                                                filters['amount'] = res[3]
                                                filters['code'] = res[0]
                                                filters['product'] = res[1]
                                                filters['price'] = res[2]
                                    
                                                if filters['amount'] > 0:
                                                    cart.append(filters['product'])
                                                    cart3.append(filters['code'])
                                                    cart4.append(filters['price'])
                                                    cart2 += filters['price']
                                                    print(f"\n{filters['product']} has been added to the cart!")
                                                    decrease(complim[0])
                                        
                                                else:
                                                    print(f"\n{filters['product']} has run out of stock.")
                                                
                                                cur = con.cursor()
                                                qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (complim[1],))
                                                res = qry.fetchone()

                                                filters['amount'] = res[3]
                                                filters['code'] = res[0]
                                                filters['product'] = res[1]
                                                filters['price'] = res[2]
                                    
                                                if filters['amount'] > 0:
                                                    cart.append(filters['product'])
                                                    cart3.append(filters['code'])
                                                    cart4.append(filters['price'])
                                                    cart2 += filters['price']
                                                    print(f"\n{filters['product']} has been added to the cart!")
                                                    decrease(complim[1])
                                        
                                                else:
                                                    print(f"\n{filters['product']} has run out of stock.")
                                                    
                                                discount = True
                                                check7 = True
                                                
                                            elif ask9 == 3:
                                                check7 = True
                                                
                                            else:
                                                print("\nError. Please enter your choice again.")
                                
                                elif filters['code'] == bundles[0] or filters['code'] == bundles[1] or filters['code'] == bundles[4] or filters['code'] == bundles[5] or filters['code'] == bundles[5]:
                                    print("""\nThe available bundle offers are:
                                    ══════════════════ 
                                      1. Neat Freak;
              Any food item + Fine Pocket Facial Tissues Pack 10 Sheets (2.5) 
                      + Cool & Cool Disinfectant 10 Wipes (3.75)
                                    ══════════════════
                                    """)
                                    
                                    while check8 == False:
                                        ask10 = input("Would you like to add this bundle? (y/n) ")
                                        
                                        if ask10 == "y":
                                            print("You chose the Neat Freak bundle.")
                                            cur = con.cursor()
                                            qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (complim[0],))
                                            res = qry.fetchone()

                                            filters['amount'] = res[3]
                                            filters['code'] = res[0]
                                            filters['product'] = res[1]
                                            filters['price'] = res[2]
                                
                                            if filters['amount'] > 0:
                                                cart.append(filters['product'])
                                                cart3.append(filters['code'])
                                                cart4.append(filters['price'])
                                                cart2 += filters['price']
                                                print(f"\n{filters['product']} has been added to the cart!")
                                                decrease(complim[0])
                                    
                                            else:
                                                print(f"\n{filters['product']} has run out of stock.")
                                            
                                            cur = con.cursor()
                                            qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (complim[1],))
                                            res = qry.fetchone()

                                            filters['amount'] = res[3]
                                            filters['code'] = res[0]
                                            filters['product'] = res[1]
                                            filters['price'] = res[2]
                                
                                            if filters['amount'] > 0:
                                                cart.append(filters['product'])
                                                cart3.append(filters['code'])
                                                cart4.append(filters['price'])
                                                cart2 += filters['price']
                                                print(f"\n{filters['product']} has been added to the cart!")
                                                decrease(complim[1])
                                    
                                            else:
                                                print(f"\n{filters['product']} has run out of stock.")
                                                
                                            discount = True
                                            check8 = True
                                        
                                        elif ask10 == "n":
                                            print("")
                                            check8 = False
                                        
                                        else: 
                                            print("\nError. Please enter your choice again.")
                                
                                elif filters['code'] == complim[3]:
                                    print("""\nThe available bundle offers are:
                                    ══════════════════ 
                                  1. Refresher's Party';
               Lipton Lemon Ice Tea Drink 320ml (3.75) + Any Snack item
                                    ══════════════════
                                    """)
                                    
                                    while check9 == False:
                                        ask11 = input("Would you like to add this bundle? (y/n) ")
                                        
                                        if ask11 == "y":
                                            check9 = False
                                            while check10 == False:
                                                ask12 = input("""\nChoose your preferred item from the bundle:
                                   ══════════════════ 
                          D1 || Oreo Original Cookies (1.5)

                     D2 || Tiffany Chunko's Choco Chip Cookies (1.0)

                  D3 || Tiffany Digestive Natural Wheat Biscuits (2.0)

                  D4 || Tiffany Glucose Milk and Honey Biscuits (0.75)
                                   ══════════════════
                                            """)
                                                if ask12 == "D1":
                                                    print("You chose the Refresher's Party bundle.")
                                                    cur = con.cursor()
                                                    qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (bundles[11],))
                                                    res = qry.fetchone()

                                                    filters['amount'] = res[3]
                                                    filters['code'] = res[0]
                                                    filters['product'] = res[1]
                                                    filters['price'] = res[2]
                                        
                                                    if filters['amount'] > 0:
                                                        cart.append(filters['product'])
                                                        cart3.append(filters['code'])
                                                        cart4.append(filters['price'])
                                                        cart2 += filters['price']
                                                        print(f"\n{filters['product']} has been added to the cart!")
                                                        decrease(bundles[11])
                                            
                                                    else:
                                                        print(f"\n{filters['product']} has run out of stock.")
                                                        
                                                    check10 = True
                                                    discount = True
                                                
                                                elif ask12 == "D2":
                                                    print("You chose the Refresher's Party bundle.")
                                                    cur = con.cursor()
                                                    qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (bundles[12],))
                                                    res = qry.fetchone()

                                                    filters['amount'] = res[3]
                                                    filters['code'] = res[0]
                                                    filters['product'] = res[1]
                                                    filters['price'] = res[2]
                                        
                                                    if filters['amount'] > 0:
                                                        cart.append(filters['product'])
                                                        cart3.append(filters['code'])
                                                        cart4.append(filters['price'])
                                                        cart2 += filters['price']
                                                        print(f"\n{filters['product']} has been added to the cart!")
                                                        decrease(bundles[12])
                                            
                                                    else:
                                                        print(f"\n{filters['product']} has run out of stock.")
                                                        
                                                    check10 = True
                                                    discount = True
                                                
                                                elif ask12 == "D3":
                                                    print("You chose the Refresher's Party bundle.")
                                                    cur = con.cursor()
                                                    qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (bundles[13],))
                                                    res = qry.fetchone()

                                                    filters['amount'] = res[3]
                                                    filters['code'] = res[0]
                                                    filters['product'] = res[1]
                                                    filters['price'] = res[2]
                                       
                                                    if filters['amount'] > 0:
                                                       cart.append(filters['product'])
                                                       cart3.append(filters['code'])
                                                       cart4.append(filters['price'])
                                                       cart2 += filters['price']
                                                       print(f"\n{filters['product']} has been added to the cart!")
                                                       decrease(bundles[13])
                                           
                                                    else:
                                                       print(f"\n{filters['product']} has run out of stock.")
                                                       
                                                    check10 = True
                                                    discount = True
                                                
                                                elif ask12 == "D4":
                                                    print("You chose the Refresher's Party bundle.")
                                                    cur = con.cursor()
                                                    qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (bundles[14],))
                                                    res = qry.fetchone()

                                                    filters['amount'] = res[3]
                                                    filters['code'] = res[0]
                                                    filters['product'] = res[1]
                                                    filters['price'] = res[2]
                                        
                                                    if filters['amount'] > 0:
                                                        cart.append(filters['product'])
                                                        cart3.append(filters['code'])
                                                        cart4.append(filters['price'])
                                                        cart2 += filters['price']
                                                        print(f"\n{filters['product']} has been added to the cart!")
                                                        decrease(bundles[14])
                                            
                                                    else:
                                                        print(f"\n{filters['product']} has run out of stock.")
                                                        
                                                    check10 = True
                                                    discount = True
                                                
                                                else:
                                                    print("\nError. Please enter the code again.")
                                        
                                        elif ask11 == "n":
                                            check9 = False
                                            
                                        else:
                                            print("\nError. Please enter your choice again.")
                                        
                            elif ask2 == 2:
                                bundlemenu()
                                
                            elif ask2 == 3:
                                break
            
                    else:
                        print(f"\n{filters['product']} has run out of stock.")
                
                else:
                    print("\nError. Please enter the code again.")
    
    # This option calls the function 'bundlemenu()' to showcase all the available bundles.
        elif ask1 == 2:
            check2 = True
            bundlemenu()
         
    # This option makes the User view the Vending Machine's list of items.
        elif ask1 == 3:
            check2 = True
            displaydata()
    
    # This option displays the items the User has bought and can delete/clear items from the cart
        elif ask1 == 4:
                          # Initializing Variables 3
            check2 = True
            temp4 = False # Used as an indicator to check if User inputted yes or no
            temp5 = False # Used as an indicator to check if User chose options 1 - 3
            temp6 = False # Used as a check for if product code entereed when removing--
                          # an item is correct
        
            if len(cart) > 0:   # The program lets you know you can't view cart if length is 0 (indexes are none)
                                # Initializing Variables 4
                count = 1       # These are important because if I use [i] as an index, in
                x = 0           # the for i in cart loop, it will not work, as the [i] is a--
                                # string type, and so I need two variables for counting as 
                                # the cart3 is a separate string list and cart4 are all float types 
                print("""
Your cart has the following items;
════════════════════════════════════════════════════ """)
                for i in cart:
                    print(f"{count}. {cart3[x]} || {i} ({cart4[x]})")
                    x += 1
                    count += 1

                print(f"""════════════════════════════════════════════════════
Total: {cart2}dhs.""")
        
                while temp4 == False:
                    ask3 = input("\nWould you like to edit your cart? (y/n) ")
            
                    if ask3.lower() == "y":
                        print("""\nNote: Deleting certain items will remove the bundle discount.
             
                               ╭────────────────.★..───╮
                                   1. Delete an item
                                   2. Clear all 
                                   3. Quit
                               ╰───..★.────────────────╯
             """)
                        temp4 = True
                        while temp5 == False:
                            ask4 = int(input("Enter your option: "))
                        
                            if ask4 == 1:
                                while temp6 == False:                            
                                    ask5 = input("Enter the code for the product you wish to remove: ")

                                    if ask5 in cart3:
                                        print("""
                                ╭───── · ·  · · ─────╮
                                     Item removed.
                                ╰───── · ·  · · ─────╯
                                """)
                                        cur = con.cursor()
                                        qry = cur.execute("SELECT Price FROM VMD WHERE Code=?", (ask5,))
                                        res = qry.fetchone()
                                        
                                        # This is separate because you don't need to find 
                                        cart2 -= res[0]
                                        
                                        filters = {'code' : '',
                                                'product' : '',
                                                'price' : 0,}

                                        cur = con.cursor()
                                        qry = cur.execute("SELECT Code, Product, Price, Amount FROM VMD WHERE Code = ?", (ask5,))
                                        res = qry.fetchone()

                                        filters['code'] = res[0]
                                        filters['product'] = res[1]
                                        filters['price'] = res[2]
                                        
                                        # This is a search function being used, once the code is found in the--
                                        # cart, it will find that same code in the VMD database, obtain a copy of
                                        # the details of the product and delete them from each of the carts.
                                        # This is a process of linear searching, the code can be anywhere in the cart
                                        # and it will be deleted once the for loop has gone through the cart and found it
                                        for i in cart3:
                                            if ask5 in cart3:
                                                cart.remove(filters['product'])
                                                cart3.remove(filters['code'])
                                                cart4.remove(filters['price'])
                                                increase(ask5)
                                                break
                                        
                                        temp6 = True
                                        
                                        # If the product was part of a bundle and deleted--
                                        # there'd be no point in having the discount
                                        if ask5 in bundles:
                                            discount = False
                                            
                                    else:
                                        print("Error. Product code not in the cart.")
                                    
                            elif ask4 == 2:
                                x = 0
                                print("""
                                ╭───── · ·  · · ─────╮
                                     Cart cleared.
                                ╰───── · ·  · · ─────╯""")
                                # Everything is gone, no need for discount!
                                discount = False
                                
                                # Cycles through every code in the cart then increases the amount--
                                # available to the user by using the increase(code) function
                                # replicating the act of 'cancelling items/shopping cart'
                                for i in cart:
                                    increase(cart3[x])
                                    x += 1
                                
                                # Clearing out the carts and returning them into empty values/lists
                                cart2 = 0
                                cartclear(cart,cart3,cart4)
                        
                            elif ask4 == 3:
                                temp5 = True
                        
                            else:
                                print("")
                                       
                    elif ask3.lower() == "n":
                        print("")
                        temp4 = True
                    
                    else:
                        print("\nError. Please enter your choice again.")
            else:
                print("\nThere is currently nothing in your cart.")
   
    # This option proceeds with payment for all items in the cart (indexes are none)
    # If there is nothing in the cart, it will not go through with payment
        elif ask1 == 5:
            temp = False             # Used as an indicator if the User inputted enough funds (credit)
            temp2 = False            # Used as an indicator if the User inputted the correct payment type
            check2 = True
            if len(cart) > 0:        # Before payment, the condition checks if the length of the cart list is more than 0
                                     # The program lets you know you can't make payments if length is 0
                while temp2 == False:
                    
                    payment = str(input("\n\nWould you like to pay with cash or credit? "))
                    cashed = 0       # The variable is the bill a User enters
                    casher = 0       # This variable is a 'credits' system of the amount of cash stored
                    count = 1        # Purely for aesthetic, it's to list down the items being dispensed
                    x = 0
            
                    if payment.lower() == "cash":
                        temp2 = True
                        # Adding the discount if True by changing cart2 to its 30% off state
                        if discount == True:
                            offer = (cart2 * 0.3)
                            cart2 -= offer  
                        
                        # As long as the cashed is not equal to cart2 it will run the following
                        while cashed != cart2:
                            print("""
                     +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
                     *This machine only accepts 5/10/20 paper bills.
                     +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+""")
                            cashed = int(input("\nPlease insert a bill: "))
                         
                            if cashed in (5,10,20,0):
                                # I added the increment here so that, when the User inputs enough funds
                                # The User is automatically given the change by the program!
                                # As it checks the casher amount immediately after this, and gives the verdict
                                # If it were outside/in any other line, you would need to input more money--
                                # than neccessary...
                                casher += cashed
                                if casher >= cart2:
                                    print("\n\nYour change will be calculated in a moment. . .")
                                    t.sleep(2)
                                    print(f"\nYour change is: {round(casher-cart2,2)}dhs.")
                                    t.sleep(1)
                                    print("""\nYou purchased the following items;
════════════════════════════════════════════════════""")
                                    for i in cart:
                                        print(f"{count}. {cart3[x]} || {i} ({cart4[x]})")
                                        x += 1
                                        count += 1
                                    cartclear(cart,cart3,cart4)
                                    cart2 = 0
                                    temp = True
                                    temp2 = True
                                    t.sleep(2)
                                    break # If conditions are met, User has successfully cashed out all products
                                    
                                # If conditions are not met User will be given a record of how many credits they have--
                                # and how many more they need left.
                                print(f"> Your credits are now {casher}dhs. You need {round(cart2-casher,2)}dhs more.")
                                
                            else:
                                print("\nError. Please enter the amount again.")
                                
                    elif payment.lower() == "credit":
                        temp2 = True
                        while temp == False:
                            # Credit allows you enter any amount of money.
                            credit =  float(input("Enter the amount of your payment: "))
                   
                            if credit > cart2:
                                print(f"\nYour change is: {round(credit-cart2,2)}dhs.")
                                t.sleep(1)
                                print("""\nYou purchased the following items;
════════════════════════════════════════════════════════════════════════""")
                                for i in cart:
                                    print(f"{count}. {cart3[x]} || {i} ({cart4[x]})")
                                    x += 1
                                    count += 1
                                
                                cartclear(cart,cart3,cart4)
                                cart2 = 0
                                temp = True
                                temp2 = True
                                t.sleep(2)
    
                            else:
                                print("\nYou do not have enough funds. You need {round(cart2-credit,2)}dhs more.")
                           
                    else:
                       print("\nError. Please enter payment type again.")
    
            else:
                print("There's nothing in your cart.")
        
    # This option restocks the entire Vending Machine
        elif ask1 == 6:
            check2 = True
            print("Please wait as we restock the machine. . .")
            restock()
            t.sleep(3)
            print("Restock completed.")
            t.sleep(2)
    
    # This option stops the program entirely, and prints out the last statement
        elif ask1 == 7:
            final = True
            check2 = True

        else:
            print("\nError. Please enter your choice again.\n")

# This is the closing statement, which is what happens when the first while loop is broken
# final = True        
print(""" 
                                   ⋆⁺｡˚⋆˙‧₊☾ ◯ ☽₊‧˙⋆˚｡⁺⋆
                                      Have a good day! 
                  Vendin' Machines and Co make it a pleasure to serve you.""")