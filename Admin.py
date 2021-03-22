import sqlite3
import Products
class Admin:

    def __init__(self):
        self.connection()

    def connection(self):
        self.baglanti = sqlite3.connect("market.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("Create Table If not exists Sales (User_name TEXT ,Mail TEXT,Received TEXT,Date TEXT)")
        self.baglanti.commit()

    def user_sales(self,User_name,Mail,Received,Date):
        self.cursor.execute("Insert into Sales Values (?,?,?,?)",(User_name,Mail,Received,Date))
        self.baglanti.commit()

    def users_info(self):
        self.cursor.execute("Select * From Sales")
        alan = self.cursor.fetchall()
        for i in alan:
            print("Recipient's name:{} Recipient's mail {}  Product name:{}  Received date:{}".format(i[0], i[1], i[2],i[3]))

    def user_info(self,date):
        self.cursor.execute("Select * From Sales where Date = ? ",(date,))
        alan = self.cursor.fetchall()
        for i in alan:
            print("Recipient's name:{} Recipient's mail {}  \nProduct name:{}  Received date:{}\n*-*-*-*-*-*-*-*-*-*-*-*-*".format(i[0], i[1], i[2],i[3]))

    def admin_control(self):
       while True:
            print(
                """************\nFor up-to-date Stock information "1"\nTo Update Price "2"\nCurrent sales figures "3"\nTo exit 'q'\nPress...\n************ """)
            operation1 = input("The action you will take:")
            if operation1 == "1":
                Products.Datum().Products_info()
                break
            elif operation1 == "2":
                Value1 = input("Product id:")
                urun = Products.Datum().Products_sales(Value1)
                print(urun.name)
                sales1 = input("New price:")
                Products.Datum().Sales(sales1, Value1)

            elif operation1 == "3":
                operation2 = input(
                    "Write all for 'All' sales figures\nWrite a date for sales figures by date.Ex(10 Mart 2020):")
                if operation2 == "All":
                    Admin().users_info()
                else:
                    Admin().user_info(operation2)
            elif operation1 == "q":
                print("Goodbye")
                break

            else:
                print("Invalid transaction....")
