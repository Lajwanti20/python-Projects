#Project : Shopping Billing System

#Enter customer name
customerName = input("Enter a customer name: ")

#take 3 products with price as input from user

product1 = input("Enter product 1 : ")
priceProduct1 = float(input("Enter product 1 price :"))

product2 = input("Enter product 2 : ")
priceProduct2 = float(input("Enter product 3 price :"))

product3 = input("Enter product 3 : ")
priceProduct3 = float(input("Enter product 3 price :"))

#Add 3 products in a list and prices in a list
productList = []
productList.append(product1)
productList.append(product2)
productList.append(product3)

print("List of products : ",productList)

productPriceList = []
productPriceList.append(priceProduct1)
productPriceList.append(priceProduct2)
productPriceList.append(priceProduct3)

print("List of product price : ",productPriceList)

#Calculate total bill
totalBill = sum(productPriceList)
print("Total Bill : ",totalBill)

#discount
priceAfterDiscount = 0

if(totalBill > 5000) :
    priceAfterDiscount = totalBill - (totalBill * (10/100))
    print("Discount Rs.",(totalBill * (10/100)),"sss",priceAfterDiscount)
elif (totalBill >= 3000 or totalBill>=4999) :
     priceAfterDiscount = totalBill - (totalBill * (5/100))
     print("Discount Rs.",(totalBill * (5/100)))

     
#Ask about membership if membership is yes and amount is greater than 3000 then customer get 2% more discount.
membership = input("Do you have membership? ")

if(membership.lower() == "yes" and priceAfterDiscount > 3000) : 
       membershipDiscount =  (priceAfterDiscount * (2/100))
       print ("Extra Membership Discount: Rs.",membershipDiscount )
       priceAfterDiscount = priceAfterDiscount - membershipDiscount
       print ("Final Payable Amount: Rs.",priceAfterDiscount )
else :
      
       print ("Final Payable Amount: Rs.",priceAfterDiscount )