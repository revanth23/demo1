import add, subtract, multiplication, divide, modulus



print("<-- Mathematical Program -->\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
inp = int(input("Enter your choice->"))
if(inp==1):
	print(add.add())
elif(inp==2):
	print(subtract.subtract())
elif(inp==3):
	print(multiplication.multiply())
elif(inp==4):
	print(divide.div())
elif(inp==5):
	print(modulus.mod())
else:
	print("Invalid choice")