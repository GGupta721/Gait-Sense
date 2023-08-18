import glob
import os
import pandas as pd

labels_df = pd.read_csv('./Data/data_details.csv')


def get_filenames(child_directory):
    filenames = []
    directory = f'./data/{child_directory}/'
    os.chdir(directory)
    for file in glob.glob('*.csv'):
        filenames.append(file)
    lens_labels = len(labels_df)
    for i in range(len(filenames)):
        labels_df.at[i + lens_labels, 'directory'] = child_directory
        labels_df.at[i + lens_labels, 'filename'] = filenames[i][:len(filenames[i])-4]
    print(labels_df)
    labels_df.to_csv('../test.csv', index=False)
    return filenames


filenames3 = get_filenames('round3')

# print(filenames3)