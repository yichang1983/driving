country = input('Where are you from: ')
age = input('How old are you: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You are allowed to take a driving test')
	else:
		print('You are NOT allowed to take a driving test')
elif country == 'USA':
	if age >= 16:
		print('You are allowed to take a driving test')
	else:
		print('You are NOT allowed to take a driving test')
else:
	print('You can only put Taiwan/USA')
	