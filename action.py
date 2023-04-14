
def listProduct(product_dicts,v): # To list the products
    print("---------------------------------")
    print("List of Products")
    print("ID|Name|Price")
    for i in range(len(v)):
        print(v[i][0],product_dicts[i+1],v[i][1])
    print("---------------------------------")

def buyProduct(list_my_products,product_dicts,v):
    try:
        id1 = int(input("Select Product by ID : "))
        qty = int(input("Enter the Quantity : "))
        name = product_dicts[id1] #getting name of the product using dictionary
        v_dict = dict(v)
        price = v_dict[id1] * qty # calculating price
        list_my_products.append([id1,name,qty,price])
        return list_my_products
    except:
        print("Exception")
        return list_my_products

def myBill(list_my_products,user_name):
    if len(list_my_products) == 0:
        print("Please add products to the cart")
    else:
        total_price = 0
        dis_total_price = 0
        f = 0
        for i in list_my_products:
            total_price += i[3]
        if total_price>=4000: # if total price greater than 4000 then discount of 10%
            dis = (total_price*10)/100
            dis_total_price = (total_price*90)/100
            line = "You got 10% discount"
            f = 1 
        print("---------------------------------")
        print("Bill:")
        if f == 1:
            print(line)
        print("ID|Name|Quantity|Total Price")
        for i in list_my_products:
            print(i[0],i[1],i[2],i[3])
        print("Total Amount : ",total_price)
        if f == 1:
            print("Discount : ", dis)
            print("Discounted Amount To be paid: ",dis_total_price) 
            
        print("---------------------------------")
        with open(user_name+"_Bill.txt", 'w') as file: # Saving the bill in the txt file.
            for row in list_my_products:
                s = " ".join(map(str, row))
                file.write(s+'\n')
            file.write("Total Amount : "+str(total_price)+'\n')
            if f == 1:
                file.write("Discount : "+str(dis)+'\n')
                file.write("Discounted Amount To be paid : "+str(dis_total_price)) 