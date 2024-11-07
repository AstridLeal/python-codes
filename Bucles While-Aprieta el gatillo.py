score=100
a=0
while a<=3:
	i=input()
	if(i=="hit"):
		score=score+10
	if(i=="miss"):
		score=score-20
	a=a+1
print(score)