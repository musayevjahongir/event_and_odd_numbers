#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=int(input("raqamni kiriting: "))
#Create a variable "sum_even" and assign it 0.
sum_even=0
#Find the sum of the even digits in the variable "var_int".
for n in range(4) :
    if var_int%2==0 :
        sum_even+=var_int%10
    var_int=var_int//10
print (sum_even)