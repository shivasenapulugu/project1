print("welcome to keka hotel:")
print("1.idly - 50:")
print("2.dosa - 100")
print("3.vada - 150")
print("4.puri - 120")
ch = int(input("enter your choice:"))
if ch >= 1 and ch <= 4:
   if ch == 1:
      item_name = "idly"
      cost = 50
   elif ch == 2:
      item_name = "dosa"
      cost = 100
      print("types of dosa")
      print("1.masala dosa - 50")
      print("2.egg dosa - 60")
      print("3.onion dosa - 50")
      print("4.double egg dosa - 100")
      ch = int(input("enter your choice:"))
      if ch >=1 and ch<=4:
         if ch == 1:
            item_name = "masala dosa"
            cost = 50
         elif ch == 2:
             item_name = "egg dosa"
             cost = 60
         elif ch == 3:
              item_name = "onion dosa"
              cost = 50
         else:
             item_name = "double agg dosa"
             cost = 100
   elif ch == 3:
        item_name = "vada"
        cost = 150
   elif ch == 4:
        item_name = "puri"
        cost = 120
   quantity = eval(input("enter your quantity:"))
   bill_amt = quantity*cost
   discount = eval(input("enter discount:"))
   discount_amt = bill_amt*discount/100
   final_bill = bill_amt-discount_amt
   paid_amt = eval(input("enter paid amount:"))
   balance = paid_amt-final_bill
   print("item name is:",item_name)
   print("cost is:",cost)
   print("quantity is:",quantity)
   print("bill amount is :",bill_amt)
   print("discount is:",discount)
   print("discount amount is:",discount_amt)
   print("final bill is:",final_bill)
   print("paid amount is:",paid_amt)
   print("balance is:",balance)
else:
    print("sorry...! no matching found")
