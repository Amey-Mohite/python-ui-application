from db_connection import DatabaseConnection,createOrderTable
from action import listProduct,buyProduct,myBill

try:
    createOrderTable() #This will create table.
except:
    pass

#creating a product list 
product_list = [[1,500],[2,100],[3,400],[4,1000],[5,200],[6,700]]
product_dicts = {1:"Bread",
        2:"Butter",
        3:"Biscuit",
        4:"Sweets",
        5:"noodles",
        6:"cake"}
list_my_products = []

#inserting values into database table
with DatabaseConnection('Database.db') as connection:
    cursor = connection.cursor()
    for i in product_list:
        try:
            cursor.execute('INSERT INTO Product VALUES(?,?)', (i[0], i[1]))
        except:
            pass

# fetching values from the database table.
with DatabaseConnection('Database.db') as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Product')
    v = cursor.fetchall()

print()
print("*******Wayne SuperMarket Stores*******")
print()
user_name = input("Enter you Name : ")

while True:
    print("1. View List of Products")
    print("2. Buy Products")
    print("3. View My Bill")
    print("4. Exit")
    user_input = input(": ")

    if user_input == '1':
        listProduct(product_dicts,v)
    elif user_input == '2':
        list_my_products = buyProduct(list_my_products,product_dicts,v)
    elif user_input == '3':
        myBill(list_my_products,user_name)
    elif user_input == '4':
        break
    else:
        print("Unknown command : %s" % user_input)