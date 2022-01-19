#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
This Module have all The Functions which are used in the Main Page of the Re: Cafe!

Arguments:
    No argument Taken

global variable:
    login_value  : variable is use to conform whether the user has successfully login or not.
    menu_changed : variable is use to conform whether the menu has successfully Changed or not.
"""


# **Funtion to get data from the file into a list!!**

# In[2]:


def retrieve_data(path):
    """
    This Function is use to get the data from the File, 
    which contains the data in comma seprated form and
    convert it into a nested list and return that list.

    Arguments:
        path : The path of the .txt file to read in string format.

    Returns:
        Returns a nested list, in which data in each line is converted into a list.
        In the case of an error, it returns None.

    Raises:
        FileNotFoundError: Raises an exception when the file is not found in the specified path.
    """
    try:
        file_data = open(path , mode = "rt" , encoding = "utf-8" )
        list_data = []
        for data in file_data:
            if data != '\n' :
                raw_data = data.strip()
                final_data = raw_data.split(",")
                list_data.append(final_data)
            else:
                pass
        file_data.close()
        return list_data
    except FileNotFoundError :
        print("Please Make Sure That The Path You Have Provided Is Correct!")
        return 
    except Exception as e :
        print("An Error Occured!")
        print("ERROR :",e,"\n")
        return 


# **Funtion to enter data in the file from a list!!**

# In[3]:


def data_entry(path,entry):
    """
    This Function is use to enter the data from the Nested List,
    Into the file in a comma seprated form.
    Each line in the file contains the data of a list(element).

    Arguments:
        path  : The path of the .txt file is to write in string format.
        entry : The Nested List(Which means a List inside a List).

    Returns:
        returns True, if executed succesfully.
        In the case of an error it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try:
        file_open = open(path , mode = "wt" , encoding = "utf-8" )
        data = ""
        for list_data in entry:
            data = ",".join(list_data)            
            final_data = data + "\n"
            file_open.write(final_data)
        file_open.close()
    except Exception as e:
        print("An Error Occured!")
        print("ERROR :",e)
        print("Please Enter A Valid Input!\n")


# **Funtion to Display the menu!!**

# In[4]:


def menu_display():
    """
    This Function is use to retrieve the data from the file cafe_menu.txt,
    into the function using retrieve_data function.
    Then, Print the current Menu Page.

    Arguments:
        No Argument Taken   

    Returns:
        returns the Menu in a Tabular form.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try :
        print()
        print("." * 46)
        print(": Item I.D :        Item        :   Price    :")
        menu_list = retrieve_data("cafe_menu.txt")
        for i in menu_list:
            print("." * 46)
            print(":" , " " , i[0] , " " , ":" , " " , i[1] , " " * (15 - len(i[1])) , ":" , "  " , i[2] , " "*(6 - len(i[2])),":")
        print("." * 46,"\n")
    except Exception as e:
        print("An Error Occured!")
        print("ERROR :",e,"\n")


# **Get The Menu Data in the form of dictionary**

# In[5]:


def menu_data():
    """
    This Function is use to retrieve the data from the file cafe_menu.txt,
    into the function using retrieve_data function.
    Then, convert it into a dictonary with Key as Item_Id and Value as a tuple of name and price.

    Arguments:
        No Argument Taken   

    Returns:
        returns a dictonary with Key as Item_Id and Value as a tuple of name and price.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try :
        menu_dictionary = {}
        menu_list = retrieve_data("cafe_menu.txt")
        for item in menu_list :
            item_id = item[0]
            item_name = item[1]
            item_price = float(item[2])
            menu_dictionary[item_id] = item_name , item_price 
        return menu_dictionary  
    except Exception as e :
        print("An Error Occured!")
        print("ERROR :",e,"\n")  


# **Get The User Data in the form of dictionary**

# In[6]:


def user_data():
    """
    This Function is use to retrieve the data from the file Admin_info.txt,
    into the function using retrieve_data function.
    Then convert it into a dictonary with Key as admin name and Value as the password.

    Arguments:
        No Argument Taken   

    Returns:
        returns a dictonary with Key as admin name and Value as the password.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try :
        user_dictionary = {}
        user_list = retrieve_data("Admin_info.txt")
        for info in user_list :
            user_name = info[1]
            password = info[2]
            user_dictionary[user_name] = password 
        return user_dictionary
    except Exception as e :
        print("An Error Occured!")
        print("ERROR :",e,"\n")


# **Funtion to print Greeting!**

# In[7]:


def greeting(): 
    """
    This Function is use to print the greeting at the start of the program.

    Arguments:
        No Argument Taken   

    Returns:
        print greeting message.

    """
    print(r"                                                                                                                  _")
    print(r" __                __                           _______        _____           _     _______                     | |")
    print(r" \ \              / /                          |__   __|      |  _  \         |_|   | ______|                    | |")
    print(r"  \ \     __     / /                              | |         | |_| /               | |                          | |")
    print(r"   \ \   /__\   / /  __       _  _   _   _   _    | |   _     |  __ \     __        | |          _     __   __   |_|")
    print(r"    \ \_//  \\_/ /  |_   |   |  | | | \_/ | |_    | |  | |    | |  \ \   |_    _    | |_____    /_\   |_   |_     _ ")
    print(r"     \__/    \__/   |__  |_  |_ |_| |     | |_    |_|  |_|    |_|   \_\  |__  |_|   |_______|  /   \  |    |__   |_|")


# **Funtion to check Item Details From the Menu**

# In[8]:


def check_item_details(item_id , item_name = None):
    """
    This Function is use to check whether the Item_Id and Item_Name
    provided matches with that in the DataBase(cafe_menu.txt) File.
    And Returns a tuple with 2 boolean values.
    For Example : if item_id is correct and item_name is wrong
    output      : (True,False)

    Arguments:
        item_id   : The Item ID is written in string format.
        item_name : The Item Name is written in string format and it is not necessary to include(optional argument).
                    Default Value is None.

    Returns:
        Returns a tuple with 2 boolean values.
        For Example : if item_id is correct and item_name is wrong
        output      : (True,False)

    Raises:
        UnknownError: Raises an exception when a error is found.
    """ 
    try :
        menu = menu_data()
        for value in menu:
            if value == item_id :
                if menu[value][0] == item_name :
                    return True , True
                else :
                    return True , False
            elif value != item_id :
                if menu[value][0] == item_name :
                    return False , True                        
            else :    
                pass
        return False , False  
    except Exception as e :
        print("An Error Occured!")
        print("ERROR :",e,"\n")


# **Storing the order details**

# In[9]:


def add_menu_item():
    """
    This Function is use to Add New Menu Items into the File cafe_menu.txt,
    By Using the data_entry function.
    To verify that the Item_Id provided does not exists in the menu to avoid Duplication of the Item_Id,
    check_item_details function is used (as Item_Id is a unique Key/Primary Key).
    After updating the quantity it stores the order back into the cart.txt File.

    Arguments:
        No Argument Taken.
    
    Inputs:
        Take the Unique Item Id and Item Name as an input from the user.

    Returns:
       returns True, if it is is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try :
        old_menu = retrieve_data("cafe_menu.txt")
        print("       *** The Current Menu Details ***")
        menu_display()
        print("Please Enter the Following Detail's!\n")
        item_id = input("Unique Item Id : ",)
        item_name = input("Item Name : ",)
        try :
            item_price = float(input("Item Price :",))
        except:
            print()
            print("Please Enter a valid Item Price!\n")
            return False
        validity = check_item_details(item_id , item_name)
        if validity == (False , False) and item_name != "" :
            item_detail = item_id , item_name , str(item_price)
            item_detail = list(item_detail)
            old_menu.append(item_detail)
            data_entry("cafe_menu.txt",old_menu)
            return True
        else :
            print()
            print("Please Enter a valid Input!")
            print("ERROR : Duplication of Input was Found!\n")
            return False
    except Exception as e :
        print()
        print("An Error Occured!")
        print("ERROR :",e)
        print("Please Enter a valid Input!\n")
        return False


# **Function To Store Order in Cart.txt ; Cart.txt : A Temporary txt file to have the order details**

# In[10]:


def cart(order_list):
    """
    This Function is use to enter(append) the data from the Nested List,
    into the file cart.txt in a comma seperated form.
    Each line in the file contains the data of a list(element).

    Arguments:
        order_list : The Nested List.(A List Inside A List)   

    Returns:
        returns nothing(None).

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try :
        file_cart = open("cart.txt" , mode = "at" , encoding = "utf-8" )
        order = ",".join(order_list)            
        final_order = order + "\n"
        file_cart.write(final_order)
        file_cart.close()
        return
    except Exception as e :
        print("An Error Occured!")
        print("ERROR :",e,"\n")
        return  


# **Taking the Order and Storing it in the Cart.txt File**

# In[11]:


def take_order(item_id , quantity = 1):
    """
    This Function is use to Take Order with the Item_Id and quantity as the inputs.
    And uses check_item_details function to check with that in the DataBase(cafe_menu.txt) File.
    And uses cart function to add the item into the cart.txt File.

    Arguments:
        item_id   : The Item ID is written in string format.
        Quentity  : The Item Quantity is written in integer format.( Default value is 1)

    Returns:
        returns True, if it is is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try :
        check = check_item_details(item_id)
        if check == (True , False) :
            order_list = [item_id,]
            menu_dict = menu_data()
            order_list.append(menu_dict[item_id][0])
            order_list.append(str(menu_dict[item_id][1]))
            order_list.append(str(quantity))
            cart(order_list)
            return True
        else :
            return False
    except Exception as e :
        print("An Error Occured!")
        print("ERROR :",e)
        print("Please Enter a valid Input!\n")
        return False 


