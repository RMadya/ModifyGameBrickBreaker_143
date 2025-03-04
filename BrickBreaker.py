import tkinter as tk
from tkinter import colorchooser

class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)


class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.radius = 10
        self.direction = [1, -1]
        self.speed = 10  # Default speed
        self.base_speed = 10  # Store base speed for speed multiplier
        item = canvas.create_oval(x-self.radius, y-self.radius, 
                                   x+self.radius, y+self.radius, 
                                   fill='white')
        super(Ball, self).__init__(canvas, item)

    def update(self):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] <= 0 or coords[2] >= width:
            self.direction[0] *= -1
        if coords[1] <= 0:
            self.direction[1] *= -1
        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed
        self.move(x, y)

    def set_speed_multiplier(self, multiplier):
        self.speed = self.base_speed * multiplier

    def collide(self, game_objects):
        coords = self.get_position()
        x = (coords[0] + coords[2]) * 0.5
        if len(game_objects) > 1:
            self.direction[1] *= -1
        elif len(game_objects) == 1:
            game_object = game_objects[0]
            coords = game_object.get_position()
            if x > coords[2]:
                self.direction[0] = 1
            elif x < coords[0]:
                self.direction[0] = -1
            else:
                self.direction[1] *= -1

        for game_object in game_objects:
            if isinstance(game_object, Brick):
                game_object.hit()


class Paddle(GameObject):
    def __init__(self, canvas, x, y):
        self.width = 80
        self.height = 10
        self.ball = None
        self.base_speed = 10  # Base movement speed
        self.speed = self.base_speed  # Current speed
        item = canvas.create_rectangle(x - self.width / 2,
                                       y - self.height / 2,
                                       x + self.width / 2,
                                       y + self.height / 2,
                                       fill='yellow')
        super(Paddle, self).__init__(canvas, item)

    def set_ball(self, ball):
        self.ball = ball

    def set_speed_multiplier(self, multiplier):
        self.speed = self.base_speed * multiplier

    def move(self, direction):
        offset = direction * self.speed
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super(Paddle, self).move(offset, 0)
            if self.ball is not None:
                self.ball.move(offset, 0)


class Brick(GameObject):
    COLORS = {1: '#e74c3c', 2: '#3498db', 3: '#222222'}

    def __init__(self, canvas, x, y, hits):
        self.width = 75
        self.height = 20
        self.hits = hits

 
import tkinter as tk
from tkinter import colorchooser

class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)


class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.radius = 10
        self.direction = [1, -1]
        self.speed = 10  # Default speed
        self.base_speed = 10  # Store base speed for speed multiplier
        item = canvas.create_oval(x-self.radius, y-self.radius, 
                                   x+self.radius, y+self.radius, 
                                   fill='Gold')
        super(Ball, self).__init__(canvas, item)

    def update(self):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] <= 0 or coords[2] >= width:
            self.direction[0] *= -1
        if coords[1] <= 0:
            self.direction[1] *= -1
        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed
        self.move(x, y)

    def set_speed_multiplier(self, multiplier):
        self.speed = self.base_speed * multiplier

    def collide(self, game_objects):
        coords = self.get_position()
        x = (coords[0] + coords[2]) * 0.5
        if len(game_objects) > 1:
            self.direction[1] *= -1
        elif len(game_objects) == 1:
            game_object = game_objects[0]
            coords = game_object.get_position()
            if x > coords[2]:
                self.direction[0] = 1
            elif x < coords[0]:
                self.direction[0] = -1
            else:
                self.direction[1] *= -1

        for game_object in game_objects:
            if isinstance(game_object, Brick):
                game_object.hit()


class Paddle(GameObject):
    def __init__(self, canvas, x, y):
        self.width = 80
        self.height = 10
        self.ball = None
        self.base_speed = 10  # Base movement speed
        self.speed = self.base_speed  # Current speed
        item = canvas.create_rectangle(x - self.width / 2,
                                       y - self.height / 2,
                                       x + self.width / 2,
                                       y + self.height / 2,
                                       fill='Red')
        super(Paddle, self).__init__(canvas, item)

    def set_ball(self, ball):
        self.ball = ball

    def set_speed_multiplier(self, multiplier):
        self.speed = self.base_speed * multiplier

    def move(self, direction):
        offset = direction * self.speed
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super(Paddle, self).move(offset, 0)
            if self.ball is not None:
                self.ball.move(offset, 0)


class Brick(GameObject):
    COLORS = {1: 'White', 2: 'Black', 3: 'Gold'}

    def __init__(self, canvas, x, y, hits):
        self.width = 75
        self.height = 20
        self.hits = hits
        color = Brick.COLORS[hits]
        item = canvas.create_rectangle(x - self.width / 2,
                                       y - self.height / 2,
                                       x + self.width / 2,
                                       y + self.height / 2,
                                       fill=color, tags='brick')
        super(Brick, self).__init__(canvas, item)

    def hit(self):
        self.hits -= 1
        if self.hits == 0:
            self.delete()
        else:
            self.canvas.itemconfig(self.item,
                                   fill=Brick.COLORS[self.hits])


