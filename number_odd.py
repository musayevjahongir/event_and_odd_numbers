#A four-digit integer is given. Find the number of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=int(input("raqamni kiriting: "))
#Print the number of odd digits in the variable "var_int".
k=0
for n in range(4) :
    if var_int%2==1 :
        k+=1
    var_int=var_int//10
print (k)