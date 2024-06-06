item1 = input("Enter the cost of the first item: $")
item2 = input("Enter the cost of the second item: $")
item3 = input("Enter the cost of the third item: $")
discount = "-"+input("Discount (write 0 if none): $")

print(f"""##################################
############# The Bill ###########
##################################
Item no ##  Description ### Cost
   1.       Chocolate       ${float(item1):.2f}
   2.       Pasta           ${float(item2):.2f}
   3.       Water           ${float(item3):.2f}
   Discount	         ${float(discount[1:]):.2f}
   Subtotal                 ${float(s):.2f}
----------------------------------
   Tax (15%)                ${s*.15:.2f}
----------------------------------
   Grand total              ${s*1.15:.2f}
----------------------------------
""")
