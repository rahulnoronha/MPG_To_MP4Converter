import tkinter as tk
from tkinter import filedialog
import moviepy.editor as moviepy
import os
import os.path
folder_path = filedialog.askdirectory()
files = os.listdir(folder_path)
for file in files:
    print(f"{folder_path}{file[0:-4]}.mp4")
    clip = moviepy.VideoFileClip(f"{folder_path}/{file[0:-4]}.MPG")
    clip.write_videofile(f"{folder_path}/{file[0:-4]}.mp4")