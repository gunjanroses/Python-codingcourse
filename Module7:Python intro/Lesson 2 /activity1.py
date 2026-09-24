snack_item ="pizza"
quantity = 40
price = 599.00
is_available = True

print(f"variable:snack_item, value:{snack_item}, data type :{type(snack_item)}")
print(f"Variable:quantity,Value:{quantity},data type:{type(quantity)}")
print(f"Variable:price,value:{price}, data type:{type(price)}")
print(f"VAriable: is_availabe, Value: {is_available}, data type: {type(is_available)}")

topping = None
print(type(topping))

total_bill = quantity * price 
print("Total bill:", total_bill)
print("sale price :",price - 100)
print(100/ 3)
# floor division
print(100//3)

#Exponentiation - power
print(3 ** 4)

# remainder - %
print(10%2)

print("Is the price below 200?", price<200)
print("More than 10 in stock?" ,quantity>10)
print("Price is exactly 1.5?", price==1.5)

print(1=="1")

shop_name= "quick"+ " " + "bites"
print(shop_name)
shop_name = f"Quick Bites ({snack_item} available here)"
print(shop_name)

print(len(shop_name))
print(shop_name[0:11])
s="Roll No:59"
print(s[8:10])
print(s[-2:])

a=7
b=10
temp=a
a=b
b=temp
print(a)
print(b)