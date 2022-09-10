country = input('哪國人呀: ')
age = input('小姐/先生 貴庚: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('來考照吧~')
	else:
		print('滿18再來喔~')
elif country == '美國':
	if age >= 16:
		print('歡迎來考照~')
	else:
		print('滿16再來好嗎~')
else:
	print('請輸入台灣或美國')