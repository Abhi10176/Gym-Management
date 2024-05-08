import mysql.connector as sql
fit=sql.connect(host="localhost" , user="root" , passwd="pass", database="fitness")
if fit.is_connected():
    print("Connected")
print("""
                                                        WELCOME TO ABHI FITNESS CENTRE
                                -------------------------------------------------------""")

mycursor=fit.cursor()
user=int(input("Enter your id: "))
passw=int(input("Enter your password: "))
c="INSERT INTO login(user_id, passwd) VALUES({},{})".format(user, passw)
mycursor.execute(c)
fit.commit()

while True:
    print("""
1. TO CREATE YOUR NEW ACCOUNT PRESS
2. TO LOGIN PRESS
3. TO EXIT PRESS
""")
    ch = int(input("enter your choice: "))
    if(ch==1):
        print("TO CREATE YOUR ACCOUNT PLEASE ENTER DETAILS")
        mycursor=fit.cursor()
        cid = int(input("Enter your id: "))
        passw=int(input("Enter your password: "))
        name=input("Enter your name: ")
        add=input("Enter your address: ")
        doj=input("Enter your date of joined: ")
        amt=int(input("Enter your paid amount: "))
        st="INSERT INTO main_table (user_id, passwd, user_name, user_address, date_of_joined, amt_paid)VALUES({}, {}, '{}', '{}','{}', {})".format(cid,passw,name,add,doj,amt)
        mycursor.execute(st)
        fit.commit()
        print('Account Created')
        print('Thank You')
    elif(ch==2):
        mycursor=fit.cursor()
        print("TO LOGIN ENTER YOUR  PASSWORD")
        passwd=int(input("Enter your password: "))
        mycursor.execute("select * from login")
        for i in mycursor:
            t_user,t_pas=i
        if t_pas==passwd:
            print("SUCCESSFULLY LOGIN!!!!!!!!")
            print('')
            print("Welcome to fitness centre")
            print('')
            print("""
   1. To see user details
   2. To update user details
   3. To see gym items
   4. To update new gym items
   5. To create gym items
   6. Go back
""")
            c=int(input("Enter your choice: "))
            # see user details
            if(c==1):
                mycursor=fit.cursor()
                mycursor.execute("select * from main_table")
                data=mycursor.fetchall()
                count=mycursor.rowcount
                print("Total custamer is:",count)
                for row in data:
                    print(row)
                # updating user details    
            elif(c==2):
                print("""
    To update user details please enter the followig detail................
""")

                mycursor=fit.cursor()
                passs=int(input("Update password: "))

                mycursor.execute("update main_table set passwd='"+str(passs)+"'")
                fit.commit()
                print('')
                uname=input("Update user name: ")

                mycursor.execute("update main_table set user_name='"+uname+"'")
                fit.commit()
                print('')
                uaddress=input("Update address of user: ")

                mycursor.execute("update main_table set user_address='"+uaddress+"'")
                fit.commit()
                print('')
                udoj=input("Update user joined data: ")
                mycursor.execute("update main_table set date_of_joined='"+udoj+"'")
                fit.commit()
                print('')
                amtp=int(input("Update paid amount: "))
                mycursor.execute("update main_table set amt_paid='"+str(amtp)+"'")
                fit.commit()
                print("costumer details succesully updated")
                # see jim items
            elif(c==3):
                mycursor=fit.cursor()
                mycursor.execute("select * from gym_items")
                data=mycursor.fetchall()
                count=mycursor.rowcount
                print("Total gym items is:",count)
                for row in data:
                    print(row)
            # updating jim items
            elif(c==4):
                mycursor=fit.cursor()
                oname=input("Update object name: ")
                mycursor.execute("update gym_items set object_name='"+oname+"'")
                fit.commit()
                print('')
                dop=input("Update date of purchase: ")
                mycursor.execute("update gym_items set date_of_parchase='"+dop+"'")
                fit.commit()
                print('')
                rd=input("Update repairing data: ")
                mycursor.execute("update gym_items set repairing_data='"+rd+"'")
                fit.commit()
                print('')
                tpu=input("Update total people using: ")
                mycursor.execute("update gym_items set total_people_using='"+tpu+"'")
                fit.commit()
                print("Gym items updated")
                # create jim items
            elif(c==5):
                print("TO CREATE GYM ITEMS PLEASE ENTER DETAILS ")
                mycursor=fit.cursor()
                oid= int(input("Enter your object id: "))
                oname=input("Enter your object name: ")
                dop=input("Enter your date of parchase: ")
                rd=input("Enter your repairing data: ")
                tpu=int(input("Enter your no. of pepole using: "))
                st="INSERT INTO gym_items(object_id, object_name, date_of_parchase, repairing_data, total_people_using)VALUES({}, '{}', '{}', '{}', {})".format(oid,oname,dop,rd,tpu)
                mycursor.execute(st)
                fit.commit()
                print("GYM ITEMS CREATED")
                print('Thank You')
            elif(c==6):
                break
            else:
                print("Invalid input........")
             
        else:
            print("Wrong Password......")

    elif(ch==3):
        break

    else:
        print("Something went wrong......")

