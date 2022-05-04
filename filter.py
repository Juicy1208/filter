#找出留言長度小於100
data = []
with open('reviews.txt','r') as reviews:
	for review in reviews:  
		data.append(review)
small100 =[]
for d in data:
	if len(d)<100:
		small100.append(d)
print(len(small100))

