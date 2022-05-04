#找出留言有good。
data = []
with open('reviews.txt','r') as reviews:
	for review in reviews:  
		data.append(review)
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print(len(good))
