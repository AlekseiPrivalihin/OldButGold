import os, sys, pygame, math, random
from pygame.locals import *
pygame.init()

ko = [1 for i in range(102)]

border = 0.055
kk = 1.0025

def calc(i, j):
    ans = 0
    for x in range(max(0, j - 50), min(width, j + 51)):
        for y in range(max(0, i - 50), min(height, i + 51)):
            ans += (image[y][x] - border) * ko[abs(i - y) + abs(j - x)]
    ans /= (min(width, j + 51) - max(j - 50, 0)) * (min(height, i + 51) -  max(i - 50, 0))
    ans *= 2
    if ans > border:
        return ans
    else:
        return 0

def calc1(i, j):
    ans = 0
    border1 = border * 0.6
    for x in range(max(0, j - 50), min(width, j + 51)):
        for y in range(max(0, i - 50), min(height, i + 51)):
            ans += (image[y][x] - border1) * ko[abs(i - y) + abs(j - x)]
    ans /= (min(width, j + 51) - max(j - 50, 0)) * (min(height, i + 51) -  max(i - 50, 0))
    ans *= 2
    if ans > border1:
        return image[i][j]
    else:
        return 0

def learn(j, i, correct):
    aaa = calc(i, j)
    if (aaa > 0):
        aaa = 1
    if (aaa > correct):
        for x in range(max(0, j - 50), min(width + 1, j + 51)):
            for y in range(max(0, i - 50), min(height + 1, i + 51)):
                if image[y][x] < border:
                    ko[abs(i - y) + abs(j - x)] *= kk
                else:
                    ko[abs(i - y) + abs(j - x)] /= kk
    elif aaa < correct:
        for x in range(max(0, j - 50), min(width, j + 51)):
            for y in range(max(0, i - 50), min(height, i + 51)):
                if image[y][x] < border:
                    ko[abs(i - y) + abs(j - x)] /= kk
                else:
                    ko[abs(i - y) + abs(j - x)] *= kk
        
def get():
    infile = open("koef.txt", "r")
    ko = list(map(float, infile.readline().split()))
    infile.close()

def put():
    outfile = open("koef.txt", "w")
    for i in ko:
        outfile.write(str(i) + ' ')
    outfile.write('\n')
    outfile.close()            
