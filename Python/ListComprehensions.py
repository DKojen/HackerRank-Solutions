#Problem https://www.hackerrank.com/challenges/list-comprehensions/problem

#List Comprehension

if __name__ == '__main__':
    x, y, z, n = [1,1,1,2]
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1)
        for c in range(0,z+1) if a + b + c != n ])

  #(int(input()) for _ in range(4))
    #_ is used to signify that even though
    #something is being returned, we don't plan to use that variable any where.
