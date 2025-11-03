#36
human = float(input('Say your age: '))

if human < 0:
	print('Wrong number! You have to say positive number')
else:
	if human <= 21:
		dog = human/10.5
	else:
		dog = 2+(human-21)/4

print(f'{dog:.1f} is dog\'s age ')

if dog < 2.0:
	print(f'{dog:.1f} меньше 2 лет ')
elif dog > 2.0:
	print(f'{dog:.1f} больше 2 лет')
else:
	print(f'{dog:.1f} ровно 2 года')