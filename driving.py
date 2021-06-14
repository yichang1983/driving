country = input('Where are you from: ')
age = input('How old are you: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You are allow to take a driving test')
	else:
		print('You are NOT allow to take a driving test')
