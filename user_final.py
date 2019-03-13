import sqlite3

import re
import sys



from user1 import User
conn = sqlite3.connect('user_sec.db')

c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS user_sec(
            name text,phone integer)""")




def ins(user_name,phone_no):



    mat = "^((([a-zA-Z][’])?[a-zA-Z]+[\,]?\s*)?(([a-zA-Z][’])?[a-zA-Z]+[\-]?[a-zA-Z]*\s*)?[a-zA-z]*[\.]?)$"
    #pat = "^([a-zA-Z]['][a-zA-Z]*\s*[a-zA-Z]*\s*[a-zA-Z]*[.]?)"
    #cat = mat | pat
    if not re.match(mat,user_name):
        print("Invalid user name.Please try  again!")
        return


    #phone = "^(\d{5})|((\+?\d{1,3})?/s?([\(]\d{1,3}[\)])?/s?/-?(d{1,3})?/-?/s?d{4})|(\d{5}.\d{5})$"
    #phone = "^(\d{5})$|^(((\+?\d{1,3}?)?\s?([(]?\d{1,3}[)]?)?\s?\-?\d{1,3}?\-?\s?\d{4}?))$|^(\d{5}.\d{5})$"
   #phone = "^(\d{5})$|^(((\+?\d{1,3}?)?\s?([(]\d{1,3}[)])?\s?\-?\d{1,3}?\-?\s?\d{4}?))$|^(\d{5}.\d{5})$"
    phone_new = "^(\d{5})$|^((\+?\d{1,3}?)?\s?(\d)?\s?(([(]?\d{1,3}[)]?)?\s?\-?\d{1,3}?\-?\s?\d{4}?))$|^(\d{5}.\d{5})$"
    if not re.match(phone_new,phone_no):
        print("Invalid phone number .Please try  again!")
        return
    else:
        if (re.match("^(\+[0-9]{4})",phone_no)) or (re.match("^[0-9]{10}$",phone_no) or (re.match("^([(][0-9]{3}[)]\s([0-9]{3})\-[0-9]{4})$",phone_no)) or (re.match("^[0-9]{10}$",phone_no)) or  (re.match("^([\+][0-9]{2}\s[(][0-9]{3}[)]\s([0-9]{3})\-[0-9]{4})$",phone_no))):

            print("Invalid  phone number .Please try  again!")
            return
        else:
            user = User(user_name,phone_no)
            insert_user(user)




def insert_user(user):
    with conn:
        c.execute("insert into user_sec values (:name,:phone)",{'name':user.name,'phone':user.phone})
        #c.execute("insert into user_sec values ('name','phone') values (%s,%s)")

        print("The user record is inserted")



def select_user():
    with conn:
        c.execute("select * from user_sec")
        return c.fetchall()

def delete_user(user):
    with conn:
        c.execute("select * from user_sec where name= :name",{'name':user})
        result = c.fetchone()
        #print("user is",user)
        #print(result)
        if(result != None):
            c.execute("delete from user_sec where name= :name",{'name':user})
            print("Record deleted")
            return
        c.execute("select count(*) from user_sec where phone= :phone", {'phone': user})
        result1 = c.fetchone()
        if (result1 != None):
            c.execute("delete from user_sec where phone= :phone", {'phone': user})
            print("Record deleted")










def main():
    try:
        arg1 = sys.argv[1]
    except:
        print("please  give input in the format <functionname> <input1> <input2>")
        return
    if(arg1 == "ADD"):
         try:
             name = sys.argv[2]
             ph = sys.argv[3]
             ins(name, ph)
         except IndexError:
             print("please  give input in the format <functionname> <input1> <input2>")


    if(arg1 == "DEL"):
        try:
            user = sys.argv[2]

        except:
            print("please  give input in the format <functionname> <input1>")
            return
        delete_user(user)
    if(arg1 == "LIST"):
        list = select_user()
        print(list)






if __name__== "__main__":
  main()
