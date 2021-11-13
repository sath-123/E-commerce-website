import subprocess as sp
import pymysql
import pymysql.cursors 
from tabulate import tabulate


#view options

def viewTable(rows):

    a = []
    try:
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")   
        return
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    print(tabulate(a, tablefmt="psql", headers="firstrow"))
    print()
    return
def viewoption():
    print("Choose a VIEW option\n\n")
    print("1.  Orders")
    print("2.  PRODUCT")
    print("3.  SUPPLIER")
    print("4.  Shipper")
    print("5.  cards")
    print("6.  ord_details")
    print("7.  payment")
    print("8.  phone_no")
    print("9.  review")
    print("10. users")
    print("11. AVALIABLESIZES")
    
    print("\n")
    n = input("enter any thing to continue: ")

    if n == '1':
        query = "SELECT * FROM Orders;"
    elif n == '2':
        query = "SELECT * FROM PRODUCT;"
    elif n == '3':
        query = "SELECT * FROM SUPPLIER;"
    elif n == '4':
        query = "SELECT * FROM Shipper;"
    elif n == '5':
        query = "SELECT * FROM cards;"
    elif n == '6':
        query = "SELECT * FROM ord_details;"
    elif n == '7':
        query = "SELECT * FROM payment;"
    elif n == '8':
        query = "SELECT * FROM phone_no;"
    elif n == '9':
        query = "SELECT * FROM review;"
    elif n == '10':
        query = "SELECT * FROM users;"
    elif n == '11':
        query = "SELECT * FROM AVALIABLESIZES;"
    else:
      print("invalid options\n")
      return
    try:
        no_of_rows = cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    rows = cur.fetchall()
    viewTable(rows)
    #for x in rows:
        #print(x)

   
# addition part
def Addition_Options():
    print("Choose an Addition Option:\n")
    print("1. Add User")#user+cards+phonenum
    print("2. Add Product") #product+availablesizes
    print("3. Add Supplier")
    print("4. Add a new card for User")
    print("5. New Order") #order+details
    print("6. Add review")

    n= int(input("Enter option number: "))
    if n ==1 :
        addUser()
    elif n==2:
        add_product()
    elif n==3:
        addsupplier()
    elif n==4:
        addcards()
    elif n==5:
        add_order()
    elif n==6:
        add_review()
    else:
      print("invalid options\n")
      return
      
