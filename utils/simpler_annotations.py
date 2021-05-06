import pandas as pd


annotations_file = 'oidv6-train-annotations-bbox.csv'

print('Loading annotations file')
df = pd.read_csv(annotations_file)
print('Success loading annotations file')
df = df[['ImageID', 'LabelName', 'XMin', 'XMax', 'YMin', 'YMax']]
print('Writing new simpler annotations file')
df.to_csv('simpler-' + annotations_file, index=False)
print('Success writing simpler annotations file')

