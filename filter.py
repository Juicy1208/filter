#找出留言長度小於100
data = []
with open('reviews.txt','r') as reviews:
	for review in reviews:  #for字串in清單
		data.append(review) #把字串丟入data清單
small100 =[]
for d in data:
	if len(d)<100: #篩選字串長度小於100的字串
		small100.append(d) #長度小於100的存入small100清單
print(len(small100))

