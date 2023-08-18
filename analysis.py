import pandas as pd
import fourier_transform as ft
from ml_class_and_regr import *


def main():
    labels_df = pd.read_csv('./Data/data_details3.csv')
    filenames = './Data/' + labels_df['directory'].astype(str) + '/' + labels_df['filename'].astype(str)
    filenames = filenames.to_numpy()
    labels_df['avg_freq'] = ''
    transformed_datasets = []
    untransformed_datasets = []
    original_datasets = []

    # reading from directories
    for i in range(0, len(filenames)):
        # getting all the files in a directory
        # print(i)
        temp_fft, avg_frequency, untransformed_dataset, original_dataset = ft.analyse_CSV(filenames[i])
        labels_df.at[i, 'avg_freq'] = avg_frequency
        transformed_datasets.append(temp_fft)
        untransformed_datasets.append(untransformed_dataset)
        original_datasets.append(original_dataset)

    data_num = 1
    plot_after_transformation(original_datasets[data_num], untransformed_datasets[data_num], transformed_datasets[data_num], './plots')

    lin_regression(labels_df['avg_freq'].apply(float), labels_df['weight'].apply(float), 'Linear regression of Weight vs Frequency of Steps', 'Weight')
    print()

    print('Favorite activities vs Frequency of Steps - Classifiers:')
    classifying(labels_df[['avg_freq']].values, labels_df['fav_activity'].values)
    print()

    print('Gender vs Frequency of Steps - Classifiers:')
    classifying(labels_df[['avg_freq']].values, labels_df['gender'].values)
    print()

    print('Shoe types vs Frequency of Steps - Classifiers:')
    classifying(labels_df[['avg_freq']].values, labels_df['shoe_type'].values)
    print()

    plot_piechart('./plots/pie_fav_activity', labels_df,
                  'fav_activity', 'Visualization of favourite activity distribution')
    plot_piechart('./plots/pie_shoe_type', labels_df,
                  'shoe_type', 'Visualization of shoe type distribution')


if __name__ == '__main__':
    main()
