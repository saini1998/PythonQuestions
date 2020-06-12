


# 2. Given n email addresses of different domains, please send an email to the first address(in alphabetical order) of each domain. Please assume a function sendmail() to send the emails.
# A sample email array is following {ghi@hotmail.com, def@yahoo.com, ghi@gmail.com, abc@channelier.com, abc@hotmail.com, def@hotmail.com, abc@gmail.com, abc@yahoo.com, def@channelier.com,jkl@hotmail.com, ghi@yahoo.com, def@gmail.com }

oldEmails = ["ghi@hotmail.com", "def@yahoo.com", "ghi@gmail.com", "abc@channelier.com", "abc@hotmail.com", "def@hotmail.com", "abc@gmail.com", "abc@yahoo.com", "def@channelier.com","jkl@hotmail.com", "ghi@yahoo.com", "def@gmail.com" 
]
newEmails = []
for x in oldEmails:
    i = x.find("@")
    index = i + 1
    em = x[index:]
    newEmails += [em] 
    
newEmails.sort()
for y in newEmails:
    for z in oldEmails:
        if y in z:
            print(z)
  
