# Welcome Note
print("Howdy, I'm Prabindh")
# Defining  The Function
def simple_interest(P,T,R): 
	print('The Principal Is', P,'Currencies') 
	print('The Time Duration Is', T,'Years') 
	print('The Rate Of Interest Is',R,'%') 
# Entering Through The Formula	
	SI = (P * T * R)/100
# Printing & Returning The Simple Interest	
	print('The Simple Interest Is', SI,'Currencies') 
	return SI
# Recieving The Data From The User
P=float(input("Enter The Principle : "))
T=float(input("Enter The Time Duration : "))
R=float(input("Enter The Rate Of Interest : "))
# Finding Out The Simpl Interest
simple_interest(P,T,R)