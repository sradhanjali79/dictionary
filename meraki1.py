# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1) 
print('welcome to SBl bank')
print('insert your card')
Total=10000
language=input('select language')
if language=="english" or language=="hindi":
	pin=5555
	pin=int(input('enter pin'))
	if pin==5555:
		print('transaction')
		transaction=int(input('select transaction 1.withdraw 2.deposit 3.total'))
		if transaction==1:
			withdraw=int(input('enter amount'))
			total=Total-withdraw
			print('balance is:',total)
		elif transaction==2:
			deposit=int(input('enter amount'))
			balance=Total+deposit
			print('balance is:',balance)
		elif transaction==3:
			print('balance is:',balance)
		else:
			print('quite')
	else:
		print('incorrect pin')
else:
	print('incorrect language')
