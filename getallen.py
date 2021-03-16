getallen = [3, 53, 21, 88, 21]    
#			0   1   2   3   4
print("test")
rondjecontrolle = 0
print(getallen)
for test in range(500):
	teller = 0
	print("=================")
	controle = 0
	rondjecontrolle += 1
	for getal in getallen:
		if teller >= (len(getallen) - 1) :
			break
		print(getallen[teller])
		print(getallen[teller+1])
		if getallen[teller] > getallen[teller+1]:
			temp = getallen[teller]
			getallen[teller] = getallen[teller+1]
			getallen[teller+1] = temp
			controle = 1
		else:
			print("andere")
		teller = teller + 1
		print(getallen)
	if controle == 0:
		break
print(getallen)	
print(rondjecontrolle)