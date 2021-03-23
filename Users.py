import sqlite3
import time
import Mail


class User():
    def __init__(self, name, last_name, user_name, password, mail, balance):
        self.name = name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.mail = mail
        self.balance = balance


class Datum():

    def __init__(self):
        self.connection()

    def connection(self):
        self.baglanti = sqlite3.connect("market.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists Users (Name TEXT,Last_name TEXT,User_name TEXT,Password INT,mail TEXT,Balance INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def user_login(self, user):
        self.cursor.execute("Insert into Users Values(?,?,?,?,?,?)",
                            (user.name, user.last_name, user.user_name, user.password, user.mail, user.balance))
        self.baglanti.commit()

    def user_name(self, user_name):
        self.cursor.execute("Select * From Users where User_name= ?", (user_name,))
        user = self.cursor.fetchone()
        return user

    def user_mail(self, user_mail):
        self.cursor.execute("Select * From Users where mail= ?", (user_mail,))
        user = self.cursor.fetchone()
        return user

    def user(self, name):
        self.cursor.execute("Select * From Users where User_name = ? ", (name,))
        user = self.cursor.fetchone()
        user1 = User(name=user[0], last_name=user[1], user_name=user[2], password=user[3], mail=user[4],
                     balance=user[5], )
        return user1

    def new_user_login(self):

        name = input("Your name:")
        last_name = input("Your last name:")
        while True:
            user_name = input("Your user name:")
            user1 = Datum().user_name(user_name)
            if user1:
                print("Such a username already exists..")
            else:
                break
        while True:
            password = input("Your password must be at least 6 digits.\nYour password:")
            if 5 >= len(password):
                print("Your password is short")
            else:
                break
        while True:
            mail = input("Your mail:")
            user1 = Datum().user_mail(mail)
            if user1:
                print("Such a mail already exists..")
            else:
                break
        balance = input("Your balance:")
        new_user = User(name, last_name, user_name, password, mail, balance)
        Datum().user_login(new_user)
        time.sleep(2)
        Mail.Mail().user(new_user.user_name)
        time.sleep(2)
        print("Privilege welcome to shopping {} :)".format(new_user.name))

    def user_control(self):
        balance = 2
        while True:
            user_name = input("Your user name:")
            password = input("Your password:")
            self.cursor.execute("Select * From Users where user_name= ? and password = ?", (user_name, password))
            user = self.cursor.fetchone()
            if user:
                if user[2] == "admin":

                    return 1
                else:
                    user1 = User(name=user[0], last_name=user[1], user_name=user[2], password=user[3], mail=user[4],
                                 balance=user[5], )
                    return user1
            elif balance == 0:
                print("You have no more access rights...")
                time.sleep(2)
                break
            else:
                print("Password and username are incorrect...")
                balance -= 1

    def user_update(self,price,name):
        self.cursor.execute("UPDATE Users SET Balance = ? where User_name = ?", (price,name))
        self.baglanti.commit()