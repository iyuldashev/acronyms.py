text_input = str(input("Enter a Phrase: "))
text = text_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)