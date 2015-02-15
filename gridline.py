# Author: Filip Bartek (filip.bartek@hotmail.com)

# This script presents dynamic patterns in a small rectangular grid.
# Observe the patterns and try to identify the direction of movement of each pattern.
# Try to only consider the four basic directions (up, down, left, right).
# The presentation ends when a key is pressed.

# Based on: http://www.psychopy.org/coder/tutorial1.html


from psychopy import visual, core, event
import random


# Configuration:
# Dimensions of the grid in elements
n_x = 3
n_y = 3

# Dimensions of the elements in degrees of visual angle
width=0.5
height=0.5

lineColor = [0,0,0] # Color of the element boundaries

delayFrame = 1.0 / 8 # Delay after each frame
delaySequence = 1 # Delay after each full sequence

seed = 0 # Initial randomness seed


def in_phase(i_x, i_y, phase, dir, n_x, n_y):
    if dir[0] == 1:
        x = n_x - 1 - i_x
    else:
        x = i_x
    if dir[1] == 1:
        y = n_y - 1 - i_y
    else:
        y = i_y
    
    return x + y == phase

def random_dir(rnd):
    return (rnd.choice([0,1]), rnd.choice([0,1]))

rnd = random.Random(seed)

mywin = visual.Window(monitor='testMonitor', units='deg', rgb=[-1,-1,-1], fullscr=True)

frames = []

for i_x in range(n_x):
    frames.append([])
    x = (- n_x / 2 + i_x) * width + width/2
    for i_y in range(n_y):
        y = (- n_y / 2 + i_y) * height + height/2
        pos = (x, y)
        frames[i_x].append(visual.Rect(mywin, width=width, height=height, pos=pos, lineColor=lineColor, autoDraw=True))

phase = 0
dir = random_dir(rnd)

mywin.flip()
core.wait(delaySequence)

while True:
    if len(event.getKeys()) > 0:
        break
    event.clearEvents()
    
    for i_x in range(n_x):
        for i_y in range(n_y):
            if in_phase(i_x, i_y, phase, dir, n_x, n_y):
                frames[i_x][i_y].fillColor = [1,1,1]
            else:
                frames[i_x][i_y].fillColor = [-1,-1,-1]
    mywin.flip()
    
    core.wait(delayFrame)
    
    phase += 1
    if phase > n_x + n_y:
        phase = 0
        dir = random_dir(rnd)
        core.wait(delaySequence)

mywin.close()
core.quit()