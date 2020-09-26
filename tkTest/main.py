import tkinter as tk

class Renderer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.resolution = (1920, 1080)
        self.canvas = tk.Canvas(self.window, bg='black', highlightthickness=0, width=self.resolution[0], height=self.resolution[1])
        self.render('placeholder')
        self.window.mainloop()


    def render(self, game):
        self.canvas.delete("all")
        line0 = self.canvas.create_line(0, 0, 1920, 1080, fill='red')
        line1 = self.canvas.create_line(1920, 0, 0, 1080, fill='green', width=10)
        self.canvas.pack()
        

if __name__ == '__main__':
    test = Renderer()