def addUser():
    row={}
    print("Enter new user details: ")
    row["user_id"]=int(input("User_Id: "))
    row["user_name"]=input("User_name: ")
    row["Email_id"]=input("Email_id: ")
    row["password"]=input("Password: ")
    row["Gender"]=input("Gender: ")
    row["Age"]=int(input("Age: "))
    row["line1"]=input("Address: line1 > ")
    row["line2"]=input("line2: ")
    row["district"]=input("district: ")
    row["city"]=input("city: ")
    row["state"]=input("state: ")
    row["country"]=input("country: ")
    row["pincode"]=int(input("pincode: "))
    phnos=[]
    print("how many phone numbers do you wish to save?:\n")
    t=int(input())
    for i in range(t):
        phnos.append(int(input("Enter Phone_number: ")))

    ch=input("do you wish to add your cards info?\nif yes: y| else n: ")
    if ch=='y':
        row["card_No"]=(input("Card_Number: "))
        row["card_type"]= input("Card_type: ")
        row["Expiry_month"]=int(input("Expiry month: "))
        row["Expiry_year"]=int(input("Expiry year:"))


    # print(row["Age"])
    try:
        query="insert into users values('%d', '%s', '%s', '%s', '%s', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%d')"%(row["user_id"],row["user_name"],row["Email_id"],row["password"],row["Gender"],row["Age"],row["line1"],row["line2"],row["district"],row["city"],row["state"],row["country"],row["pincode"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("try with different data\n")
        return
    
    try:
        for i in range(t):
            query1= "insert into phone_no values('%d','%d')"%(row["user_id"],phnos[i])
            cur.execute(query1)
            con.commit()
    except Exception as e:
        print(e)
        print("error while inserting phone numbers")
        return

    try:
        if ch=='y':
            query2="insert into cards values('%d', '%s', '%s','%d','%d')"%(row["user_id"],row["card_No"],row["card_type"],row["Expiry_month"],row["Expiry_year"])
            cur.execute(query2)
            con.commit()
    except Exception as e:
        print(e)
        print("error in data related to cards\n")
        return
    print("data added to database")


    
def add_product():
    row={}
    print("Enter details of a product to be added: \n")
    row["productcode"]=input("productcode: ")
    row["color"]=input("color: ")
    row["name"]=input("Name of product: ")
    row["stock"]=int(input("stock(in integer): "))
    row["description"]=input("description: ")
    row["productavailability"]=(input("productavailability: "))
    row["original price"]=int(input("original price: "))
    row["no_of_products_sold_out"]=int(input("no_of_products_sold_out: "))
    row["brandname"]=input("brandname: ")
    row["discount"]=int(input("discount(in integer): "))
    row["sellerID"]=input("sellerID: ")
    row["companyname"]=input("companyname: ")
    row["Address"]=(input("Address: "))
    sizes=[]
    print("How many sizes are available?:")
    t=int(input())
    for i in range(t):
        sizes.append(int(input("Size: ")))

    try:
        query="insert into PRODUCT values('%s','%s','%s','%d','%s','%s','%d','%d','%s','%d','%s','%s','%s')"%(row["productcode"],row["color"],row["name"],row["stock"],row["description"], row["productavailability"],
         row["original price"],row["no_of_products_sold_out"],row["brandname"],row["discount"],row["sellerID"],row["companyname"],row["Address"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("try with different data\n")
        return

    try:
        for i in range(t):
            queryf="insert into AVAILABLESIZES values('%d','%s)"%(row["productcode"],sizes[i])
            cur.execute(query)
            con.commit()
    except Exception as e:
        print(e)
        print("error in sizes available")
        return
        
def addsupplier():
    row={}
    print("Enter new supplier details: ")
    row["sellerID"]=input("Seller_ID: ")
    row["Name"]=input("Name of the company: ")
    row["line1"]=input("Address>\nline1: ")
    row["line2"]=input("line2: ")
    row["district"]=input("district: ")
    row["city"]=input("city: ")
    row["state"]=input("state: ")
    row["country"]=input("country: ")
    row["pincode"]=int(input("pincode: "))
    
    try:
        query="insert into SUPPLIER values('%s', '%s', '%s', '%s', '%s',  '%s', '%s', '%s', '%d')"%(row["sellerID"],row["Name"],row["line1"],row["line2"],row["district"],row["city"],row["state"],row["country"],row["pincode"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("try with different data\n")
        return
    print("data added to database")

def addcards():
    row={}
    print("Enter new card details: ")
    row["user_id"]=int(input("USERID: "))
    row["card_No"]=input("Card Number: ")
    row["card_type"]=input("Card type: ")
    row["Expiry_month"]=int(input("Expiry month: "))
    row["Expiry_year"]=int(input("Expiry year: "))
    
    
    try:
        query="insert into cards values('%d', '%s', '%s', '%d', '%d')"%(row["user_id"],row["card_No"],row["card_type"],row["Expiry_month"],row["Expiry_year"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("try with different data\n")
        return
    print("data added to database")
    
def add_order():
    row={}
    print("Enter new order details: ")
    row["orderid"]=int(input("orderid: "))
    row["shipperid"]=int(input("shipperid: "))
    row["t_ime"]=input("date of delivery: ")
    row["s_tatus"]=input("status of delivery: ")
    row["d_ate"]=input("booked date: ")
    row["customer_ID"]=int(input("userID: "))
    
    
    # print(row["Age"])
    try:
        query="insert into Orders values('%d', '%d', '%s', '%s', '%s')"%(row["orderid"],row["shipperid"],row["t_ime"],row["s_tatus"],row["d_ate"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("try with different data\n")
        return
       
    print("How many products do u want to buy?:")
    t=int(input())
    for i in range(t):
         row["Product_code"]=int(input("product_code: "))
         row["Quantity"]=int(input("Quantity: "))
         row["size"]=input("size: ")
         try:
              query="insert into ord_details values('%d', '%d', '%d', '%d', '%s')"%(row["customer_ID"],row["orderid"],row["Product_code"],row["Quantity"],row["size"])
              cur.execute(query)
              con.commit()
         except Exception as e:
              print(e)
              print("try with different data\n")
              return
         print("product added into orderdetails")
    print("jjj")
    
    
def add_review():
    row={}
    print("Enter new review details: ")
    row["Rating"]=int(input("Rating: "))
    row["Quality"]=int(input("Quality: "))
    row["fitness"]=int(input("fitness: "))
    row["transparency"]=int(input("transparency: "))
    row["text"]=input("text: ")
    row["product_code"]=int(input("product_code: "))
    row["user_id"]=int(input("user_id: "))
   
    
    # print(row["Age"])
    try:
        query="insert into review values('%d', '%d', '%d', '%d', '%s', '%d', '%d')"%(row["Rating"],row["Quality"],row["fitness"],row["transparency"],row["text"],row["product_code"],row["user_id"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("try with different data\n")
        return
    print("data added to databs")




#deleteoptions
def deletion():
    print("Choose a deletion Option:\n")
    print("1. User")#user+cards+phonenum
    print("2. Product") #product+availablesizes
    print("3. Order")

    n= int(input("Enter option number: "))
    if n ==1 :
        delete_User()
    elif n==2:
        delete_product()
    elif n==3:
        delete_order()
    else:
        print("invalid option\n")

def delete_User():
    id=int(input("Enter UserId which needs to be deleted:"))
    try:
        query="delete from users where user_id=%d"%(id)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("error in deleteing user")
        return

def delete_product():
    c=int(input("Enter product code which needs to be deleted: "))
    try:
        query="delete from PRODUCT where productcode=%d"%(c)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("Error in deleting product")
        return

def delete_order():
    oid=int(input("Enter order Id which needs to be deleted: "))
    try:
        query="delete from Orders where orderid=%d"%(oid)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("Error in deleting order")
        return 
        
#modify options
def update():
    print("Choose a update Option:\n")
    print("1. User's password")#user+cards+phonenum
    print("2. User's Address")
    print("3. Product availability") #product+availablesizes
    print("4. discount on a product")
    print("5. Number of products sold out")
    print("6. delivery status")

    n= int(input("Enter option number: "))
    if n ==1 :
        update_password()
    elif n==2:
        update_Address()
    elif n==3:
        product_availability()
    elif n==4:
        update_discount()
    elif n==5:
        update_num_of_pdts_sold()
    elif n==6:
        update_delivery()
    else:
        print("invalid option\n")     
        
def update_password():
    uid=int(input("Enter UserID whose password needs to be changed"))
    n_pass=input("Enter new password: ")
    try:
        query="update users set password='%s' where user_id='%d'"%(n_pass,uid)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("unable to update password")
        return

def update_Address():
    uid=int(input("Enter UserID whose address needs to be changed"))
    row={}
    row["line1"]=input("Enter line1: ")
    row["line2"]=input("Enter line2: ")
    row["district"]=input("Enter district: ")
    row["city"]=input("Enter city: ")
    row["state"]=input("Enter state: ")
    row["country"]=input("Enrer country: ")
    row["pincode"]=int(input("Enrer pincode: "))
    try:
        query="update users set line1='%s',line2='%s',district='%s',city='%s',state='%s',country='%s',pincode='%d' where user_id=%d"%(row["line1"],row["line2"],row["district"],row["city"],row["state"],row["country"],row["pincode"],uid)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("unable to update address")
        return

def product_availability():
    pc=int(input("Enter product code whose availabilty needs to be updated: "))
    avail=input("Enter availability of product (available/not available): ")
    try:
        query="update PRODUCT set productavailability='%s' where productcode='%d'"%(avail,pc)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("unable to update product availability")
        return
        
def update_delivery():
    oid=int(input("Enter orderid whose delivery status needs to be updated: "))
    st=input("Enter status of delivery (delivered/not delivered): ")
    try:
        query="update Orders set s_tatus='%s' where orderid='%d'"%(st,oid)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("couldn't update delivery status\n")
        return

def update_discount():
    pc=int(input("Enter product code whose discount needs to be updated: "))
    d=int(input("Enter discount (in integer): "))
    try:
        query="update PRODUCT set discount='%d' where productcode=%d"%(d,pc)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("couldn't update discount")
        return

def  update_num_of_pdts_sold():
    pc=int(input("Enter product code whose number of products sold out needs to be updated: "))
    nps=int(input("Enter number of products sold: "))
    try:
        query="update PRODUCT set no_of_products_sold_out=%d where productcode=%d"%(nps,pc)
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("couldnt update number of products sold out")
        return    


# sort
def sort():  
    print("Choose an option based on which you want sort products:\n")
    print("1.OriginalPrice-highest to lowest")
    print("2.OriginalPrice-lowest to highest ")
    print("3.Discount")
    print("4.Stock")
    n= int(input("Enter option number: "))
    if n ==1 :
       query="SELECT * FROM PRODUCT ORDER BY original_price DESC;"
    elif n==2:
       query="SELECT * FROM PRODUCT ORDER BY original_price ASC;" 
    elif n==3:
       query="SELECT * FROM PRODUCT ORDER BY discount DESC;"
    elif n==4:
       query="SELECT * FROM PRODUCT ORDER BY stock DESC;"
    else:
       print("invalid option\n")
       return
    try:
        print(query)
        cur.execute(query)
        rows=cur.fetchall()
        viewTable(rows)
    except Exception as e:
            print(e)
    return      


#filter
def Filter():  
    print("Choose an option based on which you want filter products:\n")
    print("1.colour")
    print("2.price")
    print("3.brandname")
    n= int(input("Enter option number: "))
    if n ==1 :
        print("Select colour:\n")
        print("1.red")
        print("2.blue")
        print("3.green")
        print("4.white")
        print("5.pink")
        print("6.black")
        print("7.yellow")
        print("8.brown")
        m= int(input("Enter option number: "))
        if m==1:
           query="SELECT * FROM PRODUCT WHERE colour='red';"
        elif m==2:
           query="SELECT * FROM PRODUCT WHERE colour='blue';"
        elif m==3:
           query="SELECT * FROM PRODUCT WHERE colour='green';"
        elif m==4:
           query="SELECT * FROM PRODUCT WHERE colour='white';"
        elif m==5:
           query="SELECT * FROM PRODUCT WHERE colour='pink';"
        elif m==6:
           query="SELECT * FROM PRODUCT WHERE colour='black';"
        elif m==7:
           query="SELECT * FROM PRODUCT WHERE colour='yellow';"
        elif m==8:
           query="SELECT * FROM PRODUCT WHERE colour='brown';"
    elif n==2:
        print("Select originalprice range:\n")
        print("1.<500")
        print("2.500-1000")
        print("3.1000-2000")
        print("4.2000-5000")
        print("5.5000-10000")
        print("6.>=10000")
        m= int(input("Enter option number: "))
        if m==1:
           query="SELECT * FROM PRODUCT WHERE original_price<500 ;"
        elif m==2:
           query="SELECT * FROM PRODUCT WHERE original_price>=500 AND original_price<1000;"
        elif m==3:
           query="SELECT * FROM PRODUCT WHERE original_price>=1000 AND original_price<2000;"
        elif m==4:
           query="SELECT * FROM PRODUCT WHERE original_price>=2000 AND original_price<5000;"     
        elif m==5:
           query="SELECT * FROM PRODUCT WHERE original_price>=5000 AND original_price<=9999;"
        elif m==6:
           query="SELECT * FROM PRODUCT WHERE original_price>9999;"      
    elif n==3:
        print("Select brand name:\n")
        print("1.LIBAS")
        print("2.GERUA")
        print("3.INDO ERA")
        print("4.ISHIN")
        m= int(input("Enter option number: "))
        if m==1:
          query="SELECT * FROM PRODUCT WHERE brandname='LIBAS';"
        elif m==2:
          query="SELECT * FROM PRODUCT WHERE brandname='GERUA';"
        elif m==3:
          query="SELECT * FROM PRODUCT WHERE brandname='INDO ERA';"
        elif m==4:
          query="SELECT * FROM PRODUCT WHERE brandname='ISHIN';"
    else:
       print("invalidoptions\n")
       return
    try:
        print(query)
        cur.execute(query)
        rows=cur.fetchall()
        viewTable(rows)
    except Exception as e:
            print(e)
    return  
    
#selection
def selectbybrand():
    brandname=input("enter brand name: ")
    try :
        query="SELECT * FROM PRODUCT WHERE brandname='%s';" % (brandname)
        cur.execute(query)
    except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
    x=cur.fetchall() 
    viewTable(x) 
    con.commit()
    
    
def selectbygender():
    brandname=input("M/F: ")
    try :
        query="SELECT * FROM users WHERE Gender='%s';" % (brandname)
        cur.execute(query)
    except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
    x=cur.fetchall() 
    viewTable(x)  
    con.commit()
  
#project   
def listoutbyage():
    age=int(input("enter age of users: "))
    try :
        query="SELECT user_name,Gender FROM users WHERE Age>'%d';" % (age)
        cur.execute(query)
    except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
    x=cur.fetchall() 
    viewTable(x)
    con.commit()
    

def listoutbyprice():
    price=int(input("enter price of products: "))
    try :
        query="SELECT name,(original_price-original_price*discount*0.01) as Price FROM PRODUCT WHERE (original_price-original_price*discount*0.01)>='%d';" % (price)
        cur.execute(query)
    except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
    x=cur.fetchall() 
    viewTable(x) 
    con.commit()
     

#partialmatch
def searchproduct():
    price=input("enter products by names: ")
    try :
        query="SELECT * FROM PRODUCT WHERE INSTR(name,'%s')>0;" % (price)
        cur.execute(query)
    except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
    x=cur.fetchall() 
    viewTable(x)  
    con.commit()    
    
#analysis

def avgRating():
    product=int(input("Enter product_code:"))
    print("Choose an option based on which you want average rating:\n")
    print("1. TotalRating")
    print("2. Quality")
    print("3. Fitness")
    print("4. Transparency")
    n= int(input("Enter option number: "))
    if n ==1 :
        try:
            query="SELECT avg(Rating) from review where product_code='%s';"% (product)
            cur.execute(query)
            rows=cur.fetchall()
            viewTable(rows)
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    elif n==2:
         try:
            query="SELECT avg(Quality) from review where product_code='%s';"% (product)
            cur.execute(query)
            rows=cur.fetchall()
            viewTable(rows)
         except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
         return
    elif n==3:
          try:
            query="SELECT avg(fitness) from review where product_code='%s';"% (product)
            cur.execute(query)
            rows=cur.fetchall()
            viewTable(rows)
          except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
          return
    elif n==4:
         try:
            query="SELECT avg(transparency) from review where product_code='%s'"% (product)
            cur.execute(query)
            rows=cur.fetchall()
            viewTable(rows)
         except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
         return
    else:
      print("invalid options\n")
      return
           
def total10prod():
     try:
          query="SELECT product_code,COUNT(*) as no_of_10_stars from review WHERE Rating=10 GROUP BY product_code;"
          cur.execute(query)
          rows=cur.fetchall()
          viewTable(rows)
     except Exception as e:
          print(e)
          print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
     return

        
#analysis   
def orderbyshipper():
      cname=input("Enter company name of shipper:")
      try:
          query="SELECT orderid,shipperid,t_ime as time,s_tatus,d_ate as date from Orders inner join Shipper on Orders.shipperid=Shipper.shipper_id where company_name='%s';"%(cname)
          cur.execute(query)
          rows=cur.fetchall()
          viewTable(rows)
               
      except Exception as e:
          print(e)
          print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
      return
          

        
def brandhighavgpro():
     try:
          query="SELECT brandname,avg(Rating),product_code from PRODUCT inner join review on PRODUCT.productcode=review.Product_code GROUP BY product_code ORDER BY avg(Rating) DESC LIMIT 1;"
          cur.execute(query)
          rows=cur.fetchall()
          for x in rows:
               print(x)
     except Exception as e:
          print(e)
          print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
     return

def totalprice():
     user=int(input("Enter user id:"))
     order=int(input("Enter order id:"))
     try:
          query="SELECT SUM(tprice) as total_price from(SELECT original_price*Quantity as tprice from ord_details inner join PRODUCT on ord_details.product_code=PRODUCT.productcode WHERE customer_ID=%d AND orderid=%d)as C;"%(user,order)
          cur.execute(query)
          rows=cur.fetchall()
          for x in rows:
               print(x)
     except Exception as e:
          print(e)
          print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
     return

#----  
def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        viewoption()
    elif(ch == 2):
        Addition_Options()
    elif(ch == 3):
        deletion()
    elif(ch == 4):
        update()
    elif(ch == 5) :
        sort()
    elif(ch == 6):
        Filter()
    elif(ch == 7):
        selectbybrand()
    elif(ch == 8):
        selectbygender()
    elif(ch == 9):
        listoutbyage()
    elif(ch == 10):
        listoutbyprice()
    elif(ch == 11):
        searchproduct()
    elif(ch == 12):
        avgRating()
    elif(ch == 13):
        total10prod()
    elif(ch == 14):
        orderbyshipper()
    elif(ch == 15):
        brandhighavgpro()
    elif(ch == 16):
         totalprice()
    else:
        print("Error: Invalid Option")
        
        
  
  # GLOBAL
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user='root',
                              password='Spr@1438',
                              db='checking',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                print("1. View")  
                print("2. Addition") 
                print("3. Deletion")  
                print("4. Modify")  
                print("5. Sort")
                print("6. Filter")
                print("7. Retreive all products of a particular brand")
                print("8. Retreive all users of particulargender ")
                print("9. Project name and gender of users above particular age")
                print("10.Project name,price of products above particular price")
                print("11.Partial match by productname")
                print("12.Avg rating of product")
                print("13.Total 10 stars given to product")
                print("14.select orders by shippername")
                print("15.Brand with highest avg rating for one of its products")
                print("16.Total price in an order")
                print("0. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 0:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
