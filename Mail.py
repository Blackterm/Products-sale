import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import sqlite3
import Users
import time

class Mail():

    def __init__(self):
        self.connection()

    def connection(self):
        self.baglanti = sqlite3.connect("market.db")
        self.cursor = self.baglanti.cursor()

    def user(self, name):
        self.cursor.execute("Select * From Users where Name = ? ", (name,))
        user = self.cursor.fetchone()
        user1 = Users.User(name=user[0], last_name=user[1], user_name=user[2], password=user[3], mail=user[4],
                     balance=user[5], )

        mesaj = MIMEMultipart()

        mesaj["From"] = "Sender's mail" #Sender's mail

        mesaj["To"] = user1.mail

        mesaj["Subject"] = "Welcome {}".format(user1.name)

        yazi = """
        Dear {};\nWelcome to privileged shopping. Thank you for choosing us.
        """.format(user1.name)

        mesaj_govdesi = MIMEText(yazi, "plain")

        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.gmail.com",
                                587)

            mail.ehlo()

            mail.starttls()

            mail.login("info.teknolojimarket@gmail.com",
                       "Muratcan_1997@")

            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            print("OKEY...")
            time.sleep(2)
            mail.close()

        except:
            sys.stderr.write(
                "EROR...")
            sys.stderr.flush()

    def password_control (self,):
       balance = 2
       while True:
            name = input("Your user name:")
            self.cursor.execute("Select * From Users where User_name = ? ", (name,))
            user = self.cursor.fetchone()

            if user:
                user1 = Users.User(name=user[0], last_name=user[1], user_name=user[2], password=user[3], mail=user[4],
                                   balance=user[5], )
                mesaj = MIMEMultipart()

                mesaj["From"] = "Sender's mail" #Sender's mail

                mesaj["To"] = user1.mail

                mesaj["Subject"] = "Your password info {}".format(user1.user_name)

                yazi = """
                Dear {};\nYour password:{}.
                """.format(user1.name,user1.password)

                mesaj_govdesi = MIMEText(yazi, "plain")

                mesaj.attach(mesaj_govdesi)

                try:
                    mail = smtplib.SMTP("smtp.gmail.com",
                                        587)

                    mail.ehlo()

                    mail.starttls()

                    mail.login("Sender's mail",
                               "Password")

                    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
                    print("OKEY...")
                    time.sleep(2)
                    mail.close()

                    break
                except:
                    sys.stderr.write(
                        "EROR..")
                    sys.stderr.flush()
            elif balance == 0:
                print("You do not have the right to enter")
                break
            else:
                print("There is no such user...")
                balance -= 1