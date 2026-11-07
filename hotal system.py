# Creating variables for the items
burger = "BURGER" 
pizza = "PIZZA"
french_fries = "FRENCH FRIES"
price_of_burger=190
price_of_pizza=200
price_of_french_fries=100

# Displaying the menu and asking for the user's choice
print("Welcome to our Hotel Management System!".upper())
print("We serve the following items:".upper())
print("1.", burger,":",price_of_burger)
print("2.", pizza,":",price_of_pizza)
print("3.",french_fries,":",price_of_french_fries)
print("Which one would you like to have? Please enter your choice: ".upper())
ask=str(input("ENTER WHAT YOU WANT IN THESE THREE:"))
if ask==burger:
    size_of_burger=str(input("ENTER SIZE OF BURGER:"))
    quantity_of_burger=int(input('TELL HOW MUCH BURGER YOU WANT:'))
    if size_of_burger == "SMALL" or size_of_burger == "SLIDER" or size_of_burger == "REGULAR" or size_of_burger == "SMALL SIZE" or size_of_burger == "REGULAR SIZE"and quantity_of_burger >= 1:
            price_of_burger *= quantity_of_burger
            print("THIS IS YOUR ",quantity_of_burger,burger)
            print("THIS IS YOUR AMOUNT:",price_of_burger)
            ask_again=str(input("ENTER Y IF YOU WANT SOMETHING ENTER N IF YOU DONT WANT:"))
            if ask_again=="Y" or ask_again=="YES":
                ask_second_time=str(input("YOU WANT SOMTHING ELSE :"))
                if ask_second_time == pizza:
                    pizza_size_second_time = str(input("ENTER SIZE OF PIZZA:"))
                    quantity_of_pizza_second_time = int(input("ENTER HOW MUCH PIZZA DO YOU WANT:"))
                    if (pizza_size_second_time == "SMALL" or pizza_size_second_time == "PERSONAL SIZE"or pizza_size_second_time == "PERSONAL") and quantity_of_pizza_second_time >= 1:
                        price_of_pizza *= quantity_of_pizza_second_time
                        print("THIS IS YOUR ",quantity_of_pizza_second_time,pizza)
                        print("THIS IS YOUR AMOUNT OF PIZZA :",price_of_pizza)
                        print("THIS IS YOUR TOTAL  AMOUNT:",price_of_pizza+price_of_burger)
                    elif pizza_size_second_time == "MEDIUM" or pizza_size_second_time == "MEDIUM SIZE"and quantity_of_pizza_second_time >= 1:
                        price_of_pizza += 100
                        price_of_pizza *= quantity_of_pizza_second_time
                        print("THIS IS YOUR",quantity_of_pizza_second_time,pizza)
                        print("ON SIZE OF MEDIUM YOU'LL PAY 100 MORE ")
                        print("THIS IS YOUR AMOUNT OF PIZZA:",price_of_pizza)
                        print("THIS IS YOUR TOTAL AMOUNT:",price_of_pizza+price_of_burger)
                    elif pizza_size_second_time == "LARGE" or pizza_size_second_time == "LARGE SIZE"and quantity_of_pizza_second_time >= 1:
                        price_of_pizza += 200
                        price_of_pizza *= quantity_of_pizza_second_time
                        print("ON SIZE OF LARGE YOU'LL PAY 200 MORE ")
                        print("THIS IS YOUR",quantity_of_pizza_second_time,pizza)
                        print("THIS IS AMOUNT OF PIZZA :",price_of_pizza)
                        print("THIS IS YOUR TOTAL AMOUNT:",price_of_pizza+price_of_burger)
                    elif pizza_size_second_time == "EXTRA LARGE" or size_of_pizza_second_time == "EXTRA LARGE SIZE"or pizza_size_second_time == "JUMBO" and quantity_of_pizza_second_time >= 1:
                        price_of_pizza += 300
                        price_of_pizza *= quantity_of_pizza_second_time
                        print("IF YOU SELECT EXTRA LARGE OR JUMBO SO WILL BE PAY 300 MORE:")
                        print("THIS IS YOUR",quantity_of_pizza_second_time,pizza)
                        print("THIS IS YOUR TOTAL AMOUNT:",price_of_pizza+price_of_burger)
                elif ask_second_time == "FRENCH FRIES":
                    size_of_french_fries_second_time = str(input("ENTER SIZE OF FRENCH FRIES: "))
                    quantity_of_french_fries_second_time = int(input("ENTER HOW MUCH FRENCH FRIES DO YOU NEED: "))
                    if (size_of_french_fries_second_time == "SMALL" or size_of_french_fries_second_time == "PERSONAL SIZE" or size_of_french_fries_second_time=="REGULAR" or size_of_french_fries_second_time == "SMALL SIZE" or size_of_french_fries_second_time == "REGULAR SIZE" or size_of_french_fries_second_time == "PERSONAL")and  quantity_of_french_fries_second_time >= 1:
                        price_of_french_fries *= quantity_of_french_fries_second_time
                        print("THIS IS YOUR",quantity_of_french_fries_second_time,french_fries)
                        print("THE PRICE OF FRENCH FRIES",price_of_french_fries)
                        print("THIS IS YOUR TOTAL AMOUNT:",price_of_french_fries+price_of_burger)
                    elif size_of_french_fries_second_time == "MEDIUM" or size_of_french_fries_second_time == "MEDIUM SIZE" and quantity_of_french_fries_second_time>=1:
                        price_of_french_fries += 100
                        price_of_french_fries *= quantity_of_french_fries_second_time
                        print("THIS IS YOUR",quantity_of_french_fries_second_time,french_fries)
                        print("IF YOU SELECT MEDIUM SIZE OF FRENCH FRIES PACKET YOU'LL PAY 100 MORE ")
                        print("THIS IS YOUR TOTAL AMOUNT:",price_of_french_fries+price_of_burger)
                    elif size_of_french_fries_second_time == "LARGE" or size_of_french_fries_second_time == "LARGE SIZE" and quantity_of_french_fries_second_time >= 1:
                        price_of_french_fries += 200
                        price_of_french_fries *= quantity_of_french_fries_second_time
                        print("THIS IS YOUR",quantity_of_french_fries_second_time,french_fries)
                        print("IF YOU SELECT LARGE SIZE SO YOU'LL PAY 200 MORE")
                        print("THIS IS PRICE OF FRENCH FRIES",french_fries)
                        print("THIS IS YOUR AMOUNT:",price_of_french_fries+price_of_burger)
                    elif size_of_french_fries_second_time ==" EXTRA LARGE" or size_of_french_fries_second_time == "FAMILY PACK"or size_of_french_fries_second_time == "BUCKET"and quantity_of_french_fries_second_time >=  1:
                        price_of_french_fries += 300
                        price_of_french_fries *= quantity_of_french_fries_second_time
                        print("THIS IS YOUR",quantity_of_french_fries_second_time,french_fries)
                        print("IF YOU SELECT EXTRA LARGE SIZE SO YOU'LL PAY 300 MORE")
                        print("THIS IS PRICE OF FRENCH FRIES",price_of_french_fries)
                        print("THIS IS YOUR TOTAL AMOUNT:",price_of_french_fries+price_of_burger)  
            elif ask_again == "N" or ask_again=="NO":
                print("AS YOU WISH:")
                print("SO YOU HAVE JUST ",quantity_of_burger,burger)
                print("THIS IS YOUR AMOUNT:",price_of_burger)
    elif size_of_burger == "MEDIUM" or size_of_burger == "MEDIUM SIZE" or size_of_burger == "STANDARD" and quantity_of_burger >= 1:
        price_of_burger += 100
        price_of_burger *= quantity_of_burger
        print("SO YOU HAVE", quantity_of_burger, burger)
        print("IF YOU SELECT MEDIUM SIZE OR STANDARD SO YOU'LL PAY 100 MORE:")
        print("THIS IS YOUR AMOUNT:", price_of_burger)
        ask_second_time = input("DO YOU WANT TO LIKE SOMETHING ELSE OR NOT:")
        if ask_second_time=="Y" or ask_second_time=="YES":
            what_you_want=str(input("ENTER WHAT YOU WANT:"))
            if what_you_want == "PIZZA":
                size_of_pizza_second_time = input("ENTER SIZE OF PIZZA: ")
                quantity_of_pizza_second_time = int(input("ENTER QUANTITY OF PIZZA: "))
                if (size_of_pizza_second_time == "SMALL" or size_of_pizza_second_time == "SMALL SIZE" or size_of_pizza_second_time == "PERSONAL" or size_of_pizza_second_time == "PERSONAL SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("THIS IS YOUR",quantity_of_pizza_second_time, pizza)
                    print("THIS IS YOUR PRICE OF PIZZA :",price_of_pizza)
                    print("THIS IS YOUR TOTAL AMOUNT :", price_of_pizza+price_of_burger)
                elif size_of_pizza_second_time == "MEDIUM" or size_of_pizza_second_time == "MEDIUM SIZE"and quantity_of_pizza_second_time >= 1:
                    price_of_pizza+=100
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("THIS IS YOUR",quantity_of_pizza_second_time, pizza)
                    print("IF YOU SELECT MEDIUM SIZE SO YOU'LL PAY 100 MORE ")
                    print("THIS IS PRICE OF PIZZA :",price_of_pizza)
                    print("THIS IS YOUR TOTAL AMOUNT :", price_of_pizza+price_of_burger)
                elif (size_of_pizza_second_time == "LARGE" or size_of_pizza_second_time == "LARGE SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza+=200
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("THIS IS YOUR",quantity_of_pizza_second_time, pizza)
                    print("IF YOU SELECT LARGE SIZE SO YOU'LL PAY 200 MORE ")
                    print("THIS IS PRICE OF PIZZA :",price_of_pizza)
                    print("THIS IS YOUR TOTAL AMOUNT", price_of_pizza+price_of_burger)
                elif (size_of_pizza_second_time == "EXTRA LARGE" or size_of_pizza_second_time == "EXTRA LARGE SIZE" or size_of_pizza_second_time == "JUMBO" or size_of_pizza_second_time == "JUMBO SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza+=300
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("THIS IS YOUR",quantity_of_pizza_second_time, pizza)
                    print("IF YOU SELECT EXTRA LARGE SIZE  OR JUMBO SIZE SO YOU'LL PAY 300 MORE ")
                    print("THIS IS PRICE OF PIZZA :",price_of_pizza)
                    print("THIS IS YOUR TOTAL AMOUNT", price_of_pizza+price_of_burger) 
            elif what_you_want=="FRENCH FRIES":
                size_of_french_fries_second_time = input("ENTER SIZE OF FRENCH FRIES: ")
                quantity_of_french_fries_second_time = int(input("ENTER QUANTITY OF FRENCH FRIES: "))
                if (size_of_french_fries_second_time == "SMALL" or size_of_french_fries_second_time == "SMALL SIZE" or size_of_french_fries_second_time == "REGULAR" or size_of_french_fries_second_time == "REGULAR SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries*=quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("PRICE OF FRENCH FRIES :",price_of_french_fries)
                    print("THIS IS YOUR AMOUNT:",price_of_french_fries+price_of_burger)
                elif (size_of_french_fries_second_time == "MEDIUM" or size_of_french_fries_second_time == "MEDIUM SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries+=100
                    price_of_french_fries*=quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOU SELECT MEDIUM SIZE SO YOU'LL PAY 100 MORE ")
                    print("PRICE OF FRENCH FRIES :",price_of_french_fries)
                    print("THIS IS YOUR AMOUNT:",price_of_french_fries+price_of_burger)
                elif (size_of_french_fries_second_time == "LARGE" or size_of_french_fries_second_time == "LARGE SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries+=200
                    price_of_french_fries*=quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOU SELECT LARGE SIZE SO YOU'LL PAY 200 MORE ")
                    print("PRICE OF FRENCH FRIES :",price_of_french_fries)
                    print("THIS IS TOTAL AMOUNT:",price_of_french_fries+price_of_burger)
                elif (size_of_french_fries_second_time == "EXTRA LARGE" or size_of_french_fries_second_time == "EXTRA LARGE SIZE" or size_of_french_fries_second_time == "FAMILY PACK" or size_of_french_fries_second_time == "BUCKET") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries+=300
                    price_of_french_fries*=quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOU SELECT EXTRA LARGE OR FAMILY PACK OR BUCKET SO WILL BE PAY 300 MORE:")
                    print("THE PRICE OF FRENCH FRIES :",price_of_french_fries)
                    print("THIS IS YOUR AMOUNT:",price_of_french_fries+price_of_burger)

        elif ask_second_time=="N" or ask_second_time=="NO":
            print("AS YOU WISH:")
            print("SO YOU HAVE JUST",quantity_of_burger,burger)
            print("AND YOUR PRICE IS",price_of_burger)
    elif (size_of_burger == "LARGE" or size_of_burger == "LARGE SIZE" or size_of_burger == "QUARTER POUNDER" or size_of_burger == "DOUBLE PATTY") and quantity_of_burger >= 1:
        price_of_burger+=200
        price_of_burger*=quantity_of_burger
        print("THIS IS YOUR",quantity_of_burger,burger)
        print("IF YOU SELECT LARGE SIZE OR QUARTER POUNDER OR DOUBLE PATTY YOU'LL PAY 200 MORE ")
        print("THIS IS YOUR TOTAL AMOUNT:",price_of_burger)
        ask_second_time=str(input("DOES YOU WANT SOMETHING:"))
        if ask_second_time=="Y" or ask_second_time=="YES":
            ask_again=str(input("ENTER WHAT YOU WANT:"))
            if ask_again == "PIZZA":
                size_of_pizza_second_time = str(input(" ENTER SIZE OF PIZZA : "))
                quantity_of_pizza_second_time = int(input("ENTER HOW MUCH PIZZA DO YOU WANT: "))
                if (size_of_pizza_second_time == "SMALL" or size_of_pizza_second_time == "SMALL SIZE" or size_of_pizza_second_time == "PERSONAL" or size_of_pizza_second_time == "PERSONAL SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza*=quantity_of_pizza_second_time
                    print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                    print("THIS PRICE OF PIZZA :", price_of_pizza)
                    print("THIS IS YOUR TOTAL  AMOUNT:",price_of_pizza+price_of_burger)
                elif (size_of_pizza_second_time == "MEDIUM" or size_of_pizza_second_time == "MEDIUM SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 100
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ", quantity_of_pizza_second_time,pizza)
                    print("IF YOU SELECT MEDIUM SIZE SO YOU'LL PAY 100 MORE ")
                    print("THIS PRICE OF PIZZA :", price_of_pizza)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_pizza+price_of_burger)
                elif (size_of_pizza_second_time == "LARGE" or size_of_pizza_second_time == "LARGE SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 200
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ", quantity_of_pizza_second_time,pizza)
                    print("IF YOU SELECT LARGE SIZE SO YOU'LL PAY 200 MORE ")
                    print("THIS PRICE OF PIZZA :", price_of_pizza)
                    print("THIS IS YOUR TOTAL AMOUNT:", price_of_pizza+price_of_burger)
                elif (size_of_pizza_second_time == "EXTRA LARGE" or size_of_pizza_second_time == "EXTRA LARGE SIZE" or size_of_pizza_second_time =="JUMBO" or size_of_pizza_second_time == "JUMBO SIZE" ) and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 300
                    print("THIS IS YOUR ",quantity_of_pizza_second_time)
                    print("IF YOU SELECT EXTRA LARGE SIZE OR JUMBO SIZE YOU WILL 300 MORE :")
                    print("THE PRICE OF PIZZA ",price_of_pizza)
                    print("THE TOTAL AMOUNT :",price_of_pizza+price_of_burger)
            elif ask_again == "FRENCH FRIES":
                size_of_french_fries_second_time = str(input("ENTER SIZE OF FRENCH FRIES :"))
                quantity_of_french_fries_second_time = int(input("ENTER HOW MUCH FRENCH FRIES DO YOU WANT: "))
                if (size_of_french_fries_second_time == "SMALL" or size_of_french_fries_second_time == "PERSONAL" or size_of_french_fries_second_time == "SMALL SIZE" or size_of_french_fries_second_time == "PERSONAL SIZE" or size_of_french_fries_second_time == "REGULAR" or size_of_french_fries_second_time == "REGULAR SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries*=quantity_of_french_fries_second_time
                    print("HERE IS YOUR",quantity_of_french_fries_second_time,french_fries)
                    print("THIS PRICE OF FRENCH FRIES :",price_of_french_fries)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_french_fries+price_of_burger)
                elif (size_of_french_fries_second_time == "MEDIUM" or size_of_french_fries_second_time == "MEDIUM SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries+=100
                    price_of_french_fries*=quantity_of_french_fries_second_time
                    print("HERE IS YOUR",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOU SELECT MEDIUM SIZE OF FRENCH FRIES PACKET YOU'LL PAY 100 MORE ")
                    print("THIS IS YOUR AMOUNT:",price_of_french_fries)
                    print("THIS IS YOUR TOTAL AMOUNT:",price_of_french_fries+price_of_burger)
                elif (size_of_french_fries_second_time == "LARGE" or size_of_french_fries_second_time == "LARGE SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries+=200
                    price_of_french_fries*=quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOU SELECT LARGE  SIZE OF FRENCH FRIES PACKET YOU'LL PAY 200 MORE ")
                    print("THIS IS YOUR AMOUNT:",price_of_french_fries)
                    print("THIS IS YOUR TOTAL AMOUNT:",price_of_french_fries+price_of_burger)
                elif (size_of_french_fries_second_time == "EXTRA LARGE" or size_of_french_fries_second_time == "EXTRA LARGE SIZE" or size_of_french_fries_second_time == "FAMILY PACK" or size_of_french_fries_second_time == "BUCKET") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries+=300
                    price_of_french_fries*=quantity_of_french_fries_second_time
                    print("HERE IS YOUR",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOU SELECT EXTRA LARGE  SIZE OF FRENCH FRIES PACKET YOU'LL PAY 300 MORE ")
                    print("THIS IS YOUR AMOUNT:",price_of_french_fries)
                    print("THIS IS YOUR TOTAL AMOUNT:",price_of_french_fries+price_of_burger)
        elif ask_second_time=="N" or ask_second_time=="NO":
            print("AS YOU WISH:")
            print("YOU HAVE JUST",quantity_of_burger,burger)
            print("AND THIS IS YOUR FINAL AMOUNT:",price_of_burger)
    elif (size_of_burger == "EXTRA LARGE" or size_of_burger == "EXTRA LARGE SIZE" or size_of_burger == "MONSTER" or size_of_burger == "MONSTER SIZE" or size_of_burger == "TRIPLE PATTY") and quantity_of_burger >= 1:
            price_of_burger += 300
            price_of_burger *= quantity_of_burger
            print("THIS IS YOUR", quantity_of_burger,burger)
            print("IF YOU SELECT EXTRA LARGE SIZE OR MONSTER OR TRIPLE PATTY YOU'LL PAY 300 MORE ")
            print("THIS IS YOUR TOTAL AMOUNT :", price_of_burger)
            ask_again = input("DO YOU WANT SOMTHING ELSE? (YES/Y): ")
            if ask_again == 'YES' or ask_again == 'Y':
                ask_second_time = input("ENTER WHAT YOU WANT: ")
                if ask_second_time == 'PIZZA':
                    size_of_pizza_second_time = input("ENTER SIZE OF PIZZA: ")
                    quantity_of_pizza_second_time = int(input("HOW MUCH IN QUANTITY YOU WANT PIZZA: "))
                    if (size_of_pizza_second_time == 'SMALL' or size_of_pizza_second_time == 'SMALL SIZE' or size_of_pizza_second_time == 'PERSONAL' or size_of_pizza_second_time == 'PERSONAL SIZE') and quantity_of_pizza_second_time >= 1:
                        price_of_pizza*=quantity_of_pizza_second_time
                        print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                        print("THIS IS PRICE OF PIZZA :",price_of_pizza)
                        print("THIS IS YOUR TOTAL AMOUNT:",price_of_pizza+price_of_burger)
                    elif (size_of_pizza_second_time == "MEDIUM" or size_of_pizza_second_time == "MEDIUM SIZE") and quantity_of_pizza_second_time >= 1:
                        price_of_pizza += 100
                        price_of_pizza *= quantity_of_pizza_second_time
                        print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                        print("IF YOU SELECT MEDIUM SIZE YOU WILL PAY 100 MORE ")
                        print("THIS IS PRICE OF PIZZA :",price_of_pizza)
                        print("THERE IS TOTAL  AMOUNT :",price_of_pizza+price_of_burger)
                    elif (size_of_pizza_second_time == "LARGE" or size_of_pizza_second_time == "LARGE SIZE") and quantity_of_pizza_second_time >= 1 :
                        price_of_pizza += 200
                        price_of_pizza *= quantity_of_pizza_second_time
                        print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                        print("IF YOU SELECT LARGE SIZE YOU WILL PAY 200 MORE ")
                        print("THE PRICE OF PIZZA :",price_of_pizza)
                        print("THERE IS TOTAL AMOUNT :",price_of_pizza+price_of_burger)
                    elif (size_of_pizza_second_time == "EXTRA LARGE" or size_of_pizza_second_time == "EXTRA LARGE SIZE" or size_of_pizza_second_time == "JUMBO" or size_of_pizza_second_time == "JUMBO SIZE") and quantity_of_pizza_second_time >= 1:
                        price_of_pizza += 300
                        price_of_pizza *= quantity_of_pizza_second_time
                        print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                        print("IF YOU SELECT EXTRA LARGE SIZE OR JUMBO SIZE YOU WILL PAY 300 MORE ")
                        print("THE PRICE OF PIZZA :",price_of_pizza)
                        print("THERE IS TOTAL AMOUNT :",price_of_pizza+price_of_burger)
                elif ask_second_time == "FRENCH FRIES":
                    size_of_french_fries_second_time = str(input("ENTER SIZE OF FRENCH FRIES : "))
                    quantity_of_french_fries_second_time = int(input("ENTER HOW MUCH : "))
                    if (size_of_french_fries_second_time == "SMALL" or size_of_french_fries_second_time == "SMALL SIZE" or size_of_french_fries_second_time == "REGULAR" or size_of_french_fries_second_time == "REGULAR SIZE") and quantity_of_french_fries_second_time >= 1:
                        price_of_french_fries *= quantity_of_french_fries_second_time
                        print("HERE IS YOUR",quantity_of_french_fries_second_time,french_fries)
                        print("THE PRICE OF FRENCH FRENCH FRIES : ",price_of_french_fries)
                        print("THIS IS YOUR AMOUNT : ",price_of_french_fries+price_of_burger)
                    elif (size_of_french_fries_second_time == "MEDIUM" or size_of_french_fries_second_time == "MEDIUM SIZE") and quantity_of_french_fries_second_time >= 1:
                        price_of_french_fries += 100
                        price_of_french_fries *= quantity_of_french_fries_second_time
                        print("HERE IS YOUR",quantity_of_french_fries_second_time)
                        print("IF YOU SELECT MEDIUM SIZE SO ,YOU PAY MORE 100 ")
                        print("THE PRICE OF FRENCH FRENCH FRIES : ",price_of_french_fries)
                        print("THIS IS TOTAL AMOUNT : ",price_of_french_fries+price_of_burger)
                    elif (size_of_french_fries_second_time == "LARGE" or size_of_french_fries_second_time == "LARGE SIZE") and quantity_of_french_fries_second_time >= 1:
                        price_of_french_fries += 200
                        price_of_french_fries *= quantity_of_french_fries_second_time
                        print("HERE IS YOUR",quantity_of_french_fries_second_time,french_fries)
                        print("IF YOU SELECT LARGE SIZE SO ,YOU PAY MORE 200 ")
                        print("THE PRICE OF FRENCH FRENCH FRIES : ",price_of_french_fries)
                        print("THIS IS TOTAL AMOUNT : ",price_of_french_fries+price_of_burger)
                    elif (size_of_french_fries_second_time == "EXTRA LARGE" or size_of_french_fries_second_time == "EXTRA LARGE SIZE" or size_of_french_fries_second_time == "FAMILY PACKET" or size_of_french_fries_second_time == "FAMILY PACK" or size_of_french_fries_second_time == "BUCKET") and quantity_of_french_fries_second_time >= 1:
                        price_of_french_fries += 300
                        price_of_french_fries *= quantity_of_french_fries_second_time
                        print("HERE IS YOUR",quantity_of_french_fries_second_time,french_fries)
                        print("IF YOU SELECT EXTRA LARGE SIZE OR FAMILY PACKET OR BUCKET  SO ,YOU PAY MORE 300 ")
                        print("THE PRICE OF FRENCH FRENCH FRIES : ",price_of_french_fries)
                        print("THIS IS YOUR AMOUNT : ",price_of_french_fries + price_of_burger)
                
                        
                

# NOW IF YOU  IF USER TELL PIZZA IN FIRST TIME 
                

            

elif ask == pizza:
    size_of_pizza = str(input("ENTER SIZE OF PIZZA : "))
    quantity_of_pizza = int(input("ENTER HOW MUCH PIZZA DO YOU WANT : "))
    if size_of_pizza=="SMALL" or size_of_pizza=="SMALL SIZE" or size_of_pizza=="PERSONAL" or size_of_pizza=="PERSONAL SIZE" and quantity_of_pizza >=1:
        price_of_pizza *= quantity_of_pizza
        print("HERE IS YOUR", quantity_of_pizza,pizza)
        print("THIS IS YOUR AMOUNT:", price_of_pizza)
        ask_again = str(input("DOES YOU WANT SOMETING ELSE:"))
        if ask_again == "Y" or ask_again == "YES":
            ask_second_time=str(input("WHAT YOU WANT :"))
            if ask_second_time == burger:
                size_of_burger_second_time=str(input("ENTER SIZE OF BURGER : "))
                quantity_of_burger_second_time=int(input("ENTER HOW MUCH BURGER YOU NEED : "))
                if (size_of_burger_second_time == "SMALL" or size_of_burger_second_time == "SLIDER" or size_of_burger_second_time == "REGULAR" or size_of_burger_second_time == "SMALL SIZE" or size_of_burger_second_time == "REGULAR SIZE") and quantity_of_burger_second_time >= 1:
                    price_of_burger*=quantity_of_burger_second_time
                    print("THIS IS YOUR",quantity_of_burger_second_time,burger)
                    print("THE PRICE OF BURGER : ",price_of_burger)
                    print("THIS IS YOUR TOTAL AMOUNT :", price_of_burger + price_of_pizza)
                elif (size_of_burger_second_time == "MEDIUM" or size_of_burger_second_time == "MEDIUM SIZE" or size_of_burger_second_time == "STANDARD") and quantity_of_burger_second_time >= 1:
                    price_of_burger+=100
                    price_of_burger*=quantity_of_burger_second_time
                    print("THIS IS YOUR",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE ")
                    print("THE PRICE OF BURGER : ",price_of_burger)
                    print("THIS IS YOUR TOTAL AMOUNT :", price_of_burger + price_of_pizza)
                elif (size_of_burger_second_time == "LARGE" or size_of_burger_second_time == "LARGE SIZE" or size_of_burger_second_time == "QUARTER POUNDER" or size_of_burger_second_time == "DOUBLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger+=200
                    price_of_burger*=quantity_of_burger_second_time
                    print("THIS IS YOUR",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE ")
                    print("THE PRICE OF BURGER : ",price_of_burger)
                    print("THIS IS YOUR TOTAL AMOUNT :", price_of_burger + price_of_pizza ) 
                elif (size_of_burger_second_time == "EXTRA LARGE" or size_of_burger_second_time == "EXTRA LARGE SIZE" or size_of_burger_second_time == "MONSTER" or size_of_burger_second_time == "TRIPLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 300
                    price_of_burger*=quantity_of_burger_second_time
                    print("THIS IS YOUR",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 300 MORE ")
                    print("THE PRICE OF BURGER : ",price_of_burger)
                    print("THIS IS YOUR TOTAL AMOUNT :", price_of_burger + price_of_pizza)
            elif ask_second_time == french_fries:
                size_of_french_fries_second_time = str(input("ENTER SIZE OF FRENCH FRIES : "))
                quantity_of_french_fries_second_time = int(input("ENTER HOW MUCH FRENCH FRIES PACKET : "))
                if (size_of_french_fries_second_time == "SMALL" or size_of_french_fries_second_time == "SMALL SIZE" or size_of_french_fries_second_time == "PERSONAL" or size_of_french_fries_second_time == "PERSONAL SIZE" or size_of_french_fries_second_time == "REGULAR" or size_of_french_fries_second_time == "REGULAR SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("THE AMOUNT OF FRENCH FRIES : ",price_of_french_fries)
                    print("AND THIS IS YOUR TOTAL AMOUNT :",price_of_french_fries + price_of_pizza )
                elif (size_of_french_fries_second_time == "MEDIUM" or size_of_french_fries_second_time == "MEDIUM SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries += 100
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE : ")
                    print("THE AMOUNT OF FRENCH FRIES : ",price_of_french_fries)
                    print("AND THIS IS YOUR TOTAL AMOUNT :",price_of_french_fries + price_of_pizza)
                elif (size_of_french_fries_second_time == "LARGE" or size_of_french_fries_second_time == "LARGE SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries += 200
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE : ")
                    print("THE AMOUNT OF FRENCH FRIES : ",price_of_french_fries)
                    print("AND THIS IS YOUR TOTAL AMOUNT :",price_of_french_fries + price_of_pizza) 
                elif (size_of_french_fries_second_time == "FAMILY PACK SIZE" or size_of_french_fries_second_time == "EXTRA LARGE SIZE" or size_of_french_fries_second_time == "EXTRA LARGE" or size_of_french_fries_second_time == "FAMILY PACKET" or size_of_french_fries_second_time == "FAMILY PACK" or size_of_french_fries_second_time == "BUCKET") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries += 300
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOU SELECT EXTRA LARGE SIZE OR FAMILY PACK OR BUCKET ,SO YOU WILL PAY 300 MORE : ")
                    print("THE AMOUNT OF FRENCH FRIES : ",price_of_french_fries)
                    print("AND THIS IS YOUR TOTAL AMOUNT :",price_of_french_fries + price_of_pizza)
                
                    
        elif ask_again == "N" or ask_again == "NO":
            print("AS YOU WISH ")
            print("HERE IS YOUR", quantity_of_pizza,pizza)
            print("THIS IS YOUR AMOUNT:", price_of_pizza)
    elif (size_of_pizza == "MEDIUM" or size_of_pizza == "MEDIUM SIZE") and quantity_of_pizza >= 1:
        price_of_pizza += 100
        price_of_pizza *= quantity_of_pizza
        print("HERE IS YOUR ",quantity_of_pizza,pizza)
        print("IF YOU SELECT MEDIUM ,SO YOU WILL PAY 100 MORE :")
        print("THIS IS YOUR AMOUNT :",price_of_pizza)
        ask_again = str(input("ENTER YOU WANT SOMETING OR NOT :"))
        if ask_again == "YES" or ask_again == "Y":
            second_time =  str(input("ENTER WHAT YOU WANT :"))
            if second_time == "BURGER" :
                size_of_burger_second_time = str(input("ENTER SIZE OF BURGER : "))
                quantity_of_burger_second_time = int(input("ENTER HOW MUCH BURGER YOU WANT : "))
                if (size_of_burger_second_time == "SMALL" or size_of_burger_second_time == "SMALL SIZE" or size_of_burger_second_time == "REGULAR" or size_of_burger_second_time == "REGULAR SIZE") and quantity_of_burger_second_time >= 1:
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("THE AMOUNT OF BURGER : ",price_of_burger)
                    print("THE AMOUNT :",price_of_burger + price_of_pizza )
                elif (size_of_burger_second_time == "MEDIUM" or size_of_burger_second_time == "MEDIUM SIZE" or size_of_burger_second_time == "STANDARD" or size_of_burger_second_time == "STANDARD SIZE") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 100
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE :")
                    print("THE AMOUNT OF BURGER : ",price_of_burger)
                    print("THE AMOUNT :",price_of_burger + price_of_pizza)
                elif (size_of_burger_second_time == "LARGE" or size_of_burger_second_time == "LARGE SIZE" or size_of_burger_second_time == "QUARTER POUNDER" or size_of_burger_second_time == "DOUBLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 200
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE :")
                    print("THE AMOUNT OF BURGER : ",price_of_burger)
                    print("THE AMOUNT :",price_of_burger + price_of_pizza)
                elif (size_of_burger_second_time == "EXTRA LARGE" or size_of_burger_second_time == "EXTRA LARGE SIZE" or size_of_burger_second_time == "MONSTER" or size_of_burger_second_time == "TRIPLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 300
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 300 MORE :")
                    print("THE AMOUNT OF BURGER : ",price_of_burger)
                    print("THE AMOUNT :",price_of_burger + price_of_pizza)
            elif second_time == "FRENCH FRIES":
                size_of_french_fries_second_time = str(input("ENTER SIZE OF FRENCH FRIES : "))
                quantity_of_french_fries_second_time = int(input("ENTER HOW MUCH FRENCH FRIES DO YOU WANT : "))
                if (size_of_french_fries_second_time == "SMALL" or size_of_french_fries_second_time == "SMALL SIZE" or size_of_french_fries_second_time == "REGULAR" or size_of_french_fries_second_time == "REGULAR SIZE" or size_of_french_fries_second_time == "PERSONAL" or size_of_french_fries_second_time == "PERSONAL SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("THE AMOUNT OF FRENCH FRIES :",price_of_french_fries)
                    print("THE AMOUNT :",price_of_french_fries + price_of_pizza)
                elif (size_of_french_fries_second_time == "MEDIUM" or size_of_french_fries_second_time == "MEDIUM SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries += 100
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOUR SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE :")
                    print("THE AMOUNT OF FRENCH FRIES :",price_of_french_fries)
                    print("THE AMOUNT :",price_of_french_fries + price_of_pizza )
                elif (size_of_french_fries_second_time == "LARGE" or size_of_french_fries_second_time == "LARGE SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries += 200
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOUR SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE :")
                    print("THE AMOUNT OF FRENCH FRIES :",price_of_french_fries)
                    print("THE AMOUNT :",price_of_french_fries + price_of_pizza)
                elif (size_of_french_fries_second_time == "EXTRA LARGE" or size_of_french_fries_second_time == "EXTRA LARGE SIZE" or size_of_french_fries_second_time == "FAMILY PACK" or size_of_french_fries_second_time == "BUCKET" or size_of_french_fries_second_time == "FAMILY PACKET") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries += 300
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOUR SELECT EXTRA LARGE SIZE OR BUCKET OR FAMILY PACKET,SO YOU WILL PAY 300 MORE :")
                    print("THE AMOUNT OF FRENCH FRIES:",price_of_french_fries)
                    print("THE AMOUNT :",price_of_french_fries + price_of_pizza)
        elif ask_again == "N" or ask_again == "NO":
            print("AS YOU WISH:")
            print("HERE IS YOUR", quantity_of_pizza,pizza)
            print("THIS IS YOUR AMOUNT:", price_of_pizza)
    elif (size_of_pizza == "LARGE" or size_of_pizza == "LARGE SIZE") and quantity_of_pizza >= 1:
        price_of_pizza += 200
        price_of_pizza *= quantity_of_pizza
        print("HERE IS YOUR ",quantity_of_pizza,pizza)
        print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE ")
        print("THIS IS YOUR AMOUNT :",price_of_pizza)
        ask_again = str(input("ENTER YOU WANT SOMETING OR NOT :"))
        if ask_again == "YES" or ask_again == "Y":
            second_time == str(input("ENTER WHAT YOU WANT :"))
            if second_time == burger :
                size_of_burger_second_time = str(input("TELL HOW MUCH SIZE DO YOU WANT :"))
                quantity_of_burger_second_time = int(input("ENTER HOW MUCH BURGER YOU WANT :"))
                if (size_of_burger_second_time == "SMALL" or size_of_burger_second_time == "SMALL SIZE" or size_of_burger_second_time == "REGULAR" or size_of_burger_second_time == "REGULAR SIZE") and quantity_of_burger_second_time >= 1:
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("THIS IS YOUR AMOUNT  OF BURGER :",price_of_burger)
                    print("THIS IS YOUR  TOTAL AMOUNT :",price_of_burger + price_of_pizza)
                elif (size_of_burger_second_time == "MEDIUM SIZE" or size_of_burger_second_time == "MEDIUM" or size_of_burger_second_time == "STANDARD" or size_of_burger_second_time == "STANDARD SIZE") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 100
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR",quantity_of_burger_second_time,burger)
                    print("IF YOUR SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE :")
                    print("THIS IS BURGER AMOUNT :",price_of_burger)
                    print("THIS IS  TOTAL AMOUNT :",price_of_burger + price_of_pizza)
                elif (size_of_burger_second_time == "LARGE" or size_of_burger_second_time == "LARGE SIZE" or size_of_burger_second_time == "QUARTER POUNDER" or size_of_burger_second_time == "DOUBLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 200
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR",quantity_of_burger_second_time,burger)
                    print("IF YOUR SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE :")
                    print("THIS IS BURGER AMOUNT :",price_of_burger)
                    print("THIS IS YOUR  TOTAL AMOUNT :",price_of_burger + price_of_pizza)
                elif (size_of_burger_second_time == " EXTRA LARGE" or size_of_burger_second_time == "EXTRA LARGE SIZE" or size_of_burger_second_time == "MONSTER" or size_of_burger_second_time == "TRIPLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 300
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR",quantity_of_burger_second_time,burger)
                    print("IF YOUR SELECT EXTRA LARGE SIZE ,SO YOU WILL PAY 300 MORE :")
                    print("THIS IS BURGER  AMOUNT :",price_of_burger)
                    print("THIS IS YOUR  TOTAL AMOUNT :",price_of_burger + price_of_pizza)
            elif second_time == french_fries:
                size_of_french_fries_second_time = input("ENTER SIZE OF FRENCH FRIES ")
                quantity_of_french_fries_second_time = int(input("HOW MUCH FRENCH FRIES YOU WANT "))
                if (size_of_french_fries_second_time == "SMALL" or size_of_french_fries_second_time == "PERSONAL" or size_of_french_fries_second_time == "PERSONAL SIZE" or size_of_french_fries_second_time == "SMALL SIZE" or size_of_french_fries_second_time == "REGULAR" or size_of_french_fries_second_time == "REGULAR SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("THIS IS YOUR FRENCH FRIES AMOUNT ",price_of_french_fries)
                    print("THIS IS YOUR TOTAL AMOUNT ",price_of_french_fries + price_of_pizza)
                elif (size_of_french_fries_second_time == "MEDIUM" or size_of_french_fries_second_time == "MEDIUM SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries += 100
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOUR SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE :")
                    print("THIS IS YOUR FRENCH FRIES AMOUNT :",price_of_french_fries)
                    print("THIS IS YOUR TOTAL AMOUNT ",price_of_french_fries + price_of_pizza)
                elif (size_of_french_fries_second_time == "LARGE" or size_of_french_fries_second_time == "LARGE SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries += 200
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOUR SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE :")
                    print("THIS IS YOUR FRENCH FRIES AMOUNT :",price_of_french_fries)
                    print("THIS IS YOUR TOTAL AMOUNT ",price_of_french_fries + price_of_pizza)
                elif (size_of_french_fries_second_time == "EXTRA LARGE" or size_of_french_fries_second_time == "EXTRA LARGE SIZE" or size_of_french_fries_second_time == "BUCKET" or size_of_french_fries_second_time == "FAMILY PACK" or size_of_french_fries_second_time == "FAMILY PACK SIZE" or size_of_french_fries_second_time == "FAMILY PACKET") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries += 300
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOUR SELECT EXTRA LARGE SIZE SIZE ,SO YOU WILL PAY 300 MORE :")
                    print("THIS IS YOUR FRENCH FRIES AMOUNT :",price_of_french_fries)
                    print("THIS IS YOUR TOTAL AMOUNT ",price_of_french_fries + price_of_pizza)
        elif ask_again == "N" or ask_again == "NO":
            print("AS YOU WISH")
            print("SO YOU HAVE JUST ",quantity_of_pizza,pizza)
            print("THIS IS YOUR AMOUNT :",price_of_pizza)
    elif (size_of_pizza == "EXTRA LARGE" or size_of_pizza == "EXTRA LARGE SIZE" or size_of_pizza == "JUMBO" or size_of_pizza == "JUMBO SIZE") and quantity_of_pizza >= 1:
        price_of_pizza += 300
        price_of_pizza *= quantity_of_pizza
        print("HERE IS YOUR ",quantity_of_pizza,pizza)
        print("IF YOUR SELECT EXTRA LARGE SIZE SIZE ,SO YOU WILL PAY 300 MORE :")
        print("THIS IS YOUR AMOUNT :",price_of_pizza)
        ask_second_time = str(input("DO YOU WANT SOMETING ?"))
        if ask_second_time == "YES" or ask_second_time == "Y":
            if second_time == french_fries:
                size_of_french_fries_second_time = str(input("ENTER SIZE FRENCH FRIES :"))
                quantity_of_french_fries_second_time = int(input("HOW MUCH BURGER DO YOU WANT :"))
                if (size_of_french_fries_second_time == "SMALL" or size_of_french_fries_second_time == "SMALL SIZE" or size_of_french_fries_second_time == "PERONSAL" or size_of_french_fries_second_time == "PERONSAL SIZE" or size_of_french_fries_second_time == "REGULAR" or size_of_french_fries_second_time == "REGULAR SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("THIS IS YOUR FRENCH FRIES AMOUNT :",price_of_french_fries)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_french_fries + price_of_pizza)
                elif (size_of_french_fries_second_time == "MEDIUM" or size_of_french_fries_second_time == "MEDIUM SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries += 100
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE ")
                    print("THIS IS YOUR  FRENCH FRIES AMOUNT :",price_of_french_fries)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_french_fries + price_of_pizza)
                elif (size_of_french_fries_second_time == "LARGE" or size_of_french_fries_second_time == "LARGE SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries += 200
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE ")
                    print("THIS IS YOUR FRENCH FRIES AMOUNT :",price_of_french_fries)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_french_fries + price_of_pizza)
                elif (size_of_french_fries_second_time == "EXTRA LARGE" or size_of_french_fries_second_time == "EXTRA LARGE SIZE" or size_of_french_fries_second_time == "BUCKET" or size_of_french_fries_second_time == "FAMILY PACK" or size_of_french_fries_second_time == "FAMILY PACKET" or size_of_french_fries_second_time == "FAMILY PACK SIZE") and quantity_of_french_fries_second_time >= 1:
                    price_of_french_fries += 300
                    price_of_french_fries *= quantity_of_french_fries_second_time
                    print("HERE IS YOUR ",quantity_of_french_fries_second_time,french_fries)
                    print("IF YOU SELECT EXTRA LARGE SIZE ,SO YOU WILL PAY 300 MORE ")
                    print("THIS IS YOUR AMOUNT :",price_of_french_fries)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_french_fries + price_of_pizza)
            elif second_time == burger:
                size_of_burger_second_time = str(input("ENTER SIZE OF BURGER :"))
                quantity_of_burger_second_time = int(input("ENTER HOW MUCH BURGER YOU WANT :"))
                if (size_of_burger_second_time == "SMALL" or size_of_burger_second_time == "SMALL SIZE" or size_of_burger_second_time == "PERSONAL SIZE" or size_of_burger_second_time == "PERSONAL" or size_of_burger_second_time == "REGULAR" or size_of_burger_second_time == "REGULAR SIZE") and quantity_of_burger_second_time  >= 1:
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("THIS IS YOUR BURGER AMOUNT :",price_of_burger)
                    print("THIS IS YOUR AMOUNT :",price_of_burger + price_of_pizza )
                elif (size_of_burger_second_time == "MEDIUM" or size_of_burger_second_time == "MEDIUM SIZE" or size_of_burger_second_time == "STANDARD" or size_of_burger_second_time == "STANDARD SIZE") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 100
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE ")
                    print("THIS IS YOUR AMOUNT :",price_of_burger)
                    print("THIS IS YOUR AMOUNT :",price_of_burger + price_of_pizza )
                elif (size_of_burger_second_time == "LARGE" or size_of_burger_second_time == "LARGE SIZE" or size_of_burger_second_time == "QUARTER POUNDER" or size_of_burger_second_time == "DOUBLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 200
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE ")
                    print("THIS IS YOUR AMOUNT :",price_of_burger)
                    print("THIS IS YOUR AMOUNT :",price_of_burger + price_of_pizza )
                elif (size_of_burger_second_time == "EXTRA LARGE" or size_of_burger_second_time == "EXTRA LARGE SIZE" or size_of_burger_second_time == "MONSTER" or size_of_burger_second_time == "TRIPLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 300
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT EXTRA LARGE SIZE ,SO YOU WILL PAY 300 MORE ")
                    print("THIS IS YOUR AMOUNT :",price_of_burger)
                    print("THIS IS YOUR AMOUNT :",price_of_burger + price_of_pizza )
        elif ask_second_time =="NO" or ask_second_time == "N":
            print("AS YOU WISH ")
            print("SO YOU WANT JUST ",quantity_of_pizza,pizza)
            print("AND THIS IS YOUR FINAL AMOUNT :",price_of_pizza)
# NOW IF USER ENTER FRENCH FRIES FIRST TIME SO THIS WILL BE run
elif ask == french_fries :
    size_of_french_fries = str(input("ENTER SIZE OF FRENCH FRIES : "))
    quantity_of_french_fries = int(input("ENTER HOW MUCH FRENCH FRIES : "))
    if (size_of_french_fries == "SMALL" or size_of_french_fries == "SMALL SIZE" or size_of_french_fries == "REGULAR" or size_of_french_fries == "REGULAR SIZE") and quantity_of_french_fries >= 1:
        price_of_french_fries *= quantity_of_french_fries
        print("SO YOU HAVE ",quantity_of_french_fries,french_fries)
        print("AND THIS IS YOUR AMOUNT :",price_of_french_fries)
        ask_again=str(input("DO YOU NEED OF SOMETHING ELSE ? :"))
        if ask_again == "YES" or ask_again == "Y" :
            ask_second_time = str(input("ENTER WHAT YOU WANT : "))
            if ask_second_time == pizza :
                size_of_pizza_second_time = str(input("ENTER SIZE OF PIZZA :"))
                quantity_of_pizza_second_time = int(input("ENTER HOW MUCH PIZZA DO YOU WANT :"))
                if (size_of_pizza_second_time == "SMALL" or size_of_pizza_second_time == "PERSONAL" or size_of_pizza_second_time == "PERSONAL SIZE" or size_of_pizza_second_time == "SMALL SIZE" or size_of_pizza_second_time == "REGULAR" or size_of_pizza_second_time == "REGULAR SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                    print("THIS IS YOUR  PIZZA AMOUNT :",price_of_pizza )
                    print("THIS IS YOUR  TOTAL AMOUNT :",price_of_french_fries + price_of_pizza )
                elif (size_of_pizza_second_time == "MEDIUM"  or size_of_pizza_second_time == "MEDIUM SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 100
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                    print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE" )
                    print("AND THIS IS YOUR  PIZZA AMOUNT :",price_of_pizza)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_pizza + price_of_french_fries )
                elif (size_of_pizza_second_time == "LARGE SIZE"  or size_of_pizza_second_time == "LARGE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 200
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza,)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE" )
                    print("AND THIS IS YOUR PIZZA AMOUNT :",price_of_pizza)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_pizza + price_of_french_fries )
                elif (size_of_pizza_second_time == "EXTRA LARGE"  or size_of_pizza_second_time == "EXTRA LARGE SIZE" or size_of_pizza_second_time == "JUMBO" or size_of_pizza_second_time == "JUMBO SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 300
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                    print("IF YOU SELECT EXTRA LARGE SIZE ,SO YOU WILL PAY 300 MORE" )
                    print("AND THIS IS YOUR PIZZA AMOUNT :",price_of_pizza)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_pizza + price_of_french_fries )
            elif ask_second_time == burger :
                size_of_burger_second_time = input("ENTER SIZE OF BURGER  : ")
                quantity_of_burger_second_time = int(input("ENTER HOW MUCH BURGER DO YOU WANT  : "))
                if (size_of_burger_second_time == "SMALL" or size_of_burger_second_time == "SMALL SIZE" or size_of_burger_second_time == "REGULAR" or size_of_burger_second_time == "REGULAR SIZE") and quantity_of_burger_second_time >= 1:
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print(f"THIS IS YOUR PRICE OF BURGER : {price_of_burger}")
                    print("THIS IS YOUR AMOUNT :",price_of_burger + price_of_french_fries )
                elif (size_of_burger_second_time == "MEDIUM" or size_of_burger_second_time == "MEDIUM SIZE" or size_of_burger_second_time == "STANDARD" or size_of_burger_second_time == "STANDARD SIZE") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 100
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE" )
                    print("AND THIS IS YOUR BURGER AMOUNT :",price_of_burger)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_burger + price_of_french_fries )
                elif (size_of_burger_second_time == "LARGE" or size_of_burger_second_time == "LARGE SIZE" or size_of_burger_second_time == "QUARTER POUNDER" or size_of_burger_second_time == "DOUBLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 200
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE" )
                    print("AND THIS IS YOUR  BURGER AMOUNT :",price_of_burger)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_burger + price_of_french_fries )
                elif (size_of_burger_second_time == "EXTRA LARGE" or size_of_burger_second_time == "EXTRA LARGE SIZE" or size_of_burger_second_time == "MONSTER" or size_of_burger_second_time == "TRIPLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 300
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT EXTRA LARGE SIZE ,SO YOU WILL PAY 300 MORE" )
                    print("AND THIS IS YOUR BURGER  AMOUNT :",price_of_burger)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_burger + price_of_french_fries )
        elif ask_again == "N" or ask_again == "NO" :
            print("AS YOU WISH SIR/MADAM ")
            print("YOU HAVE ONLY JUST ",quantity_of_french_fries,french_fries)
            print("AND THIS FINAL AMOUNT OF YOU ",price_of_french_fries)
    elif (size_of_french_fries == "MEDIUM" or size_of_french_fries == "MEDIUM SIZE") and quantity_of_french_fries >= 1:
        price_of_french_fries += 100
        price_of_french_fries *= quantity_of_french_fries
        print("HERE IS YOUR ",quantity_of_french_fries,french_fries)
        print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE" )
        print("AND THIS IS YOUR AMOUNT :",price_of_french_fries)
        ask_again = str(input("DOES YOU NEED ANYTHING :"))
        if ask_again == "YES" or ask_again ==  "Y" :
            second_time = str(input("WHAT YOU WANT :"))
            if second_time == burger :
                size_of_burger_second_time = str(input("ENTER YOUR SIZE OF BURGER :"))
                quantity_of_burger_second_time = int(input("ENTER HOW MUCH BURGER DO YOU NEED :"))
                if (size_of_burger_second_time == "SMALL" or size_of_burger_second_time == "SMALL SIZE" or size_of_burger_second_time == "REGULAR" or size_of_burger_second_time == "REGULAR SIZE") and quantity_of_burger_second_time >= 1:
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("THIS IS YOUR BURGER AMOUNT :",price_of_burger)
                    print("THIS IS YOUR  AMOUNT :",price_of_burger + price_of_french_fries )
                elif (size_of_burger_second_time == "MEDIUM" or size_of_burger_second_time == "MEDIUM SIZE" or size_of_burger_second_time == "STANDARD" or size_of_burger_second_time == "STANDARD SIZE") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 100
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE" )
                    print("AND THIS IS YOUR BURGER  AMOUNT :",price_of_burger)
                    print("THIS IS YOUR  AMOUNT :",price_of_burger + price_of_french_fries )
                elif (size_of_burger_second_time == "LARGE" or size_of_burger_second_time == "LARGE SIZE" or size_of_burger_second_time == "QUARTER POUNDER" or size_of_burger_second_time == "DOUBLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 200
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE" )
                    print("AND THIS IS YOUR AMOUNT :",price_of_burger)
                    print("THIS IS YOUR  AMOUNT :",price_of_burger + price_of_french_fries )
                elif (size_of_burger_second_time == "EXTRA LARGE" or size_of_burger_second_time == "EXTRA LARGE SIZE" or size_of_burger_second_time == "MONSTER" or size_of_burger_second_time == "TRIPLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 300
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT EXTRA LARGE SIZE ,SO YOU WILL PAY 300 MORE" )
                    print("AND THIS IS YOUR BURGER AMOUNT :",price_of_burger)
                    print("THIS IS YOUR  AMOUNT :",price_of_burger + price_of_french_fries )
            elif second_time == pizza :
                size_of_pizza_second_time = str(input("ENTER SIZE OF PIZZA:"))
                quantity_of_pizza_second_time = int(input("HOW MUCH PIZZA DO YOU WANT :"))
                if (size_of_pizza_second_time == "SMALL" or size_of_pizza_second_time == "PERSONAL" or size_of_pizza_second_time == "PERSONAL SIZE" or size_of_pizza_second_time == "SMALL SIZE" or size_of_pizza_second_time == "REGULAR" or size_of_pizza_second_time == "REGULAR SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ",quantity_of_pizza_second_time)
                    print("AND THIS IS YOUR PIZZA  AMOUNT :",price_of_pizza)
                    print("THIS IS YOUR  AMOUNT :",price_of_pizza + price_of_french_fries )
                elif (size_of_pizza_second_time == "MEDIUM"  or size_of_pizza_second_time == "MEDIUM SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 100
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                    print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE" )
                    print("AND THIS IS YOUR PIZZA AMOUNT :",price_of_pizza)
                    print("THIS IS YOUR  AMOUNT :",price_of_pizza + price_of_french_fries )
                elif (size_of_pizza_second_time == "LARGE"  or size_of_pizza_second_time == "LARGE SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 200
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE" )
                    print("AND THIS IS YOUR PIZZA AMOUNT :",price_of_pizza)
                    print("THIS IS YOUR  AMOUNT :",price_of_pizza + price_of_french_fries )
                elif (size_of_pizza_second_time == "EXTRA LARGE"  or size_of_pizza_second_time == "EXTRA LARGE SIZE" or size_of_pizza_second_time == "JUMBO" or size_of_pizza_second_time == "JUMBO SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 300
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                    print("IF YOU SELECT EXTRA LARGE SIZE ,SO YOU WILL PAY 300 MORE" )
                    print("AND THIS IS YOUR AMOUNT :",price_of_pizza)
                    print("THIS IS YOUR  PIZZA AMOUNT :",price_of_pizza + price_of_french_fries )
        elif ask_again == "N" or ask_again =="NO" :
            print("OK SO YOU JUST HAVE",quantity_of_french_fries,french_fries)
            print("AND THIS IS YOUR FINAL AMOUNT :",price_of_french_fries)
    elif (size_of_french_fries == "LARGE" or size_of_french_fries == "LARGE SIZE") and quantity_of_french_fries >= 1:
        price_of_french_fries += 200
        price_of_french_fries *= quantity_of_french_fries
        print("HERE IS YOUR ",quantity_of_french_fries,french_fries)
        print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE ")
        print("AND THIS IS YOUR AMOUNT :",price_of_french_fries)
        ask_again = str(input("YOU WANT ANYTHING : "))
        if ask_again == "YES" or ask_again == "Y" :
            second_time = str(input("WHAT DO YOU WANT NEXT :"))
            if second_time == pizza :
                size_of_pizza_second_time = str(input("ENTER SIZE OF PIZZA:"))
                quantity_of_pizza_second_time = int(input("HOW MUCH PIZZA DO YOU WANT :"))
                if (size_of_pizza_second_time == "SMALL" or size_of_pizza_second_time == "PERSONAL" or size_of_pizza_second_time == "PERSONAL SIZE" or size_of_pizza_second_time == "SMALL SIZE" or size_of_pizza_second_time == "REGULAR" or size_of_pizza_second_time == "REGULAR SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ",quantity_of_pizza_second_time , pizza)
                    print("AND THIS IS YOUR PRICE OF PIZZA :",price_of_pizza)
                    print("AND THIS IS YOUR TOTAL AMOUNT :",price_of_pizza + price_of_french_fries )
                elif (size_of_pizza_second_time == "MEDIUM"  or size_of_pizza_second_time == "MEDIUM SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 100
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                    print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE ")
                    print("AND THIS IS YOUR PIZZA AMOUNT :",price_of_pizza)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_pizza + price_of_french_fries )
                elif (size_of_pizza_second_time == "LARGE"  or size_of_pizza_second_time == "LARGE SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 200
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE ")
                    print("AND THIS IS YOUR  PIZZA AMOUNT :",price_of_pizza)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_pizza + price_of_french_fries )
                elif (size_of_pizza_second_time == "EXTRA LARGE"  or size_of_pizza_second_time == "EXTRA LARGE SIZE" or size_of_pizza_second_time == "JUMBO" or size_of_pizza_second_time == "JUMBO SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 300
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("IF YOU SELECT EXTRA LARGE SIZE ,SO YOU WILL PAY 300 MORE ")
                    print("HERE IS YOUR ",quantity_of_pizza_second_time,pizza)
                    print("AND THIS IS YOUR PIZZA AMOUNT :",price_of_pizza)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_pizza + price_of_french_fries )
            elif second_time == burger :
                size_of_burger_second_time = str(input("ENTER YOUR SIZE OF BURGER :"))
                quantity_of_burger_second_time = int(input("ENTER HOW MUCH BURGER DO YOU NEED :"))
                if (size_of_burger_second_time == "SMALL" or size_of_burger_second_time == "SMALL SIZE" or size_of_burger_second_time == "REGULAR" or size_of_burger_second_time == "REGULAR SIZE") and quantity_of_burger_second_time >= 1:
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("THIS IS YOUR BURGER AMOUNT :",price_of_burger)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_burger + price_of_french_fries)
                elif (size_of_burger_second_time == "MEDIUM" or size_of_burger_second_time == "MEDIUM SIZE" or size_of_burger_second_time == "STANDARD" or size_of_burger_second_time == "STANDARD SIZE") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 100
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE ")
                    print("AND THIS IS YOUR BURGER AMOUNT :",price_of_burger)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_burger + price_of_french_fries)
                elif (size_of_burger_second_time == "LARGE" or size_of_burger_second_time == "LARGE SIZE" or size_of_burger_second_time == "QUARTER POUNDER" or size_of_burger_second_time == "DOUBLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 200
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE ")
                    print("AND THIS IS YOUR BURGER AMOUNT :",price_of_burger)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_burger + price_of_french_fries)
                elif (size_of_burger_second_time == "EXTRA LARGE" or size_of_burger_second_time == "EXTRA LARGE SIZE" or size_of_burger_second_time == "MONSTER" or size_of_burger_second_time == "TRIPLE PATTY") and quantity_of_burger_second_time >= 1:
                    price_of_burger += 300
                    price_of_burger *= quantity_of_burger_second_time
                    print("HERE IS YOUR ",quantity_of_burger_second_time,burger)
                    print("IF YOU SELECT EXTRA LARGE SIZE ,SO YOU WILL PAY 300 MORE ")
                    print("AND THIS IS YOUR BURGER AMOUNT :",price_of_burger)
                    print("THIS IS YOUR TOTAL AMOUNT :",price_of_burger + price_of_french_fries)
        elif ask_again == "NO" or ask_again == "N" :
            print("OK SO YOU JUST HAVE ",quantity_of_french_fries,french_fries)
            print("AND THIS IS YOUR FINAL AMOUNT :",price_of_french_fries)
    elif (size_of_french_fries == "EXTRA LARGE" or size_of_french_fries == "EXTRA LARGE SIZE" or size_of_french_fries == "BUCKET" or size_of_french_fries == "FAMILY PACK" or size_of_french_fries == "FAMILY PACKET") and quantity_of_french_fries >= 1:
        price_of_french_fries += 300
        price_of_french_fries *= quantity_of_french_fries
        print("HERE IS YOUR", quantity_of_french_fries, "FRENCH FRIES")
        print("IF YOU SELECT EXTRA LARGE SIZE YOU WILL PAY 300 MORE")
        print("AND THIS IS YOUR FRENCH FRIES AMOUNT :",price_of_french_fries)
        ask_again = str(input("YOU WANT SOMETHING ?(Y/N) : "))
        if ask_again == "YES" or ask_again == "Y" :
            what_you_want = str(input("ENTER WHAT YOU WANT :"))
            if what_you_want == pizza :
                size_of_pizza_second_time = input("ENTER WHICH SIZE OF PIZZA YOU WANT : ")
                quantity_of_pizza_second_time = int(input("ENTER HOW MUCH PIZZA YOU WANT :"))
                if (size_of_pizza_second_time == "SMALL" or size_of_pizza_second_time == "PERSONAL" or size_of_pizza_second_time == "PERSONAL SIZE" or size_of_pizza_second_time == "SMALL SIZE" or size_of_pizza_second_time == "REGULAR" or size_of_pizza_second_time == "REGULAR SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR" , quantity_of_pizza_second_time , pizza)
                    print("THE PRICE OF PIZZA :" , price_of_pizza)
                    print("AND THIS IS THE TOTAL AMOUNT :" , price_of_pizza + price_of_french_fries)
                elif (size_of_pizza_second_time == "MEDIUM" or size_of_pizza_second_time == "MEDIUM SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 100
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR" , quantity_of_pizza_second_time , pizza)
                    print("IF YOU SELECT MEDIUM SIZE ,SO YOU WILL PAY 100 MORE")
                    print("THE PRICE OF PIZZA :" , price_of_pizza)
                    print("AND THIS IS THE TOTAL AMOUNT :" , price_of_pizza + price_of_french_fries)
                elif (size_of_pizza_second_time == "LARGE" or size_of_pizza_second_time ==  "LARGE SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 200
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR" , quantity_of_pizza_second_time , pizza)
                    print("IF YOU SELECT LARGE SIZE ,SO YOU WILL PAY 200 MORE")
                    print("THE PRICE OF PIZZA :" , price_of_pizza)
                    print("AND THIS IS THE TOTAL AMOUNT :" , price_of_pizza + price_of_french_fries)
                elif (size_of_pizza_second_time == "EXTRA LARGE" or size_of_pizza_second_time ==  "EXTRA LARGE SIZE" or size_of_pizza_second_time == "JUMBO" or size_of_pizza_second_time == "JUMBO SIZE") and quantity_of_pizza_second_time >= 1:
                    price_of_pizza += 200
                    price_of_pizza *= quantity_of_pizza_second_time
                    print("HERE IS YOUR" , quantity_of_pizza_second_time , pizza)
                    print("IF YOU SELECT EXTRA LARGE SIZE OR JUMBO SIZE ,SO YOU WILL PAY 300 MORE")
                    print("THE PRICE OF PIZZA :" , price_of_pizza)
                    print("AND THIS IS THE TOTAL AMOUNT :" , price_of_pizza + price_of_french_fries)
            elif what_you_want == burger :
                size_of_burger_second_time = input(" ENTER SIZE OF BURGER :")
                quantity_of_burger_second_time = int(input("ENTER HOW MUCH BURGER YOU WANT : "))
                if (size_of_burger_second_time == "SMALL" or size_of_burger_second_time == "SMALL SIZE" or size_of_burger_second_time == "REGULAR" or size_of_burger_second_time == "REGULAR SIZE" ) and quantity_of_burger_second_time >= 1:
                    price_of_burger *= quantity_of_burger_second_time
                    print("THIS IS YOUR " , quantity_of_burger_second_time , burger)
                    print("AND THE PRICE OF BURGER :" , price_of_burger)
                    print("AND THIS IS THE TOTAL AMOUNT : " , price_of_burger + price_of_french_fries)
                elif ( size_of_burger_second_time == "MEDIUM" or size_of_burger_second_time == "MEDIUM SIZE" or size_of_burger_second_time == "STANDARD" or size_of_burger_second_time == "STANDARD SIZE" ) and quantity_of_burger_second_time >= 1:
                    price_of_burger += 100
                    price_of_burger *= quantity_of_burger_second_time
                    print("THIS IS YOUR " , quantity_of_burger_second_time , burger)
                    print("IF YOU SELECT MEDIUM OR STANDRAD SIZE ,SO YOU WILL PAY 100 MORE ")
                    print("AND THE PRICE OF BURGER :" , price_of_burger)
                    print("AND THIS IS THE TOTAL AMOUNT : " , price_of_burger + price_of_french_fries)
                elif ( size_of_burger_second_time == "LARGE" or size_of_burger_second_time == "LARGE SIZE" or size_of_burger_second_time == "QUARTER POUNDER" or size_of_burger_second_time == "DOUBLE PATTY" or size_of_burger_second_time == "DOUBLE PATTY SIZE" or size_of_burger_second_time == "QUARTER POUNDER SIZE" ) and quantity_of_burger_second_time >= 1:
                    price_of_burger += 200
                    price_of_burger *= quantity_of_burger_second_time
                    print("THIS IS YOUR " , quantity_of_burger_second_time , burger)
                    print("IF YOU SELECT LARGE OR QUARTER POUNDER OR DOUBLE PATTY SIZE ,SO YOU WILL PAY 200 MORE ")
                    print("AND THE PRICE OF BURGER :" , price_of_burger)
                    print("AND THIS IS THE TOTAL AMOUNT : " , price_of_burger + price_of_french_fries)
                elif ( size_of_burger_second_time == "EXTRA LARGE" or size_of_burger_second_time == "EXTRA LARGE SIZE" or size_of_burger_second_time == "MONSTER" or size_of_burger_second_time == "TRIPLE PATTY" or size_of_burger_second_time == "TRIPLE PATTY SIZE" or size_of_burger_second_time == "MONSTER SIZE" ) and quantity_of_burger_second_time >= 1:
                    price_of_burger += 300
                    price_of_burger *= quantity_of_burger_second_time
                    print("THIS IS YOUR " , quantity_of_burger_second_time , burger)
                    print("IF YOU SELECT EXTRA  LARGE OR MONSTER OR TRIPLE PATTY SIZE ,SO YOU WILL PAY 300 MORE ")
                    print("AND THE PRICE OF BURGER :" , price_of_burger)
                    print("AND THIS IS THE TOTAL AMOUNT : " , price_of_burger + price_of_french_fries)
        elif ask_again == "NO" or ask_again == "N" :
            print("SO YOU HAVE JUST " , quantity_of_french_fries , french_fries)
            print("AND YOUR TOTAL AMOUNT :" , price_of_french_fries)


                
else :
    print("SORRY WE DIDN'T SURVE THIS ")
