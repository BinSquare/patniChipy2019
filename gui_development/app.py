from tkinter import *
import tkinter as tk
from random import randint


#Concepts: Using tkinter as gui
# 1. Main loop -> tkinter is already in a infinite loop, don't use a while loop unless you're confident about what it's doing.
# 2. Canvas -> it's the actual gui, the rectangle where you can draw/paint/move stuff on. Think of it as a picture that we're drawing on.
# 3. Setting the background image -> we can pull that from fusion360 or whatother available resources
# 4. Animation -> everything on the canvas is dependent on coordinates of x and y. So set those before hand.


# initialize root Window and canvas
root = tk.Tk()
root.title("Balls")
root.resizable(False,False)

canvas = Canvas(root, width = 500, height = 500)
canvas.pack(expand = YES, fill = BOTH)

# sets the background image
backgroundImage = tk.PhotoImage(file="field.png")
canvas.create_image(0,0, image = backgroundImage, anchor = NW)

# Animate the ball moving
class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")

    def move_ball(self, deltax, deltay):
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(50, self.move_ball)

# create two ball objects and animate them
ball1 = Ball(canvas, 10, 10, 30, 30)
ball2 = Ball(canvas, 60, 60, 80, 80)

# animation
ball1.move_ball(1,1)
ball2.move_ball(2,2)

root.mainloop()
