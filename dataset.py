import os
from PIL import Image
import numpy as np

img_dir = 'resources/processed/all'
files = [x for x in os.listdir(img_dir) if x[-4:] == '.png']
dataset = np.empty((len(files),28,28,1))
for i,file in enumerate(files):
      img = Image.open(os.path.join(img_dir, file))
      dataset[i] = np.expand_dims(np.array(img),axis=2)
np.save('dataset.npy', dataset)