import sqlite3

class Products():
    def __init__(self,Id,type,name,price,total,):
        self.Id = Id
        self.type = type
        self.name=name
        self.price=price
        self.total=total

class Datum():

    def __init__ (self):
        self.connection()

    def connection(self):
        self.baglanti = sqlite3.connect("market.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists Products (Type TEXT,Products_name TEXT,Price INT,Total INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def Products_info(self):
        self.cursor.execute("Select * From Products  ")
        uye = self.cursor.fetchall()
        for i in uye:
            print("Id:{}\nName:{}\nPrice:{}\nTotal:{}".format(i[0],i[2],i[3],i[4]))
            print("*********************")
    def Products_sales(self,Id):
        self.cursor.execute("Select * From Products where Id = ?",(Id,))
        product = self.cursor.fetchone()
        product1 = Products(Id=product[0],type=product[1],name=product[2],price=product[3],total=product[4])
        return product1

    def Sales (self,total,id):
        self.cursor.execute("UPDATE Products SET Total = ? where id = ?", (total,id))
        self.baglanti.commit()

