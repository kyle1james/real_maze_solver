# thank you https://stackoverflow.com/questions/12995434/representing-and-solving-a-maze-given-an-image?rq=1
# make sure maze is boxed with black outline. If not, just add that in whatever editor you please
import sys
from multiprocessing import Queue
# pillow
from PIL import Image



def a_star(start, end, matrix):

    parent = {}
    unseenNodes = [start]

    while unseenNodes:
        minNode = unseenNodes.pop(0)
        x,y = minNode

        if (x,y) == end:
            return parent

        px, py = x,y
        neighbors = ((x-1,y),(x,y-1),(x+1,y),(x,y+1))
        real_neighbors = ((x,y) for (x,y) in neighbors if matrix[x,y] > (120,120,120))

        for cx,cy in real_neighbors:
            matrix[cx,cy] = (120,120,120)
            unseenNodes.append((cx,cy))
            parent[(cx,cy)] = (px,py)


# run program
if __name__ == '__main__':
    # init values
    start = (10,7)
    end = (1768,1791)
    # invoke: python mazesolver.py <mazefile> <outputfile>[.jpg|.png|etc.]
    base_img = Image.open('maze_2.png')
    base_img = base_img.convert('RGB')
    base_pixels = base_img.load()
    # call search algorithm
    path = a_star(start, end, base_pixels)
    print('found path. Drawing Now')
    # open picture to print path on
    path_img = Image.open('maze_2.png')
    path_pixels = path_img.load()
    #reconstruct shortest path
    current_node = end
    while current_node != start:
        x,y = current_node
        path_pixels[x,y] = (255,0,0) # red
        current_node = path[current_node]
    # save image
    path_img.save('ans.jpg')
