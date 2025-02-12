import numpy as np
from PIL import Image
import math
import random

# code is written by erich priemer
# used code from this link : https://towardsdatascience.com/creating-fractals-in-python-a502e5fc2094/

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def bresenham(x0, y0, x1, y1):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).

    Input coordinates should be integers.

    The result will contain both the start and the end point.
    """
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy

#xy1 / xy2 is tuple with x,y cords
def draw_line(xy1,xy2,pixels,color):
    points = bresenham(xy1[0],xy1[1],xy2[0],xy2[1])

    for cords in points:
        if (0 <= cords[0] and cords[0] < 500# x in bounds
            and 0 <= cords[1] and cords[1] < 500# y in bounds
            ):

            pixels[cords[1]][cords[0]] = color

def draw_square(center, side_length, pixels, color):
    top_right_cords = (center[0]-round(side_length/2),center[1]-round(side_length/2))
    top_left_cords = (center[0]+round(side_length/2),center[1]-round(side_length/2))
    bottom_right_cords = (center[0]-round(side_length/2),center[1]+round(side_length/2))
    bottom_left_cords = (center[0]+round(side_length/2),center[1]+round(side_length/2))
    
    draw_line(top_left_cords,top_right_cords,pixels,color)
    draw_line(bottom_left_cords,bottom_right_cords,pixels,color)
    draw_line(top_left_cords,bottom_left_cords,pixels,color)
    draw_line(top_right_cords,bottom_right_cords,pixels,color)

    
def draw_square_fractal(center, side_lenth, depth, pixels, color, origin):
    if (depth == 0):
        return
    else:
        draw_square(center,side_lenth,pixels,color)

        plusX = round(center[0]+side_lenth/1.333333)
        minusX = round(center[0]-side_lenth/1.333333)

        plusY = round(center[1]+side_lenth/1.333333)
        minusY = round(center[1]-side_lenth/1.333333)

        r=color[0]-40
        g=color[1]-10
        b=color[2]-20

        if (r < 0):
            r = 0
        if (g < 0):
            g = 0
        if (b < 0):
            b = 0

        new_color = (r,g,b)
        
        #top right square
        #if(origin != "bottomleft"):
        draw_square_fractal((plusX,minusY),side_lenth//2, depth-1,pixels,new_color,"topright")

        #top left square
        #if(origin != "bottomright"):
        draw_square_fractal((minusX,minusY),side_lenth//2, depth-1,pixels,new_color,"topleft")

        #bottom right square
        #if(origin != "topleft"):
        draw_square_fractal((plusX,plusY),side_lenth//2, depth-1,pixels,new_color,"bottomright")

        #bottom left square
        #if(origin != "topright"):
        draw_square_fractal((minusX,plusY),side_lenth//2, depth-1,pixels,new_color,"bottomleft")


__name__ == "__main__"

    

center = (249,249)
color = (255, 255, 255)




for x in range(1,10):
        # Define the size of our image
    pixels = np.zeros( (500, 500,3), dtype=np.uint8 )
        #draw fractal 
    draw_square_fractal(center,150,x,pixels,color,None)
        # Turn our pixel array into a real picture
    img = Image.fromarray(pixels)
        # save the image
    img.save(f'half-square-fractal-{x}.png')
    



