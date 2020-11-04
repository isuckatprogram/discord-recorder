import cv2
from cv2 import VideoWriter, VideoWriter_fourcc
import glob
import os

# import pyttsx3
# engine = pyttsx3.init()

# engine.setProperty('rate', 125)  
# engine.setProperty('volume',1.0) 

# voices = engine.getProperty('voices')  

# engine.setProperty('voice', voices[1].id)

# def generate_audio(text, filename="audio.mp4"):
#   engine.save_to_file(text, filename)
#   engine.runAndWait()

def generate_video():
  images = []
  width = 531
  height = 78

  size = ( width, height)

  for image in glob.glob('assets/generated_images/*.png'):
    img = cv2.imread(image)
    images.append(img)

  video = cv2.VideoWriter('final.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 1.5, size)
  
  for i in range(len(images)):
    video.write(cv2.resize(images[i],size))

  video.release()

  return 'project.mp4'
