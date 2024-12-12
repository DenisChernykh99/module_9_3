
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (
    len(x[0]) - len(x[1]) for x in zip(first, second) if len(x[0]) != len(x[1])
)

second_result = (
    len(f) == len(s) for i in range(min(len(first), len(second))) for f, s in [(first[i], second[i])]
)

print(list(first_result))
print(list(second_result))
