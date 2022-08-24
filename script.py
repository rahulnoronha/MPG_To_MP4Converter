import moviepy.editor as moviepy
import os
import os.path
folder_path = input("Enter the path where your MPG files are")
files = os.listdir(folder_path)
for file in files:
    print(f"{folder_path}{file[0:-4]}.mp4")
    clip = moviepy.VideoFileClip(f"{folder_path}{file[0:-4]}.MPG")
    clip.write_videofile(f"{folder_path}{file[0:-4]}.mp4")