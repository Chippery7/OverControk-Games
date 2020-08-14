from tkinter import *
import random
import time

tk = Tk()
jump_counter = 0
You_win = Label(tk, text="You win!")

class Ball:
    def __init__(self, canvas, jumps, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 0
        self.y = 9
        self.jumps = jumps
        self.win = False
        self.gravity = 0.1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Up>', self.turn_Up)
        self.canvas.bind_all('<KeyRelease-Up>', self.turn_Up_stop)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyRelease-Left>', self.turn_left_stop)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyRelease-Right>', self.turn_right_stop)


    def draw(self):
        global jump_counter
        paddle_pos = self.canvas.coords(self.paddle.id)
        paddle_p2s = self.canvas.coords(self.paddle.id2)
        paddle_p3s = self.canvas.coords(self.paddle.id3)
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        self.y += self.gravity
        # pos[0] = left side of the Ball
        # pos[2] = Right side of the ball
        if pos[1] <= 0: #Top of the Ball
            You_win.pack()
            self.win = True
            self.y = 3
        if pos[3] >= self.canvas_height: #Bottom of the Ball
            jump_counter = 0
            self.y = 0

        if pos[0] <= 0: # Left Side of the Ball
            self.x = 1

        if pos[2] >= self.canvas_width: # Right Side of the Ball
            self.x = -1


#--------------------------------Hit Collision--------------------------------#
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                jump_counter = 0
                self.y = 0

        if pos[2] >= paddle_p2s[0] and pos[0] <= paddle_p2s[2]:
            if pos[3] >= paddle_p2s[1] and pos[3] <= paddle_p2s[3]:
                jump_counter = 0
                self.y = 0

        if pos[2] >= paddle_p3s[0] and pos[0] <= paddle_p3s[2]:
            if pos[3] >= paddle_p3s[1] and pos[3] <= paddle_p3s[3]:
                jump_counter = 0
                self.y = 0

        if pos[2] <= paddle_pos[2] and pos[0] >= paddle_pos[0]:
            if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                self.y = 1

        if pos[2] <= paddle_p2s[2] and pos[0] >= paddle_p2s[0]:
           if pos[1] >= paddle_p2s[1] and pos[1] <= paddle_p2s[3]:
               self.y = 1

        if pos[2] <= paddle_p3s[2] and pos[0] >= paddle_p3s[0]:
           if pos[1] >= paddle_p3s[1] and pos[1] <= paddle_p3s[3]:
               self.y = 1
# If the top of the ball is greater than or equal too paddle's top and if the top of the ball is less than or equal too paddle's bottom

#--------------------------------Hit Collision: End--------------------------------#


    def turn_Up(self, evt):
        global jump_counter
        if jump_counter == self.jumps:
            print(jump_counter)
            self.y += self.gravity
        elif jump_counter != self.jumps:
            print('Jump', jump_counter)
            jump_counter = jump_counter + 1
            self.y = -4

    def turn_Up_stop(self, evt):
        self.y += self.gravity

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3

    def turn_left_stop(self, evt):
        self.x = self.x
        time.sleep(0.005)
        self.x = 0

    def turn_right_stop(self, evt):
        self.x = self.x
        time.sleep(0.005)
        self.x = 0

class Paddle:
    def __init__(self, canvas, color):
        pstartsX = [100, 300, 400]
        pstartsY = [125, 215, 300]
        random.shuffle(pstartsX)
        random.shuffle(pstartsY)
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.id2 = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.id3 = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, pstartsX[0], pstartsY[0])
        pstartsX.pop(0)
        pstartsY.pop(0)
        random.shuffle(pstartsX)
        random.shuffle(pstartsY)
        self.canvas.move(self.id2, pstartsX[0], pstartsY[0])
        pstartsX.pop(0)
        pstartsY.pop(0)
        random.shuffle(pstartsX)
        random.shuffle(pstartsY)
        self.canvas.move(self.id3, pstartsX[0], pstartsY[0])
        pstartsX.pop(0)
        pstartsY.pop(0)
        random.shuffle(pstartsX)
        random.shuffle(pstartsY)
        self.y = 0
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 1
        elif pos[2] >= self.canvas_width:
            self.x = -1



tk.title = ('Game')
tk.resizable(0, 0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, 3, paddle, 'green')



while 1:
    if ball.win == False:
        ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
