import numpy
import os

cubes = [
	'bau','cua','tom','ca','huou','ga'
	]

cubesNew = [
	'bau','cua','tom','ca','huou','ga'
	]

random.shuffle(cubesNew)
dealer = []
player = []

dealer.append(cubesNew[0])
dealer.append(cubesNew[1])
dealer.append(cubesNew[2])

def converChoice(index):
	return cubes[index]

def openBowl():
	listResult = []
	print('tren dia co: [{}]'.format(']['.join(dealer)))
	for item in player:
		for face in dealer:
			if(item==face):
				listResult.append(face)
	if len(listResult)>0 :
		print('Ban da thang duoc: {}'.format('-'.join(listResult)))
	else:
		print('Chuc ban may man lan sau!')


def selectFace():
	print('1.bau')
	print('2.cua')
	print('3.tom')
	print('4.ca')
	print('5.huou')
	print('6.ga')
	print('7.khong dat cuoc')
	choice = input('Ban muon dat cuoc cua nao? :')
	if(int(choice)>=7):
		openBowl()
		return True
	else:
		player.append(converChoice(int(choice)-1))
		return False

while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	if len(player)>0:
		print('Ban da dat cua: [{}]'.format(']['.join(player)))
		answer = input('Ban muon dat cuoc tiep khong?(y/n): ')
		if answer == 'y':
			if selectFace():
				break
		else:
			openBowl()
			break
	else:
		if selectFace():
			break
