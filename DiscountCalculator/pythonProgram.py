# ------------------------DISCOUNT CALCULATOR APPLICATION----------------------------------------------------

def FP():
    orginalPrice = float(input("WHAT'S THE PRICE ? : $ "))
    discountPercent = int(input("HOW MUCH PERCENT DISCOUNT  : % "))
#--------------------Formula to find Final price with offer----------------------------------
    formulaFinalPrice = round((orginalPrice-orginalPrice*(discountPercent/100)),2)
#----------------------------------------------------------------------------------------
    print(f"\nYOU SHOULD PAY ----> $ {formulaFinalPrice}")
    print(f"YOU SAVE ----> $ {round((orginalPrice-formulaFinalPrice),2)}")

def OP():
    finalPrice = float(input("HOW MUCH DID YOU PAY ? : $ "))
    discountPercent = int(input("WHAT'S THE DISCOUNT OFFER ? : % "))
#-------------------Formula to find orgial price without offer-------------------------------
    formulaOrginalPrice = round((finalPrice/(1-(discountPercent/100))),2)
#--------------------------------------------------------------------------------------------
    print(f"\nTHE ORGINAL PRICE ----> $ {formulaOrginalPrice}")
    print(f"YOU SAVE ----> $ {round((formulaOrginalPrice-finalPrice),2)}")

while True:
    option = int(input("""
     WHAT DO YOU WANT TO FIND ?
     1. OFFER PRICE  
     2. ORGINAL PRICE
     YOU CHOOSE OPTION : """))
    match option:
        case 1:
            FP()
            break
        case 2:
            OP()
            break
        case _: 
            tryagain = input("""
            SORRY THERE IS ONLY OPTION 1 and 2
            DO YOU WHAT TO TRY AGAIN Y or N : """)
            if tryagain == "Y":
                continue
            else:
                print("SEE YOU SOON GOODBYE :-)")
                break

  



#================ NOTES =================

# I have used this fuction because I need this code for other project
# Also used ------MATCH (literal pattern or pattern matching) which is similar to switch case---->>For more info about pattern matching visit :-  
# https://www.python.org/dev/peps/pep-0622/
# Round function - to know more about round() visit :-
# https://docs.python.org/3/library/functions.html#round

#================ ABOUT ME ===============

# This is coded by Sakthiprasath Anbu, connect with me👇...
# LinkedIn  = https://www.linkedin.com/in/sakthiprasathanbu/ 
# Twitter   = https://twitter.com/misterwhiterat/
# Github    = https://github.com/sakthiprasathanbu
# portfolio = https://sakthiprasathanbu.github.io/portfolio/


