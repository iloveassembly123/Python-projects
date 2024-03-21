from pyautogui import password #Import only password prompt

special_characters = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '?', '"', ':', '{', '}', '|', '<', '>')

def check_password_strength(password_to_check):
 if len(password_to_check) >= 8:
        global above_eight_characthers
        above_eight_characthers = True
 else:
        above_eight_characthers = False
       
 if any(char in special_characters for char in password_to_check):
        global have_special_characther
        have_special_characther = True
 else:
        have_special_characther = False

 if any(char.isupper() for char in password_to_check):
        global has_a_capital_char
        has_a_capital_char = True
 else:
        has_a_capital_char = False

               
               
    

password_to_check = str(password(text='Please enter your password', title='Password Prompt', mask='*'))
check_password_strength(password_to_check)
print(f'above_eight_characthers: {above_eight_characthers}')
print(f'have_special_characther: {have_special_characther}')
print(f'has_a_capital_char: {has_a_capital_char}')
if all([above_eight_characthers, have_special_characther, has_a_capital_char]):
    print("All conditions are met")
else:
    print("Either all, or one condition is not met. Please improve your password.")

input("Enter to exit")


