import secrets 
otp=' '.join([ secrets.randbelow(10)for num in range(6)])
print(otp)