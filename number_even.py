#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
int_var=1964
#Print the number of even digits in the variable "var_int".
x1=int_var%10
x2=int_var//10%10
x3=int_var//100%10
x4=int_var//1000
print(x1%2+x2%2+x3%2+x4%2)