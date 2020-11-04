import glob
import os

print('deleting old frames')

for image in glob.glob('assets/generated_images/*.png'):
  os.remove(image)
  print(f'removed {image}')

try:
  os.remove('final.mp4')
except FileNotFoundError:
  print('no video.mp4 file found.')
