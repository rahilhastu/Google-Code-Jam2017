#! /bin/python

from sys import stdin

T = int(stdin.readline())

for t in range(T):
    [R, C] = [int(x) for x in stdin.readline().split()]
    cake = []
    for _ in range(R):
        cake.append([x for x in stdin.readline().strip()])
    #print 'cake = {}'.format(cake )
    firstLine = True
    for r in range(R):
        letterOnLine = '?'
        for c in range(C):
            l = cake[r][c]
           # print 'l = {}'.format(l)
            if l == '?':
                cake[r][c] = letterOnLine
    #            print 'cake = {}'.format(cake )
                continue

            if letterOnLine == '?':
                cake[r][:c] = [l]*c
            #    print 'cake = {}'.format(cake )
            cake[r][c] = l
            letterOnLine = l

        if letterOnLine == '?' and not firstLine:
            cake[r] = cake[r-1][:]
        elif firstLine and not letterOnLine == '?':
            for k in range(r):
                cake[k] = cake[r][:]
        if not letterOnLine == '?':
            firstLine = False


    print("Case #{}: ".format(t+1))
    for r in range(R):
        print("".join(cake[r]))