# **Function to Generate a Bill**

# In[12]:


def generate_bill(order_list):
    """
    This Function is use to generate the bill from the data in the order_list.
    Then generate the bill and also the total amount to be payed.

    Arguments:
        order_list : The Nested List.(A List Inside A List)
    
    Returns:
        returns True, if it is is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    print()
    print()
    print("                                            ***  BILL  ***                                             ")
    print("." * 106)
    print(":    S.No    :    ITEM ID    :       ITEM NAME       :     PRICE     :    QUANTITY   :    TOTAL AMOUNT   :")
    s_no = 1
    total_amount = 0.0
    try :
        for item in order_list:
            print("." * 106)
            print(":    " , s_no , " " * (5 - len(str(s_no))) , ":    " , item[0] , " " * (8 - len(item[0])) , ":    " , item[1] ,
                  " " * (16 - len(item[1])) , ":    " , item[2] , " " * (8 - len(str(item[2]))) , ":      " , item[3] ,
                  " " * (6 - len(str(item[3]))) , ":     " , item[3]*item[2] , " " * (11 - len(str(item[3]*item[2]))) , ":")
            s_no += 1
            total_amount += item[3]*item[2]
        print("." * 106)
        print()
        print()
        print("." * 55)
        print(":    TOTAL AMOUNT TO PAY IN RUPEES    :    " , total_amount , " " * (8 - len(str(total_amount))) , ":")
        print("." * 55)
        return True
    except Exception as e :    
        print("An Error Occured!")
        print("ERROR :",e,"\n")
        return False


# **Updating The Order Quantity and Stoing it in The Cart.txt File**

# In[13]:


def update_order(item_id , update_qty):
    """
    This Function is use to Update the Item Quentity present in the cart.txt File.
    To verify that the Item_Id provided exists check_item_details funcion is used.
    After updating the quantity it stores the order back into the cart.txt File.

    Arguments:
        item_id    : The Item ID is written in string format.
        update_qty : The Updated Quantity of the item in the string format.

    Returns:
        returns True, if it is is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try :
        check = check_item_details(item_id)
        if check == (True , False) and update_qty != "":
            order = retrieve_data("cart.txt")
            for value in order:
                if value[0] == item_id :
                    value[3] = update_qty
                    data_entry("cart.txt",order)
                    return True
            print("ERROR : The Item does not exit in the cart!")
            print("Please enter a valid Input\n")
            return False
        else :
            print("Please enter a valid Item ID\n")
            return False
    except Exception as e :    
        print("An Error Occured!")
        print("ERROR :",e,"\n")
        return False


# **Function to Log-in into the Admin system and with a global variable to check**

# In[14]:


def log_in(attempts = 3):
    """
    This is a login Function for the Admin, It takes the Admin Name and Admin Password and
    Check the input from the Admin_info.txt File(Data Base).
    The password is taken using getpass method.
    login_value variable is use to confirm whether the user has successfully login or not.
    login_value variable is define globally, so that it can be used outside the function also.  

    Argumentss:
        Attempts : Number of attempts provided to login.
                   Default value is 3.
        
    Inputs:
        Take the Admin Name and Password as the input.

    Returns:
        returns True, if it is is executed succesfully.
        In case of any error, it returns False.
        But after first try function returns None value (Thats why to check use login_value). 

    Raises:
        UnknownError: Raises an exception when a error is found.

    """
    try :
        global login_value
        login_value = False
        if attempts != 0 :
            from getpass import getpass 
            print("Please Enter the following details!\n")
            user_name = input("User Name :",)
            user_name = user_name.lower()
            password = getpass("Password :",)
            print()
            user_list = user_data()
            for user in user_list :
                if user_name == user and password == user_list[user]:
                    login_value = True
                    print("~~~ Log-in successfully!! ~~~\n")
                    print("Welcome" , user_name , "!")
                    return True
            if attempts == 3 or attempts == 2 : 
                print("This is not a valid Username/Password, input Username and Password again please!\n") 
                log_in(attempts - 1)
            elif attempts == 1 :
                print("This is not a valid Username/Password!")
                print("This was your last attempt!")
                print("Please try later!\n")
                login_value = False
                return False
        else :
            login_value = False
            return False
    except Exception as e :    
        print("An Error Occured!")
        print("ERROR :",e,"\n")
        return False


