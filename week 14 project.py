"""
Your module description
"""

import random
	
company_ec2 = ['A154DH', 'A6793G', 'A1693H', 'A9240J', 'A1009D', 'F4983S','F2296C','F1778B',
	'F9021X', 'F1664A', 'M3527G', 'M1290Z', 'M1420M', 'M8376L', 'M0876T']  # Random EC2 List
	
ec2 = int(input("How many instance do you want: ")) #Allow the user to input how many EC2 instances they want names for and output the same amount of unique names
	
if ec2 == 0:
   print("Enter a value greater than 0")
elif ec2 == 1:
    print(random.choice(company_ec2))
elif ec2 == 2:
	    print(random.sample(company_ec2, 2))
elif ec2 == 3:
	    print(random.sample(company_ec2, 3))
elif ec2 == 4:
	    print(random.sample(company_ec2, 4))
elif ec2 == 5:
	    print(random.sample(company_ec2, 5))
elif ec2 == 6:
	    print(random.sample(company_ec2, 6))
elif ec2 == 7:
	    print(random.sample(company_ec2, 7))
elif ec2 == 8:
	    print(random.sample(company_ec2, 8))
elif ec2 == 9:
	    print(random.sample(company_ec2, 9))
elif ec2 == 10:
	    print(random.sample(company_ec2, 10))
elif ec2 == 11:
	    print(random.sample(company_ec2, 11))
elif ec2 == 12:
	    print(random.sample(company_ec2, 12))
elif ec2 == 13:
	    print(random.sample(company_ec2, 13))
elif ec2 == 14:
	    print(random.sample(company_ec2, 14))
elif ec2 == 15:
	    print(random.sample(company_ec2, 15))
	    
	    
	   
	
	
else:
	    print("ERROR")
	    

	    
	    
department = str(input("Enter your department name: ")) # allowing user to input department name

if department == "Marketing": #Allow the user to input the name of their department that is used in the unique name
	    print("EC2 that begins with 'M' is for your department")
elif department == "FinOps":
	    print("EC2 that starts with 'F' is for your department")
elif department == "Accounting":
	    print("EC2 that starts with 'A' is for your department")
	
else:
	    print("INVALID ENTRY, only departments with permission can use name generator.") #print a message that they should not use this Name Generator
