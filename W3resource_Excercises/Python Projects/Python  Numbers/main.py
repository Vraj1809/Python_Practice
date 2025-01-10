import random_profile as rp
num = int(input("Input number of random name/full name/profile: "))
name = rp.Name(num)
'''
name = rp.Name(num=1)
num = Total No. of Name You Want To Print
deafult is 1
To Print More Than one Name Change value of num
'''
print("For First Name: ")
name.first_name()

print("\nFor Full Name:")
name.full_name()

print("\nFor Full Profile:")
name.full_description()
