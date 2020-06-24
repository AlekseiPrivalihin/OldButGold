import os, sys, pygame, math, random
from pygame.locals import *
pygame.init()
border = 0.055
for root, dirs, files in os.walk(os.curdir):
            for file in files:
                if file.endswith(".tif"):
                    print(file)
                    img = pygame.image.load(file)
                    img1 = pygame.image.load(file + '-mod.png')
                    width, height = img.get_size()
                    s = pygame.image.tostring(img, "RGB")
                    s1 = pygame.image.tostring(img1, "RGB")
                    ans = 0
                    num = 0
                    for i in range(len(s) // 3):
                        if (s1[3 * i + 2] > 0):
                            ans += (s[i * 3] + s[i * 3 + 1] + s[i * 3 + 2]) / (3 * 255)
                            num += 1
                    ans = ans / num
                    print('average: 255 * ' + str(ans) + ' in ' + str(num) + ' pixels')
