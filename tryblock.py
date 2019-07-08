a_str = "Hello Bob"
try:
    i_str = int(a_str)
except:
    i_str = -1
print('First ', i_str)

a_str = "665"
try:
    i_str = int(a_str)
except:
    i_str = -1

print("Second ", i_str)

raw_sring = input("Please, input a positive number: ")
try:
    result  = int(raw_sring);
except:
    result = -1
if result >= 0:
    print("Nice work, result is " + str(result))
else:
    print("Bad input")
