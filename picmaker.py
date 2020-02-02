import random

def main():
    color = "P3\n500 500\n255\n"
    for pixel in range(500):
        for x in range(500):
            if x <= 71:
                color += ('255 255 255 ')
            elif x <= 142:
                color += ('249 251 0 ')
            elif x <= 213:
                color += ('2 254 255 ')
            elif x <= 284:
                color += ('1 255 0 ')
            elif x <= 355:
                color += ('253 0 251 ')
            elif x <= 426:
                color += ('251 1 2 ')
            else:
                color += ('3 1 252 ')

    f = open("picmaker.ppm", "w+")
    f.write(color)
    f.close()

main()