class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.current_speed = 1.0
        self.current_bg_color = '#ffc0cb'  # Default background color
        self.is_paused = False  # Track the pause state
        
        # Create control frame
        self.control_frame = tk.Frame(self)
        self.control_frame.pack(side='top', fill='x')
        
        # Create speed control buttons
        self.create_speed_controls()
        
        # Create color picker button
        self.create_color_picker()
        
        # Create canvas
        self.canvas = tk.Canvas(self, bg=self.current_bg_color,
                                width=self.width,
                                height=self.height)
        self.canvas.pack()
        self.pack()

        self.items = {}
        self.ball = None
        self.paddle = Paddle(self.canvas, self.width/2, 326)
        self.items[self.paddle.item] = self.paddle
        
        # Create speed label
        self.speed_label = tk.Label(self.control_frame, 
                                     text=f"Speed: {self.current_speed}x",
                                     font=('Consolas', 12))
        self.speed_label.pack(side='left', padx=5)
        
        for x in range(5, self.width - 5, 75):
            self.add_brick(x + 37.5, 50, 2)
            self.add_brick(x + 37.5, 70, 1)
            self.add_brick(x + 37.5, 90, 1)

        self.hud = None
        self.setup_game()
        self.canvas.focus_set()
        
        self.canvas.bind('<Left>', lambda _: self.paddle.move(-1))
        self.canvas.bind('<Right>', lambda _: self.paddle.move(1))
        self.canvas.bind('<p>', lambda _: self.toggle_pause())  # Bind pause key

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.canvas.create_text(300, 200, text='Paused', font=('Consolas', 40), tags='pause_text')
        else:
            self.canvas.delete('pause_text')
            self.game_loop()  # Resume the game loop

    def create_color_picker(self):
        # Create a separator frame
        separator = tk.Frame(self.control_frame, width=2, bd=1, relief='sunken')
        separator.pack(side='left', padx=5, fill='y')
        
        # Create color picker button
        color_btn = tk.Button(self.control_frame,
                              text="Change Background",
                              command=self.choose_color)
        color_btn.pack(side='left', padx=5)

    def choose_color(self):
        # Open color picker dialog
        color = colorchooser.askcolor(title="Choose Background Color", 
                                      color=self.current_bg_color)
        if color[1]:  # If a color was chosen (not cancelled)
            self.current_bg_color = color[1]
            self.canvas.configure(bg=self.current_bg_color)

    def create_speed_controls(self):
        speeds = [
            ("C", 0.25),
            ("B", 0.5),
            ("A", 1.0),
            ("S", 1.5),
            ("SS", 5.0)
        ]
        
        for text, speed in speeds:
            btn = tk.Button(self.control_frame,
                            text=text,
                            command=lambda s=speed: self.set_game_speed(s))
            btn.pack(side='left', padx=5)

    def set_game_speed(self, speed_multiplier):
        self.current_speed = speed_multiplier
        if self.ball is not None:
            self.ball.set_speed_multiplier(speed_multiplier)
        if self.paddle is not None:
            self.paddle.set_speed_multiplier(speed_multiplier)
        self.speed_label.config(text=f"Speed: {speed_multiplier}x")

    def setup_game(self):
        self.add_ball()
        self.update_lives_text()
        self.text = self.draw_text(300, 200,
                                   'Press space to start')
        self.canvas.bind('<space>', lambda _: self.start_game())

    def add_ball(self):
        if self.ball is not None:
            self.ball.delete()
        paddle_coords = self.paddle.get_position()
        x = (paddle_coords[0] + paddle_coords[2]) * 0.5
        self.ball = Ball(self.canvas, x, 310)
        self.ball.set_speed_multiplier(self.current_speed)
        self.paddle.set_ball(self.ball)

    def add_brick(self, x, y, hits):
        brick = Brick(self.canvas, x, y, hits)
        self.items[brick.item] = brick

    def draw_text(self, x, y, text, size='40'):
        font = ('Consolas', size)
        return self.canvas.create_text(x, y, text=text,
                                       font=font)

    def update_lives_text(self):
        text = ' Nyawa: %s' % self.lives
        if self.hud is None:
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text=text)

    def start_game(self):
        self.canvas.unbind('<space>')
        self.canvas.delete(self.text)
        self.paddle.ball = None
        self.game_loop()

    def game_loop(self):
        if self.is_paused:
            return  # Exit the loop if the game is paused

        self.check_collisions()
        num_bricks = len(self.canvas.find_withtag('brick'))
        if num_bricks == 0:
            self.ball.speed = None
            self.draw_text(300, 200, 'GGWP')
        elif self.ball.get_position()[3] >= self.height:
            self.ball.speed = None
            self.lives -= 1
            if self.lives < 0:
                self.draw_text(300, 200, 'Nice Try')
            else:
                self.after(1000, self.setup_game)
        else:
            self.ball.update()
            self.after(50, self.game_loop)

    def check_collisions(self):
        ball_coords = self.ball.get_position()
        items = self.canvas.find_overlapping(*ball_coords)
        objects = [self.items[x] for x in items if x in self.items]
        self.ball.collide(objects)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Mentul Mentul')
    game = Game(root)
    game.mainloop()
