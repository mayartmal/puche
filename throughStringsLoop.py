test_string = 'SLOVO'

for word in test_string:
    print(word)

index = 0
while index < len(test_string):
    print(test_string[index])
    index = index + 1


word = 'blabaaaaaaaaaaaaaaaaaaaaaaaaalabla'
interst_letter = 'a'
letter_counter = 0
for letter in word:
    if letter == interst_letter:
        letter_counter = letter_counter + 1
print(letter_counter)
