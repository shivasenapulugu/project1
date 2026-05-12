print("loan eligibility")
a_sal = eval(input("enter annual salary:"))
print("annual salary is:",a_sal)
m_sal = a_sal/12
print("monthly salary is:",m_sal)
if m_sal >= 25000:
   exp = eval(input("enter experience:"))
   if exp >= 2:
       print("1.education loan - 4.8")
       print("2.gold loan - 8.9")
       print("3.personal loan - 18.5")
       ch = int(input("enter your choice:"))
       if ch >=1 and ch<=3:
          if ch == 1:
             loan = "1.education loan"
             per = 4.8
          elif ch == 2:
             loan = "2.gold loan"
             per = 8.9
          else :
               loan = "3.personal loan"
               per = 18.5
          amount = eval(input("enter your amount:"))
          duration = int(input("enter duration:"))
          int_amt = amount*per*duration/100
          final_amt = amount+int_amt
          emi = final_amt/(12*duration)
          print("enter your choice is:",loan)
          print("rate of interest is:",per)
          print("enter amount is:",amount)
          print("duration is:",duration)
          print("interest amount is:",int_amt)
          print("final amount is:",final_amt)
          print("EMI is:",emi)
   else:
        print("sorry, your loan application rejected due to less exp")
else:
    print("sorry, your loan application rejected due to less salary")
