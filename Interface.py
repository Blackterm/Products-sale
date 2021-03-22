import Users
import Mail
import Products
import datetime
import locale
import Admin
import Sales

an = datetime.datetime.now()
locale.setlocale(locale.LC_ALL, '')
kod = "sale"
while True:
    print("""*************************************
    Welcome to the Technology Market.\nTo Become A Member "1" \nFor Member Login "2"\nIf you don't remember your password "3" \nTo exit "q" \nPress...
**********************************""")
    operation = input("The action you will take:")
    if operation == "1":
        Users.Datum().new_user_login()
        break
    elif operation == "2":
        user = Users.Datum().user_control()
        if user == 1:
            Admin.Admin().admin_control()
        else:
            print("******************\nTo view product prices '1'\nFor buy '2'\nTo exit 'q' \nPress....\n******************")
            b = input("Enter value:")
            if b == "1":
                Products.Datum().Products_info()
                break
            elif b == "2":
                Sales.Sales(user.user_name)
            elif b == "q":
                print("Goodbye")
                break
            else:
                print("Invalid transaction....")
    elif operation == "3":
        Mail.Mail().password_control()
        break
    elif operation == "q":
        print("Goodbye")
        break
    else:
        print("Invalid transaction....")