#Encryption project made by tech with prakhar
'Please leave the credits of who made this'
'i will be explaining step by step of this program'



#importing modules needed
import random


# asking to set the password
#Why? To access the encryption key
master_password = input("Enter your Master Password to encrypt text and decrypt text")



# the dictionary in which i will check store keys and check keys

encrypt_stored = {
    }
# This will be running in a while loop
#so it runs forever until the user quits

while True:
    #asking the user if they have a key they want to decrypt
    
    convert_message = input("Got a encryption key and want to decrypt it? if so type yes")

    
    #checking input if yes this if statement will function
    
    if convert_message == 'yes':
        
        #asking for key
        
        get_key = input("Paste your key: ")
        
        #searching for the key in a dictionary
        
        print(encrypt_stored.get(get_key))
        
    #if user doesnt have a key this else statement will run
    else:
        print("ok no worries! ")

    # asking for text that needs to be encrypted
    
    user_input = input("Type a text you want encrypted")
    
    #a list of how many characters will be used in the key
    
    key_list = ["!","@","$","%","^","&","*","(",")","1",'2',"3","4","5"]
    
    #making the key variable which will be used
    key = ""

    #this variable checks the length
    value = len(user_input)
    #this for loop starts from 0 to the length of the text
    
    for x in range(0,value):
        
        #makes the random key
        
        key = key + random.choice(key_list)
        
    #stores in a dictionary
        
    encrypt_stored.update({key:user_input})
    
    
    #checks for authentication
    
    auth_password = input("to get the encrypt key you need a master password")
    
    # checks if the key matches master password
    
    if auth_password == master_password:
        
        #prints the key
        
        print(key)
    #if wrong then it will run else
    else:
        print("Wrong master password")
        quit()
        
    # to decrypt key
    
    decrypt_input = input("Enter your encryption key")
    
    # checks if the input matches the key if yes if statement will run
    
    if decrypt_input == key:
        print(user_input)
        
    #if it dosent it will run else
        
    else:
        print("Wrong Key! Try again...")
        pass
    
    #checks for user input if it says bye it quits
    
    if user_input == "bye":
        quit()
    # if bye isnt written it will just pass and do nothing
    else:
        pass



#Sorry for the mess this project explains step by step of what did i do 

    



