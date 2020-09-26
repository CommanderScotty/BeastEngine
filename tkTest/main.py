import tkinter as tk


class Renderer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.resolution = {'x': self.window.winfo_screenwidth(), 'y': self.window.winfo_screenheight()}
        self.canvas = tk.Canvas(self.window, bg='black', highlightthickness=0, width=self.resolution['x'], height=self.resolution['y'])
        self.render('placeholder')
        self.window.mainloop()


    def render(self, game):
        self.canvas.delete("all")
        line0 = self.canvas.create_line(0, 0, self.resolution['x'], self.resolution['y'], fill='red')
        line1 = self.canvas.create_line(self.resolution['x'], 0, 0, self.resolution['y'], fill='green', width=10)
        self.canvas.pack()
        

if __name__ == '__main__':
    test = Renderer()
