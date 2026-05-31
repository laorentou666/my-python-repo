scores = [1,3,4,2,5,7,6,8]
scores.sort()
valid_scores = scores[1:-1]
avg = sum(valid_scores) / len(valid_scores)
print(avg)