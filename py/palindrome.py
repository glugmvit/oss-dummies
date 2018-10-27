# function which checks whether a text is palindrom or not

def isPalindrome(s):  

	# Checking if both string are equal or not 
	if (s[::] == s[::-1]): 
		return True
	return False


# Driver code 
s = raw_input("Enter text:");
ans = isPalindrome(s) 

if ans == True: 
	print("Yes") 
else: 
	print("No") 
