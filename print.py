name = input('Name : ')

print(f'Hosgeldin {(name).capitalize()} ')

word = 'happyhacking'
can = 10;
indexler = []

dizi = ['-']*int(len(word))

while can>0:
	if '-' not in dizi:
		print('You won!')
		break;
	guess = input('Enter a Letter : ');
	if guess in word:
		for i in range(int(len(word))):
			if word[i] == guess:
				indexler.append(i)
		for i in indexler:
			if dizi[i] == '-':
				dizi[i] = guess
			else:
				continue
		print(dizi)

	else:
		can -=1






	
