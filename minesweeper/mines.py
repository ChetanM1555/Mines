from tkinter import *
import config as co
import util as ut

root = Tk()
# overides settings
root.configure(bg="black")
root.geometry(f"{co.WIDTH}x{co.HEIGHT}")
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(root, bg="grey", width=co.WIDTH, height=ut.height_percentage(25))
top_frame.place(x=0, y=0)

left_frame = Frame(root,bg="red", width=ut.width_percentage(25), height=ut.height_percentage(75))
left_frame.place(x=0,y=ut.height_percentage(25))

center_frame = Frame(root, bg="white", height=ut.height_percentage(75), width=ut.width_percentage(75))
center_frame.place(x=ut.width_percentage(25) ,y=ut.height_percentage(25))

root.mainloop()