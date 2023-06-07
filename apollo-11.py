list = [1]

for n in list:
	print(f"This is the {n} element")
	n = n + 1
	if n > 10:
		break
	else:
		list.append(n)
