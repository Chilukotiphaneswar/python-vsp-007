print(type(price)) #it returns the type of object
#type() is very very imp
print(type(age))
"""


#Identifiers --> names given to variables,functions,classes,objects,modules

@@ -86,13 +86,18 @@
discount = 0.15
final_price = price - (price * discount)
print(final_price)


"""
#Vijay went to hotel for dinner his bill is 2500,GST applicable is 5%
#hotel manager has given him 5% discount,how much Vijay has to pay?



price = 2500
gst = 0.05
discount = 0.05
#first apply discount
final_price = price - (price * discount)
#print(final_price)
final_price = final_price + (final_price * gst)
print(final_price)
