import pandas as pd

images_info = 'train-images-boxable-with-rotation.csv'
print('Loading images info')
df = pd.read_csv(images_info)
print('Success loading image info')
df = df[['ImageID', 'OriginalURL']]
print('writing simpler images info')
df.to_csv('simpler-' + images_info, index=False)
print('Success writing simpler images info')