import numpy as np
import math as m
import matplotlib.pyplot as plt
#from scipy.ndimage.filters import convolve


matrix = np.zeros((1000, 1000))



################################################

# add draw function here



# example drawing a square in the middle (from row 33 to row 67, column 33 to column 67)

#matrix[33:67, 33:67] = 1

#circle attempt 1

def make_crystal():
    arraysize =1000
    radius = 20
    dist = radius*4
    xpos = 200 - dist
    ypos = 200 - radius
    xpos1 = xpos
    ypos1 = ypos
    n1 = 8
    n2 = 8
    
    for i in range(n1):
        
        ypos1 = ypos

        xpos1 += dist
        
        if i % 2 == 0:
            ypos1 = ypos - dist/2
            n1 = n1+1
            
        else:
            ypos1 = ypos
            
        for j in range(n2):
            
            ypos1 +=dist
            
            x, y = np.mgrid[-xpos1:arraysize-xpos1, -ypos1:arraysize-ypos1]
            
            cir = x**2 + y**2 <= radius**2

            matrix[int(xpos):int(xpos1)+int(2*radius), int(ypos):int(ypos1)+int(2*radius)] = 1   
            matrix[cir] = 0   

    

     
    
    #xpos1 = xpos
    #ypos1 = ypos
    
    #for i in range(10):
    #    ypos1 += 50
    #    x, y = np.mgrid[-xpos1:arraysize-xpos1, -ypos1:arraysize-ypos1]
    #    cir = x**2 + y**2 <= radius**2
    #    matrix[cir] = 1
    #xpos2 = xpos+50
    #ypos2 = ypos+20
    #for i in range(10):
    #    ypos2 += 50
    #    x, y = np.mgrid[-xpos2:arraysize-xpos2, -ypos2:arraysize-ypos2]
    #    cir = x**2 + y**2 <= radius**2
    #    matrix[cir] = 1

    #xpos3 = xpos +100
    #ypos3 = ypos
    #for i in range(10):
    #    ypos3 += 50
    #    x, y = np.mgrid[-xpos3:arraysize-xpos3, -ypos3:arraysize-ypos3]
    #    cir = x**2 + y**2 <= radius**2
    #    matrix[cir] = 1
        
       
    
make_crystal()

################################################



def main():

    fig, ax = plt.subplots()

    image = ax.imshow(matrix, vmax=1, vmin=0, aspect='auto')

    ax.set_aspect('equal', 'box')

    ax.set_title('Drawing')



    plt.show()

main()
