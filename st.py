import random
from user import users

def display_options(opt_list):
    for idx , opt in enumerate(opt_list,start=1):
        print(f"{idx}.{opt}")

print()
print("WELCOME TO OUR ST BANK OF INDIA ATM")
print()
insert = input("please press 'I' to make your card work: ")

if insert == "I" or insert == 'i':
    print()
    languages = ["ENGLISH", "HINDI"]
    display_options(languages)

    lang_int = input("please insert your comfertable language :  ")
    if lang_int == "2":
        print("sorry for in convinient, your prefert language is not inserted" "to our system , english would be set by default")

    attempt = 1

    while attempt <= 3:

        user_pin = int(input("please insert your account id >>> "))

        if user_pin in users:
            first_name = users[user_pin]["first_name"]
            last_name = users[user_pin]["last_name"]
            account_no = users[user_pin]["account_no"]
            balance = users[user_pin]["balance"]
            currency = users[user_pin]["currency"]
            print(f"hello{first_name}{last_name}.\n"
                   "what would you like to do?")

            options = ["Withdraw", "Change pin", "Check balance"]
            display_options(options)

            optn_int = int(input("Please select from the above option: "))

            while True:
                if optn_int in [1, 2, 3]:
                    if optn_int == 3:
                        print("your account balance"f"{currency}.{balance}")
                    elif optn_int ==1:
                        wdr_optins = ["saving account", "current accout"]
                        display_options(wdr_optins)
                        wdr_int = int(input("select the adove option : "))
                        if wdr_int in [1, 2]:
                            if wdr_int == 2:
                                print("It's not allow to remove money from"    "current acccount")
                                break
                            elif wdr_int == 1:
                                wdn_int = int(input("Please Enter the amount"
                                                    ">>> $ "))
                                if wdn_int > balance:
                                    print("error\nthese much amount is not" 
                                           "there in your account")

                                elif wdn_int > 30000:
                                    OTP = random.randint(00000, 99999)
                                    print(f"\notp: {OTP}\n")
                                    otp_int = int(input("please enter the otp"
                                              "which had been sended to your "
                                              "register mobile number "
                                              "to make transaction:  "))
                                    if OTP == otp_int:
                                        balance -= wdn_int
                                        print("please collect the cash")
                                        print("your account balance is"
                                        f"{currency}.{balance}") 
                                    else:
                                        print("Invalied otp")
                                else:
                                    balance -= wdn_int

                                    print("Please collect your cash!")
                                    print("Your account balance is "
                                      f"{currency}{balance}") 
                            else:
                                 print("Invalide input")
                            break
                    else:
                        currnt_pin = int(input("please enter current pin :"))

                        if currnt_pin in users:
                            new_pin = int(input("please enter new pin: "))
                            if len(str(new_pin)) ==4:
                                temp = users[currnt_pin]
                                del users[currnt_pin]
                                users[new_pin] = temp

                                print("ATM pin succesfully updated")
                            else:
                                print("invalide pin")
                            break
                        else:
                            print("entered ATM pin dosenot match our record")
                    break
                else:
                    print("please select valid option")        
            print("please you can remove your ATM card")
            print("Thanks for visiting ST BANK OF  INDIA\n DO visit next time")      
            break
        else:
            attempt += 1
            print(f"Wrong ATM PIN. You have {4-attempt} attempt remaining")

else:
    print("something went wrong\n card not inserted \n thanks for visiting do visit next time")