# **Function to Update Menu by the admin!!**

# In[15]:


def update_menu(item_id):
    """
    This Function is use to update the item information present in the cafe_menu.txt file.
    To verify that the Item_Id provided exists in the menu, check_item_details funcion is used.
    After checking, the user can update the Item Name or Item Price or can update both.
    Then, the Function updates the cafe_menu.txt File.
    Also, this Function takes the input, according to the requirment to update the provided fields.

    Arguments:
        item_id : The Item ID is written in the string format.

    Inputs:
        Taking Update field Name, Item Name and Item Price as the input.

    Returns:
        rreturns True, if it is is executed succesfully.
        In case of any error, it returns False.
        But, after first try function, it returns None value.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try :
        global menu_changed 
        menu_changed = False
        check = check_item_details(item_id)
        if check == (True, False) :
            print("Help! {Input : Name/price (if you only want to update one field) or Name,Price (if you want to update both)}")
            update = input("What you want to update [Available field are : Name and Price] : ",)
            update = update.lower()
            update_list = update.split(",")
            menu_list = retrieve_data("cafe_menu.txt")
            for value_list in menu_list:
                if value_list[0] == item_id :
                    new_name = value_list[1]
                    new_price = value_list[2]
                    break
            if len(update_list) == 1 :
                if update_list[0] == "name" or update_list[0] == "item name" :
                    new_name = input("Enter the updated Item name: ",)
                    menu_changed = True
                elif update_list[0] == "price" or update_list[0] == "item price" : 
                    test_price = input("Enter the updated item price: ",)
                    try :
                        new_price = float(test_price)
                        menu_changed = True
                    except Exception as e:
                        print()
                        print("Please Enter a valid Price!{Hint : enter a integer or decimal value as a input}")
                        print("Error :",e,"\n")
                        menu_changed = False
                        update_menu(item_id)
                else :
                    print()
                    print("Please Enter a Vaild Input!\n")
                    menu_changed = False
                    update_menu(item_id)
            elif len(update_list) == 2 :
                if (update_list[0] == "name" or update_list[0] == "item name") and (update_list[1] == "price" or update_list[1] == "item price"):
                    test_name = input("Enter the updated Item name: ",)
                    test_price = input("Enter the updated item price: ",)
                    try :
                        new_price = float(test_price)
                        new_name = test_name
                        menu_changed = True
                    except Exception as e:
                        print()
                        print("Please Enter a valid Price!{Hint : enter a integer or decimal value as a input}")
                        print("Error :",e,"\n")
                        menu_changed = False
                        update_menu(item_id)
                elif (update_list[0] == "price" or update_list[0] == "item price") and (update_list[1] == "name" or update_list[1] == "item name"):
                    test_name = input("Enter the updated Item name: ",)
                    test_price = input("Enter the updated item price: ",)
                    try :
                        new_price = float(test_price)
                        new_name = test_name
                        menu_changed = True
                    except Exception as e:
                        print()
                        print("Please Enter a valid Price!{Hint : enter a integer or decimal value as a input}")
                        print("Error :",e,"\n")
                        menu_changed = False
                        update_menu(item_id)
                else :
                    print()
                    print("Please Enter a Vaild Input!\n")
                    menu_changed = False
                    update_menu(item_id)        

            else :
                    print()
                    print("Please Enter a Vaild Input!\n")
                    menu_changed = False
                    return False
        else :
            menu_changed = False
            return False
        
        if menu_changed == True :
            for value_list in menu_list:
                if value_list[0] == item_id :
                    value_list[1] = new_name
                    value_list[2] = str(new_price)
            data_entry("cafe_menu.txt", menu_list)
            return True
    except Exception as e :    
        print("An Error Occured!")
        print("ERROR :",e,"\n")
        return False 

    
# **Function to Transfer the Order Information into the order_history.txt File**

# In[16]:


def cart_to_order(customer_name):
    """
    This Function is use to enter the data from the cart.txt File into order_history.txt File,
    Data is stored in the order_history.txt file in a comma seprated form with 
    additional customer name added at the last of each line.

    Arguments:
        customer_name : The Name of the Customer is written in the string format.

    Returns:
        returns True, if it is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception, when a error is found.
    """
    try :
        final_order = retrieve_data("cart.txt")
        file_open = open("order_history.txt" , mode = "at" , encoding = "utf-8" )
        data = ""
        for list_data in final_order:
            list_data.append(customer_name)
            data = ",".join(list_data)            
            final_data = data + "\n"
            file_open.write(final_data)
        file_open.close()
        return True
    except Exception as e :    
        print("An Error Occured!")
        print("ERROR :",e,"\n")
        return False


# **Function to Empty the Current Item in the Cart.txt File**

# In[17]:


def empty_cart():
    """
    This Function is used to empty the data from the cart.txt File.

    Arguments:
        No Argument Taken.

    Returns:
        returns True, if it is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try :
        file_open = open("cart.txt" , mode = "wt" , encoding = "utf-8" )
        file_open.write("")
        file_open.close()
        return True
    except Exception as e :    
        print("An Error Occured!")
        print("ERROR :",e,"\n")
        return False


