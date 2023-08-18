import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


# todo: modify
def butterworth_filter(df):
    b, a = signal.butter(2, 0.02, 'low', analog=False)
    low_passed = signal.filtfilt(b, a, df)
    plt.figure()
    plt.title('Linear Acceleration (filtered - before transformation)')
    plt.xlabel('Time')
    plt.ylabel('Acceleration')
    plt.plot(low_passed)
    plt.savefig('./plots/before_transformation_after_filter.png')
    plt.close()
    return low_passed


def perform_FFT(data, frequency):
    # print(data)
    # print('------------')

    data_fft = data.apply(np.fft.fft, axis=0)
    data_fft = data_fft.apply(np.fft.fftshift, axis=0)
    data_fft = data_fft.abs()

    data_fft['frequency'] = frequency
    data['frequency'] = frequency

    # pre_transformed_df = data_fft
    temp_frequency_filter = data_fft[data_fft['frequency'] > 0.1]
    peak_index = temp_frequency_filter['acc'].nlargest(n=1).idxmax()

    # Avegrage steps per second
    average_frequency = data_fft.at[peak_index, 'frequency']
    # print(average_frequency)

    peak_val = data_fft['acc'].nlargest(n=1).idxmax()
    # print(peak_val)
    # print(data_fft.acc[peak_val])
    data_fft.at[peak_val, 'acc'] = temp_frequency_filter['acc'].max()
    # print(data_fft.compare(data))
    # print('------------')

    return data_fft, average_frequency, data


def calculate_SampleFrequency(dataFrame):
    num_samples = len(dataFrame)
    time_interval = dataFrame['time'].iloc[-1]-dataFrame['time'].iloc[0]
    sample_frequency = round(num_samples/time_interval)
    # print(sample_frequency)
    frequency = np.linspace(-sample_frequency/2,
                            sample_frequency/2, num=num_samples)

    return frequency


def analyse_CSV(csvName):
    temp_OriginalData = pd.read_csv(csvName+'.csv')
    temp_NewDataframe = pd.DataFrame(columns=['acc', 'vel'])

    # convert ax,ay,az and wx,wy,wz columns into acc and vel
    temp_NewDataframe['acc'] = np.sqrt(
        temp_OriginalData['ax']**2 + temp_OriginalData['ay']**2 + temp_OriginalData['az']**2)

    temp_NewDataframe['vel'] = np.sqrt(
        temp_OriginalData['wx']**2 + temp_OriginalData['wy']**2 + temp_OriginalData['wz']**2)

    # print(temp_NewDataframe)

    temp_NewDataframe = temp_NewDataframe.apply(butterworth_filter, axis=0)

    # print(temp_NewDataframe)
    # temp_OriginalData['acc'] = temp_NewDataframe['acc']

    frequency = calculate_SampleFrequency(temp_OriginalData)

    temp_fft, avg_frequency, untransformed_df = perform_FFT(
        temp_NewDataframe, frequency)
    # print(temp_fft['frequency'].values)
    # print(temp_fft)

    return temp_fft, avg_frequency, untransformed_df, temp_OriginalData
