attacks= 12 
clash= 4
reroll= False
rr6s= False
relentless= False
torrential= False
rr1s=False

defence = 3
cleave = 0
hardened = 0
evasion = 0
deadly = False
precice = False
defRR = False
rr6def = False
rr1def = False
shield = False
lineBreaker = False
smite = False
tenacious = False
bastion = 0

def defenseCheck():
	hits = hitsCheck()
	defProb = .166666 * defence
	wounds = hits - (hits * defProb)
	print("With a Defense of", defence, "you will average", int(wounds), "wounds!")

def hitsCheck():
	hitProb = .166666 * clash
	hits = attacks * hitProb
	# if reroll == True and rr6s == True:
	# 	print("You may not have rr6 and Reroll all dice, please choose one or the other")
	# 	return
	if reroll == True:
		rerolledHits = (attacks - hits) * hitProb
		hits += rerolledHits
	if rr6s == True and rr1s == False and reroll == False:
		rerolledHits = (attacks - hits) * .166666
		hits += rerolledHits
	if rr1s == True and rr6s == False and reroll == False:
		ones = hits * .166666
		hits -= ones
		rerolledHits = ones * (.166666 * clash)
		hits += rerolledHits
	if relentless == True:
		extraHits = hits * .166666
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


