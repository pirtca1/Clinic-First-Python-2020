#!/usr/bin/env python

from tkinter import *
import tkinter as tk

root = Tk()

content = tk.Frame(root)
frame = tk.Frame(content, borderwidth = 5, relief = "sunken", width = 500, height = 400)

levelLoading = tk.Label(content, text = "Level Loading")
continuity = tk.Label(content, text = "Continuity")
randomChoice = tk.Label(content, text = "Random")

upload = tk.Button(content, text = "Upload Data")
generate = tk.Button(content, text = "Generate!")
exportChoice = tk.Button(content, text = "Export")

content.grid(column = 0, row =0)
frame.grid(column = 0, row = 0, columnspan = 3, rowspan = 2)



upload.grid(column = 0, row = 4, columnspan = 1, sticky=( S, E, W))
generate.grid(column = 1, row = 4, columnspan = 1, sticky=( S, E, W))
exportChoice.grid(column = 2, row = 4, columnspan = 1, sticky=( S, E, W))
levelLoading.grid(column = 2, row = 3, sticky=( N,S, E, W))
continuity.grid(column = 1, row = 3, sticky=( N,S, E, W))
randomChoice.grid(column = 0, row = 3, sticky=( N,S, E, W))

root.columnconfigure(0, weight=10)
root.rowconfigure(0, weight=10)
content.columnconfigure(0, weight=30, pad= 3)
content.columnconfigure(1, weight=30, pad= 3)
content.columnconfigure(2, weight=30, pad= 3)
content.columnconfigure(3, weight=10, pad= 3)
content.columnconfigure(4, weight=10, pad= 3)
content.rowconfigure(1, weight=10)

root.mainloop()

