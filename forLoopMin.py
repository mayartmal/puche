min_value = None
for number in [111, 22, 21, 3, 15]:
    if min_value is None:
        min_value = number
    if number < min_value:
        min_value = number
    print(number, ' ', min_value)
print("result is ", min_value)
