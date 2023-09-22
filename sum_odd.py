#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=int(input("raqamni kiriting: "))
#Create a variable "sum_odd" and assign it 0.
sum_odd=0
#Find the sum of the odd digits in the variable "var_int".
for n in range(4) :
    if var_int%2==1 :
        sum_odd+=var_int%10
    var_int=var_int//10
print (sum_odd)