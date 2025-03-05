# standard d6 distirbution assumption
d6 = .166666

# offensive modifiers
attacks= 25 
clash = 4
reroll = False
rr6s = False
relentless = False
torrential = False
rr1s = False

# Defnesive modifiers
defence = 2
cleave = 0
hardened = 0
evasion = 1
deadly = False
precice = False
defRR = False
rr6def = False
rr1def = False
shield = True
lineBreaker = False
smite = False
tenacious = 1
bastion = 0

def defenseCheck():
	hits = hitsCheck()
	wounds = 0
	evasionChecker = False
	modifiedDefence = defence
	if shield == True and lineBreaker == False:
		modifiedDefence += 1
	if bastion > 0 and lineBreaker == False:
		modifiedDefence += bastion
	if hardened > 0 or cleave > 0:
		cvh = cleave - hardened
		if cvh < 0: cvh = 0
		modifiedDefence -= cvh
	if evasion > modifiedDefence or smite == True:
		evasionChecker = True
		modifiedDefence = evasion

	if precice == True:
		ones = hits * d6
		saves = ones * (evasion * d6)
		wounds += ones - saves
		hits -= ones

	defProb = d6 * modifiedDefence
	missedSaves = hits - (hits * defProb)
	if defRR == True:
		rerolledSaves = missedSaves * defProb
		missedSaves -= rerolledSaves
	if rr6def == True and defRR == False and rr1def == False:
		sixes = missedSaves * d6
		missedSaves -= sixes
	if rr1def == True and defRR == False and rr6def == False:
		ones = missedSaves * d6
		missedSaves += ones
	if deadly == True:
		sixes = missedSaves * d6
		sixes -= tenacious
		wounds += sixes
	if tenacious > 0:
		missedSaves -= tenacious
	
	wounds += missedSaves

	if evasionChecker == True:
		print("With an Evasion of", evasion, "you will average", int(wounds), "wounds!")
	else:
		print("With a Defense of", modifiedDefence, "you will average", int(wounds), "wounds!")
	return wounds

def hitsCheck():
	hitProb = d6 * clash
	hits = attacks * hitProb
	if reroll == True:
		rerolledHits = (attacks - hits) * hitProb
		hits += rerolledHits
	if rr6s == True and rr1s == False and reroll == False:
		rerolledHits = (attacks - hits) * d6
		hits += rerolledHits
	if rr1s == True and rr6s == False and reroll == False:
		ones = hits * d6
		hits -= ones
		rerolledHits = ones * (d6 * clash)
		hits += rerolledHits
	if relentless == True:
		extraHits = hits * d6
		hits += extraHits
	if torrential == True:
		extraHits = hits * .5
		hits += extraHits
	
	print("With a Clash of", clash, "and", attacks, "attacks, you will average", int(hits), "hits!")
	return hits

attackDict = {"hits": 12, "clash":4, "reroll": False, "rr6s": False, "relentless": False, "torrential": False, "rr1s":False}
defenseDict = {"defence": 2, "cleave": 0, "hardened": 0, "evasion": 1, "deadly": False, "precice": False, "defRR": False, "rr6def": False, "rr1def": False, "shield": False, "lineBreaker": False, "smite": False, "tenacious": False, "bastion": False}

defenseCheck()


