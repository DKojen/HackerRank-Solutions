#https://www.hackerrank.com/challenges/finding-the-percentage/problem
#Finding the percentage

# * enables storage of multiple values

if __name__ == '__main__':
    n = int(input)
    student_marks = {}
    for _ in range(n):
        #line = James, 53, 46, 65
        line = input().split() #creating a list ['James','53','46','65']
        name, scores = line[0], line [1:] # name = ['James'] scores = ['53','46','65']
        scores = list(map(float,line[1:]))
        student_marks[name] = scores
        #creating a key with the name of the student and assingning
        #it to the value of the scores list in the 'student marks' dict
        #student_marks = {'James':['53','46','65']}
    query_name = input()
    query_scores = student_marks[query_name]
    print('%.2f'%(sum(query_scores)/(len(query_scores)))) #.2f round number on 2 decimals




