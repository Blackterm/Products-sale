import  Users
import datetime
import locale
import Admin
import Products
an = datetime.datetime.now()
locale.setlocale(locale.LC_ALL, '')
kod = "sale"



def Sales (user_name):

    user = Users.Datum().user(user_name)
    Value = input("{}\nThe product you want to buy:".format(Products.Datum().Products_info()))
    Value2 = input("Please enter your code:")
    product = Products.Datum().Products_sales(Value)
    if 0 >= product.total:
        print("Not have product..")
    else:
        if user.balance < product.price:
            print("Do not have your money..")
        else:
            if Value2 == kod:
                product_sales = user.balance - (product.price - product.price * (20 / 100))
                sales = product.total - 1
                Products.Datum().Sales(sales, Value)
            else:
                product_sales = user.balance - product.price
                sales = product.total - 1
                Products.Datum().Sales(sales, Value)
            Users.Datum().user_update(product_sales, user.user_name)
            Admin.Admin().user_sales(user.user_name, user.mail, product.name, datetime.datetime.strftime(an, '%d %B %Y'))


