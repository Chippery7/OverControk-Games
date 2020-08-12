from tkinter import *
import random
import time

tk = Tk()
jump_counter = 0

class Ball:
    def __init__(self, canvas, jumps, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 0
        self.y = 3
        self.jumps = jumps
        self.gravity = 0.1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Up>', self.turn_Up)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyRelease-Left>', self.turn_left_stop)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyRelease-Right>', self.turn_right_stop)

    def draw(self):
        global jump_counter
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        self.y += self.gravity
        if pos[1] <= 0: #Top of the Ball
            self.y = 3
        if pos[3] >= self.canvas_height: #Bottom of the Ball
            jump_counter = 0
            self.y = 0
        if pos[0] <= 0: # Left Side of the Ball
            self.x = 1
        if pos[2] >= self.canvas_width: # Right Side of the Ball
            self.x = -1


    def turn_Up(self, evt):
        global jump_counter
        if jump_counter == self.jumps:
            print(jump_counter)
            self.y = 0
        elif jump_counter != self.jumps:
            print(jump_counter, 'else')
            jump_counter = jump_counter + 1
            self.y = -4

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3

    def turn_left_stop(self, evt):
        self.x = 0

    def turn_right_stop(self, evt):
        self.x = 0




tk.title = ('Game')
tk.resizable(0, 0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness=0)
canvas.pack()
tk.update()

ball = Ball(canvas, 3, 'green')


while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
