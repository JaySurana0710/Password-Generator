from random import randint,sample
import time

password=chr(randint(65,90))
password+=chr(randint(65,90))
password+=str(randint(0,9))
password+=str(randint(0,9))
password+=chr(randint(97,122))
password+=chr(randint(97,122))
password+=chr(64)


finalpass=''.join(sample(password,len(password)))

print(finalpass)
time.sleep(10)
