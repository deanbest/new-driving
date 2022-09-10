country = input('哪國人呀: ')
age = input('小姐/先生 貴庚: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('來考照吧~')
	else:
		print('滿18再來喔~')