# **Function to Remove an Item From the Menu and Update the cafe_menu.txt File**

# In[18]:


def item_remove_menu(item_id):
    """
    This Function is use to remove items from the information present in the cafe_menu.txt File.
    To verify that the Item_Id provided exists in the menu, check_item_details function is used.
    After checking, The Item's information is removed from the File.
    The,n the Function update the cafe_menu.txt File.

    Arguments:
        item_id : The Item ID is written in string format.

    Returns:
        returns True, if it is is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try:
        check = check_item_details(item_id)
        if check == (True, False):
            menu_list = retrieve_data("cafe_menu.txt")
            new_menu = []
            for value in menu_list:
                if value[0] != item_id:
                    new_menu.append(value)
            data_entry("cafe_menu.txt",new_menu)       
            return True
        else:
            print("Entered Item id was wrong. Please Enter A Valid ID!\n")
            return False
    except Exception as e :    
        print("An Error Occured!")
        print("ERROR :",e,"\n")
        return False


# **Function to Remove an Item From the Order as well as From the cart.txt File**

# In[19]:


def item_remove_order(item_id):
    """
    This Function is used to remove an item from the ordered information present in the cart.txt File.
    To verify that the item_id provided exists in the menu, check_item_details funcion is used.
    After checking, the item's information is removed from the cart.txt File.
    Then, the Function update the cart.txt File.

    Arguments:
        item_id : The Item ID is written in the string format.

    Returns:
        returns True, if it is is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    try:
        check = check_item_details(item_id)
        if check == (True, False):
            order_list = retrieve_data("cart.txt")
            new_order = []
            for value in order_list:
                if value[0] != item_id:
                    new_order.append(value)
            data_entry("cart.txt",new_order)       
            return True
        else:
            print("Entered Item id was wrong. Please Enter A Valid ID!\n")
            return False
    except Exception as e :    
        print("An Error Occured!")
        print("ERROR :",e,"\n")
        return False


# **Function to Get the Order History and to Display it from order_history.txt File!**

# In[20]:


def order_history():
    """
    This Function is use to retrieve the data from the File order_history.txt,
    into the Function using retrieve_data Function.
    Then, print the Customer Order History with the total sale done till now.

    Arguments:
        No Argument Taken   

    Returns:
        returns the Customer Order History in a Tabular form.
        returns True, if is executed succesfully.
        In case of any error, it returns False.

    Raises:
        UnknownError: Raises an exception when a error is found.
    """
    print()
    print("                                      ***  ORDER HISTORY  ***                                             ")
    print("." * 110)
    print(":    S.No    :     CUSTOMER NAME     :   ITEM ID    :       ITEM NAME        :     PRICE     :    QUANTITY   :")
    s_no = 1
    total_sale = 0.0
    order_list = retrieve_data("order_history.txt")
    try :
        for item in order_list:
            print("." * 110)
            print(":    " , s_no , " " * (5 - len(str(s_no))) , ":    " , item[-1] , " " * (16 - len(item[-1])) , ":   " , item[0] ,
                  " " * (8 - len(item[0])) , ":     " , item[1] , " " * (16 - len(str(item[1]))) , ":     " , item[2] ,
                  " " * (7 - len(str(item[2]))) , ":     " , item[3] , " " * (7 - len(item[3])) , ":")
            s_no += 1
            total_sale += (float(item[3]))*(float(item[2]))
        print("." * 110)
        print()
        print()
        print("." * 57)
        print(":    TOTAL SALE TILL NOW IN RUPEES    :    " , total_sale , " " * (10 - len(str(total_sale))) , ":")
        print("." * 57)
        return True
    except Exception as e :    
        print("An Error Occured!")
        print("ERROR :",e,"\n")
        return False
