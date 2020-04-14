print('What is your birthday month? Please put the number. Example: if your birthday is in March, put 3')
birthdayMonth = input()
print('What is your birthday date? Please put the number. Example: if your birthday is on the 25th, put 25')
birthdayDate = input()

if birthdayMonth == 3:
	if birthdayDate >= 21 and birthdayDate <= 31:
		print('You are an Aries!')
	if birthdayDate >= 1 and birthdayDate <= 20:
		print('You are a Pisces!')
if birthdayMonth == 4:
	if birthdayDate >= 1 and birthdayDate <= 18:
		print('You are an Aquarius!')
	if birthdayDate >= 19 and birthdayDate <= 30:
		print('You are an Aries!')
if birthdayMonth == 5:
	if birthdayDate >= 21 and birthdayDate <=31:
		print('You are a Gemini!')
	if birthdayDate >= 1 and birthdayDate <= 20:
		print('You are a Taurus!')
if birthdayMonth == 6:
	if birthdayDate >= 22 and birthdayDate <= 30:
		print('You are a Cancer!')
	if birthdayDate >= 1 and birthdayDate <=21:
		print('You are a Gemini!')
if birthdayMonth == 7:
	if birthdayDate >= 1 and birthdayDate <= 22:
		print('You are a Cancer!')
	if birthdayDate >= 23 and birthdayDate <= 31:
		print('You are a Leo!')
if birthdayMonth == 8:
	if birthdayDate >= 1 and birthdayDate <= 22:
		print('You are a Leo!')
	if birthdayDate >= 23 and birthdayDate <= 31:
		print('You are a Virgo!')
if birthdayMonth == 9:
	if birthdayDate >=1 and birthdayDate <= 22:
		print('You are a Virgo!')
	if birthdayDate >= 23 and birthdayDate <= 30:
		print('You are a Libra!')
if birthdayMonth == 10:
	if birthdayDate >= 1 and birthdayDate <= 23:
		print('You are a Libra!')
	if birthdayDate >= 24 and birthdayDate <= 31:
		print('You are a Scorpio!')
if birthdayMonth == 11:
	if birthdayDate >= 1 and birthdayDate <= 21:
		print('You are a Scorpio!')
	if birthdayDate >= 22 and birthdayDate <= 30:
		print('You are a Sagittarius!')
if birthdayMonth == 12:
	if birthdayDate >= 1 and birthdayDate <= 21:
		print('You are a Sagittarius!')
	if birthdayDate >= 22 and birthdayDate <= 31:
		print('You are a Capricorn!')
if birthdayMonth == 1:
	if birthdayDate >= 1 and birthdayDate <= 19:
		print('You are a Capricorn!')
	if birthdayDate >= 20 and birthdayDate <= 31:
		print('You are an Aquarius!')
if birthdayMonth == 2:
	if birthdayDate >= 1 and birthdayDate <= 18:
		print('You are an Aquarius!')
	if birthdayDate >= 19 and birthdayDate <= 29:
		print('You are a Pisces!')
