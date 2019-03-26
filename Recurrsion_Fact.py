def fact(n):
	if n==0:
		print(n)
		return 1
	else:
		return n*fact(n-1)
#num=int(input("Enter value for factorial :"))
num=995
print("Factorial" + str(num) + " is " + str(fact(num)))