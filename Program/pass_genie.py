from random import randint

def passKeyGen(pw_len):
    
    passW = ""

    for i in range(0, pw_len):
        tmp = randint(1, 4)  # using 1 _instead of 0_ to keep the output passW of the full length!
        if tmp == 1:
            index = randint(0, len(txt_Lower)-1)   # length-1 to avoid IndexError: list index out of range
            passW += (txt_Lower[index])
        if tmp == 2:
            index = randint(0, len(txt_Upper)-1)   # length-1 to avoid IndexError: list index out of range
            passW += (txt_Upper[index])
        if tmp == 3:
            index = randint(0, len(txt_Int)-1)     # length-1 to avoid IndexError: list index out of range
            passW += (txt_Int[index])
        if tmp == 4:
            index = randint(0, len(txt_Symbol)-1)  # length-1 to avoid IndexError: list index out of range
            passW += (txt_Symbol[index])
    print("Your new password is:\n{1}\nIts length {0}".format(pw_len, passW))
    
       
txt_Lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
txt_Upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
txt_Int = ["0","1","2","3","4","5","6","7","8","9"]
txt_Symbol = ["£","$","%","^","&","*","(",")","_","-","+","=","[","]","{","}","'","@",":",";","#","~","?","|",".",","]
tmp = 0
index = 0

create_new_pw='y'
while create_new_pw=='y':
    try:
        pw_len_entry=int(input("Enter the preferred password length: "))
        assert pw_len_entry>=12, "For your security! plz choose password length to be 12 characters or more."
        passKeyGen(pw_len_entry)
        create_new_pw = input("Get a new password? (y for yes) or (any other character to terminate.)")
    except AssertionError as e:
        print(e.args)
    except ValueError as v:
        print("Plz renter a number for the password length!!")
