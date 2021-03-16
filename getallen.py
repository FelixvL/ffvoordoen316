getallen = [3, 53, 21, 88, 21]    
print(getallen)
for test in range(500):
	teller = 0
	controle = 0
	for getal in getallen:
		if teller >= (len(getallen) - 1) :
			break
		if getallen[teller] > getallen[teller+1]:
			temp = getallen[teller]
			getallen[teller] = getallen[teller+1]
			getallen[teller+1] = temp
			controle = 1
		teller = teller + 1
	if controle == 0:
		break
print(getallen)	
