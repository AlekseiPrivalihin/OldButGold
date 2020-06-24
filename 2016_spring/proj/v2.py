import os, sys, pygame, math, random
from pygame.locals import *
pygame.init()

ko = [1 for i in range(102)]

border = 0.055
kk = 1.0025

def calc(i, j):
    ans = 0
    for x in range(max(0, j - 10), min(width, j + 11)):
        for y in range(max(0, i - 10), min(height, i + 11)):
            ans += (image[y][x] - border) * ko[abs(i - y) + abs(j - x)]
    ans /= (min(width, j + 11) - max(j - 10, 0)) * (min(height, i + 11) -  max(i - 10, 0))
    ans *= 2
    if ans > border:
        return ans
    else:
        return 0

def calc1(i, j):
    ans = 0
    border1 = border * 0.6
    for x in range(max(0, j - 10), min(width, j + 11)):
        for y in range(max(0, i - 10), min(height, i + 11)):
            ans += (image[y][x] - border1) * ko[abs(i - y) + abs(j - x)]
    ans /= (min(width, j + 11) - max(j - 10, 0)) * (min(height, i + 11) -  max(i - 10, 0))
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

get()
while 1:
    s = input().strip()
    if (s == "Q"):
        break
    elif (s == "L"):
        img = pygame.image.load('01.tif')
        width, height = img.get_size()
        s = pygame.image.tostring(img, "RGB")
        image = [[(s[i * 3 * width + 3 * j] + s[i * 3 * width + 3 * j + 1] + s[i * 3 * width + 3 * j + 2]) / (3 * 255) for j in range(width)] for i in range(height)]
        sz = width * height
        for i in range(200):
            x = random.randint(170, 420)
            y = random.randint(80, 330)
            learn(x, y, 1)
        for i in range(200):
            x = random.randint(940, 1100)
            y = random.randint(64, 254)
            learn(x, y, 1)
        for i in range(200):
            x = random.randint(734, 900)
            y = random.randint(768, 900)
            learn(x, y, 1)
        for i in range(200):
            x = random.randint(1150, 1320)
            y = random.randint(390, 580)
            learn(x, y, 0)
        for i in range(200):
            x = random.randint(525, 725)
            y = random.randint(90, 290)
            learn(x, y, 0)
        for i in range(200):
            x = random.randint(630, 690)
            y = random.randint(440, 540)
            learn(x, y, 0)
        print('done')
    elif (s == "G"):
        for root, dirs, files in os.walk(os.curdir):
            for file in files:
                if file.endswith(".tif"):
                    print(file)
                    img = pygame.image.load(file)
                    width, height = img.get_size()
                    s = pygame.image.tostring(img, "RGB")
                    image = [[(s[i * 3 * width + 3 * j] + s[i * 3 * width + 3 * j + 1] + s[i * 3 * width + 3 * j + 2]) / (3 * 255) for j in range(width)] for i in range(height)]
                    nimage = [[calc1(i, j)for j in range(width)]for i in range(height)]
                    image = nimage
                    print("halfway there...")
                    sz = width * height
                    q = 0
                    ns = list(s)
                    for i in range(height):
                        for j in range(width):
                            magic = min(1, calc(i, j))
                            if magic == 0:
                                ns[3 * q] = 255
                                ns[3 * q + 1] = 0
                                ns[3 * q + 2] = 0
                            else:
                                ns[3 * q] = int(255 * magic)
                                ns[3 * q + 1] = int(255 * magic)
                                ns[3 * q + 2] = int(255 * magic)
                            q += 1
                    ns = bytes(ns)
                    a = pygame.image.frombuffer(ns, (width, height), 'RGB')
                    pygame.image.save(a, file + '-mod.png')
                    print('done')
put()    

            
