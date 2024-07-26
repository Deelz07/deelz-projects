text = input('Enter text to add commas to')

words = text.split()

res = ""

for word in words:
    res += f'{word},'

print(res[:-1])
