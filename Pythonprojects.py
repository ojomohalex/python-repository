"""
Your module description
"""

Services = [] #create empty list

Services.append("EC2") #Adding items to the list
Services.append("S3")
Services.append("Lamda")
Services.append("DYnamo DB")
Services.append("Cloud Watch")
Services.append("IAM")
Services.append("Cloud Formation")
Services.append("Cloud9")

print("Here are", len(Services), "examples of services in AWS", Services) #printing the list and stating how many items it contains

del Services[1:3]


print("Here are", len(Services), "examples of services in AWS", Services)
