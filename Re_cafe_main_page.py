#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing The module Re_cafe_function in this module

import Re_cafe_function

# Importing All the Functions into our Module from Re_cafe_function Module

from Re_cafe_function import *

# Starting The System

while True :
    
    # Print The Greeting's
    
    greeting()
    print()
    
    # Getting the Type of User
    
    user_type = input("Please Specify The User Type! [Type : a for admin or c for customer] : ",)
    user_type = user_type.lower()
    
    # Admin/Master's Page
    
    if user_type == "a" or user_type == "admin" :
        
        # Entering Into The Page For The Varification! 
        
        login = log_in()
        login_value = Re_cafe_function.login_value
        
        # If Login successfully With Correct Login Credentials! 
        
        if login == True or login_value == True :
            
            # Admin System
            
            while True :
                
                # Adding of New Menu Items!
                
                add_menu = input("Do You Want to Add a Item in The Menu! [Type : y for YES or n for NO] : ",)
                add_menu = add_menu.lower()
                
                if add_menu == "y" or add_menu == "yes" :
                    while add_menu == "y" or add_menu == "yes" :
                        add_success = add_menu_item()
                        
                        if add_success == True :
                            print("Added Successfully!!\n")
                            add_menu = input("Do You Want to Add More Item's in The Menu! [Type : y for YES or n for NO] : ",)
                            add_menu = add_menu.lower()
                            
                            if add_menu == "y" or add_menu == "yes" :
                                continue
                            
                            elif add_menu == "n" or add_menu == "no" :
                                break
                            
                            else :    
                                print("Please Write a Valid Input From Next Time!\n")
                        
                        else :
                            pass
                        
                elif add_menu == "n" or add_menu == "no" :
                    pass
                
                else :
                    print("Please Write a Valid Input From Next Time!\n")
                
                # Updating of Menu Items!
                
                update_item = input("Do You Want to Update a Item in The Menu! [Type : y for YES or n for NO] : ",)
                update_item = update_item.lower()
                
                if update_item == "y" or update_item == "yes" :
                    print()
                    print("       *** The Current Menu Details ***")
                    menu_display()
                    update_item_id = input("Please Enter The Item ID Which You Want To Update! : ",)
                    while update_item == "y" or update_item == "yes" :
                        update_success = update_menu(update_item_id)
                        menu_changed = Re_cafe_function.menu_changed
                        
                        if update_success == True or menu_changed == True:
                            print("Updated Successfully!!\n")
                            update_item = input("Do You Want to Update More Item's in The Menu! [Type : y for YES or n for NO] : ",)
                            update_item = update_item.lower()
                            
                            if update_item == "y" or update_item == "yes" :
                                update_item_id = input("Please Enter The Item ID Which You Want To Update! : ",)
                                continue
                            
                            elif update_item == "n" or update_item == "no" :
                                break
                            
                            else :    
                                print("Please Write a Valid Input From Next Time!\n")
                                break
                        else :
                            print("Please Write a Valid Input From Next Time!\n")
                            break
                            
                elif update_item == "n" or update_item == "no" :
                    pass
                
                else :
                    print("Please Write a Valid Input From Next Time!\n")
                
                # Removing of Menu Items!
                
                remove_item = input("Do You Want to Remove a Item From The Menu! [Type : y for YES or n for NO] : ",)
                remove_item = remove_item.lower()
                
                if remove_item == "y" or remove_item == "yes" :
                    print()
                    print("       *** The Current Menu Details ***")
                    menu_display()
                    remove_item_id = input("Please Enter The Item ID Which You Want To Remove! : ",)
                    while remove_item == "y" or remove_item == "yes" :
                        remove_success = item_remove_menu(remove_item_id)
                        
                        if remove_success == True:
                            print("Removed Successfully!!\n")
                            remove_item = input("Do You Want to Remove More Item from The Menu! [Type : y for YES or n for NO] : ",)
                            remove_item = remove_item.lower()
                            
                            if remove_item == "y" or remove_item == "yes" :
                                remove_item_id = input("Please Enter The Item ID Which You Want To Remove! : ",)
                                continue
                            
                            elif remove_item == "n" or remove_item == "no" :
                                break
                            
                            else :    
                                print("Please Write a Valid Input From Next Time!\n")
                        
                        else :
                            break                
                
                elif remove_item == "n" or remove_item == "no" :
                    pass
                
                else :
                    print("Please Write a Valid Input From Next Time!\n")
                
                # Display The Sales Details Done Till Now!
                
                see_history = input("Do You Want to See The Order History! [Type : y for YES or n for NO] : ",)
                see_history = see_history.lower()
                
                if see_history == "y" or see_history == "yes" :
                    order_history()
                
                elif see_history == "n" or see_history == "no" :
                    pass    
                
                else :
                    print("Please Write a Valid Input From Next Time!\n")
                
                # Asking Admin Whether He/She Want to Logout From The Admin/Master Page!
                
                ask_exit = input("Do You Want To Logout and Go To The Home Page! [Type : y for YES or n for NO] : ",)
                ask_exit = ask_exit.lower()
                
                if ask_exit == "y" or ask_exit == "yes" :
                    break
                
                elif ask_exit == "n" or ask_exit == "no" :
                    continue    
                
                else :
                    print("Please Write a Valid Input From Next Time!\n")
                    continue
            
            # Print After Loging Out From The Admin/Master Page!
            
            print()
            print("Successfully LOGOUT From The Admin/Master Page!\n")
            print("Going To The Main/Home Page!")
            print("Please Wait!\n")
    
    # Customer Page For Order
    
    elif user_type == "c" or user_type == "customer" :
        customer_name = input("Please Enter The Customer Name Here! : ",)
        
        # Printing The Menu 
        
        print()
        print("Please Have a Look in The Today's Menu!\n")
        print("       ** Menu **       ")
        menu_display()
        
        # Customer Page
        
        while True :
            
            # Take Order From The Customer! 
            
            ask_order = input("Would You Like to Place Your Order! [Type : y for YES or n for NO] : ",)
            ask_order = ask_order.lower()
            
            if ask_order == "y" or ask_order == "yes" :
                while ask_order == "y" or ask_order == "yes" :
                    print()
                    print("*** TAKING ORDER ***\n")
                    order_item_id = input("Please Enter The Item Id Here! : ",)
                    id_check = check_item_details(order_item_id)
                    
                    if id_check == (True , False) :
                        
                        # Printing The Item Information 
                        
                        menu_info = menu_data()
                        item_info = menu_info[order_item_id]
                        print()
                        print("." * 64)
                        print(":  Item Name  :  " , item_info[0] , " "*(15 - len(item_info[0])) , "::  Item Price  :  " 
                                 , str(item_info[1]) , " "*(6 - len(str(item_info[1]))) , ":"  )
                        print("." * 64,"\n")
                        
                        try :
                            item_qty = int(input("Please Enter The Quantity Here! {Hint : Please Enter The Quantity in Integer!} : ",))
                        
                        except :
                            print("Please Enter a Valid Input!\n")
                            continue
                        
                        else :
                            
                            # Adding the Item To The Cart!
                            
                            add_cart_success = take_order(order_item_id , item_qty)
                            
                            if add_cart_success == True :
                                print("Successfully Added To The Cart!\n")
                                ask_order = input("Would You Like to Order Something Else! [Type : y for YES or n for NO] : ",)
                                ask_order = ask_order.lower()
                                continue
                            
                            else :
                                continue
                    
                    else :
                        print("Please Enter a Valid ITEM ID!\n")
                        continue
            
            elif ask_order == "n" or ask_order == "no" :
                print("Please Take Your Time, See The Menu, And Then Order!!\n")
                continue
            
            else :
                print("Please Write a Valid Input!\n")
                continue
            
            # Asking The Customer, If He/She Want's To Remove Some Item From The Cart!
            
            ask_remove = input("Do You Want To Remove a Item From The Cart! [Type : y for YES or n for NO] : ",)
            ask_remove = ask_remove.lower()
            
            if ask_remove == "y" or ask_remove == "yes" :
                while ask_remove == "y" or ask_remove == "yes" :
                    
                    # Printing The Current Item's Present In The Cart! 
                    
                    cart_item = retrieve_data("cart.txt")
                    print("Current Item In The Cart!")
                    for item in cart_item :
                        print(item)
                        
                    remove_item_id = input("Please Enter The Item Id Here! : ",)
                    remove_order_success = item_remove_order(remove_item_id)
                    
                    if remove_order_success == True :
                        print("Successfully Removed From The Cart!\n")
                        ask_remove = input("Do You Want To Remove more Item From The Cart! [Type : y for YES or n for NO] : ",)
                        ask_remove = ask_remove.lower()
                        
                        if ask_remove == "y" or ask_remove == "yes" :
                            continue
                        
                        elif ask_remove == "n" or ask_remove == "no" : 
                            break
                        
                        else :
                            print("Please Enter A Valid Input!\n")
                            continue
                    else :
                        print("Please Write a Valid Input From Next Time!\n")
                        break
            
            elif ask_remove == "n" or ask_remove == "no" :
                pass
            
            else :
                print("Please Write a Valid Input From Next Time!\n")
                pass
            
            # Asking The Customer, If He/She Want's To Update Some Item From The Cart!
            
            ask_update = input("Do You Want To Update The Quantity of a Item in The Cart! [Type : y for YES or n for NO] : ",)
            ask_update = ask_update.lower()
            
            if ask_update == "y" or ask_update == "yes" :
                while ask_update == "y" or ask_update == "yes" :
                    
                    # Printing The Current Item's Present In The Cart!
                    
                    cart_item = retrieve_data("cart.txt")
                    print("Current Item In The Cart!")
                    for item in cart_item :
                        print(item)
                    
                    update_order_id = input("Please Enter The Item Id Here! : ",)
                    
                    try :
                        update_qty = int(input("Please Enter The Quantity Here! {Hint : Please Enter The Quantity in Integer!} :",))
                    
                    except :
                        print("Please Enter a Valid Input!\n")
                        continue
                    
                    else :
                        update_qty = str(update_qty)
                        update_order_success = update_order(update_order_id , update_qty)
                        
                        if update_order_success == True :
                            print("Successfully Updated The Cart!\n")
                            ask_update = input("Do You Want To Update The Quantity of More Item in The Cart! [Type : y for YES or n for NO] : ",)
                            ask_update = ask_update.lower()
                            
                            if ask_update == "y" or ask_update == "yes" :
                                continue
                            
                            elif ask_update == "n" or ask_update == "no" : 
                                break
                            
                            else :
                                print("Please Enter A Valid Input!\n")
                                continue
                        
                        else :
                            print("Please Write a Valid Input From Next Time!\n")
                            break
            
            elif ask_update == "n" or ask_update == "no" :
                pass
            
            else :
                print("Please Write a Valid Input From Next Time!\n")
                pass
            
            # Asking The Customer, To Confirm The Order!
            
            confirm_order = input("Please Confirm Your Order For The Billing [Type : y for YES or n for NO] : ",)
            confirm_order = confirm_order.lower()
            
            if confirm_order == "y" or confirm_order == "yes" :
                final_order_list = retrieve_data("cart.txt")
                for item_list in final_order_list :
                    item_list[2] = float(item_list[2]) 
                    item_list[3] = int(item_list[3]) 
                
                # Transfer The Item Info. From The Cart To The Order History  
                
                store_order_history = cart_to_order(customer_name)
                
                # Generate and Print The Bill!
                
                bill_success = generate_bill(final_order_list)
                
                # Empty The Cart!
                
                cart_empty_success = empty_cart()
                
                if store_order_history == True and bill_success == True and cart_empty_success == True :
                    print()
                    print("Thanks For Choosing Us! Hope You Will Come Back!\n")
                    break
                
                else :
                    print("An ERROR Occured!")
                    print("Sorry, For The Inconvenience!")
                    print("Please wait\n")
                    continue
            
            else :
                cart_empty_success = empty_cart()
                print("Your Order is Cancelled!")
                print("Sorry, For The Inconvenience!\n")
                break
    
    # In Case If The User Type Is Wrong!
    
    else :
        print()
        print("Please Enter A Valid Input!!\n")
        continue
    
    # If You Want To Exit From The System!
    
    ask_exit = input("Do You Want To Exit From The System! [Type : y for YES or n for NO] : ",)
    ask_exit = ask_exit.lower()
    
    if ask_exit == "y" or ask_exit == "yes" :
        import sys
        sys.exit()
    
    elif ask_exit == "n" or ask_exit == "no" :
        continue    
    
    else :
        print("Please Write a Valid Input From Next Time!\n")
        continue    


# In[2]:


import Re_cafe_function

# Importing All the Functions into our Module from Re_cafe_function Module

from Re_cafe_function import *


# In[3]:


help(Re_cafe_function)


