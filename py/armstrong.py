num = input('Enter the number:')

temp = num
ans=0

while temp!=0:
	r = temp%10
	ans = ans+r*r*r
	temp = temp/10

if ans==num:
	print("Armstrong")
else:
	print("Not Armstrong")
