from colorthief import ColorThief
#import cv2
#import matplotlib.pyplot as plt
import json
def color(link):
 ct=ColorThief(link)
 dom_color=ct.get_color(quality=1)
 return(dom_color)
 
# dom_color=color('im1.jpeg')

# rgb_dict = {'r': dom_color[0], 'g': dom_color[1], 'b': dom_color[2]}
    

# json_output = json.dumps(rgb_dict)
# print(json_output)
# #plt.imshow([[dom_color]])
# #plt.show()
