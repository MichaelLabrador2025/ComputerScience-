
#declaring Variables, Variables are lables for code/ thing assigned to it
#examples
age = 17 #local Variable
name = "Michael" #Local variable 
Birth_day = 9 # Global variable
Birth_Month = "November" # Global Variable
Birth_year = 2006 # Global Variable 
#Local Variables only matter in thier block while Global affect the other ones
Brith_date = (Birth_Month, Birth_day, Birth_year)
print (name, age)
print  (Brith_date)

#inputs 
name = str(input("enter your name:"))
age = int(input("enter your age:"))
Birth_day = int(input("enter your Birth Day:"))
Birth_date = str(input("enter your Birth Date:"))
Birth_year = int(input("enter your Birth year:"))

print(name, age, Birth_date, Birth_day, Birth_year)
