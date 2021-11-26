import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, axs = plt.subplots()


def init():
    global_list = [
        #small
        {"x": [3, 3, 4, 4, 3], "y": [3, 4, 4, 3, 3]},
        #medium
        {"x": [3, 3, 5, 5, 3], "y": [3, 5, 5, 3, 3]},
        #large
        {"x": [3, 3, 7, 7, 3], "y": [3, 7, 7, 3, 3]}
        ]
    return global_list
    ## to return first dict first_dic = global_list[0:2]   list splitting

def animate(frame):

