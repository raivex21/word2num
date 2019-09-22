## TODO:
#check the first word if less than 20.

lessThanTwenty = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
scale = ['hundred', 'thousand', 'million']


def islessThanTwenty(word):
	for x in lessThanTwenty:
		if word == x:
			return True
		else:
			return False



def wordToNumbers(string):
	string = string.lower()
	words = []
	words = string.replace('-', ' ').split()
	numbers = []

	#check if the 'and' exist in the list and remove it
	for x in words:
		if x == 'and':
			words.remove('and')
		else:
			continue


	for i in words:
		if words.index(i) == 0:
			if islessThanTwenty(i):
				for j in lessThanTwenty:
					if i == j:
						numbers.append(lessThanTwenty.index(j) + 1)





	return numbers


string = wordToNumbers('one and-two nineteen')

for x in string:
	print(x, end='')
