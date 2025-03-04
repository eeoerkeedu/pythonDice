d6 = .166666

attacks= 25 
clash= 4
reroll= False
rr6s= False
relentless= False
torrential= False
rr1s=False

defence = 2
cleave = 0
hardened = 0
evasion = 1
deadly = False
precice = False
defRR = False
rr6def = False
rr1def = True
shield = True
lineBreaker = False
smite = False
tenacious = 0
bastion = 0

def defenseCheck():
	hits = hitsCheck()
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
		defProb = d6 * evasion
		wounds = hits - (hits * defProb)
		print("With an Evasion of", evasion, "you will average", int(wounds), "wounds!")
		return wounds

	defProb = d6 * modifiedDefence
	wounds = hits - (hits * defProb)
	if defRR == True:
		rerolledSaves = wounds * defProb
		wounds -= rerolledSaves
	if rr6def == True and defRR == False and rr1def == False:
		sixes = wounds * d6
		wounds -= sixes
	if rr1def == True and defRR == False and rr6def == False:
		ones = wounds * d6
		wounds += ones

	print("With a Defense of", modifiedDefence, "you will average", int(wounds), "wounds!")
	return wounds

def hitsCheck():
	hitProb = d6 * clash
	hits = attacks * hitProb
	# if reroll == True and rr6s == True:
	# 	print("You may not have rr6 and Reroll all dice, please choose one or the other")
	# 	return
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

# hitsCheck()
defenseCheck()


