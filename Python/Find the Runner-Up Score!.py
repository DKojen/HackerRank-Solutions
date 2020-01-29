#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem 
#Find the runner-up score (n-number of score;arr-scores)
n = 5
arr = 2,3,6,6,5

scores = list(arr)[:n]
scores.sort(reverse=True)
print(scores)

x = max(scores)
while max(scores) == x:
    scores.remove(max(scores))

print(max(scores))
