# Interface gráfica com Tkinter

from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.geometry('100x100')

def clique_aqui():
    msg = messagebox.showinfo('Curso de Python', 'Seja bem vindo(a)')

btn = Button(tk, text='Clique aqui', command = clique_aqui)
btn.place(x=50, y=50)

tk.mainloop()

