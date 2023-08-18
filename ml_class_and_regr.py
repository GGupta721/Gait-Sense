import numpy as np
import pandas as pd
from plotting import *
import sys
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import seaborn
from scipy import stats
seaborn.set()


def classifying(x, y):
    num_runs = 150

    count = 0
    bayes_score = 0
    knn_score = 0
    rf_score = 0

    for i in range(num_runs):
        x_train, x_valid, y_train, y_valid = train_test_split(x, y)
        bayes_model = GaussianNB().fit(x_train, y_train)
        knn_model = KNeighborsClassifier(n_neighbors=5).fit(x_train, y_train)
        rf_model = RandomForestClassifier(n_estimators=500, min_samples_leaf=5, max_depth=3).fit(x_train, y_train)

        bayes_score += bayes_model.score(x_valid, y_valid)
        knn_score += knn_model.score(x_valid, y_valid)
        rf_score += rf_model.score(x_valid, y_valid)

        count += 1



    print(f'Bayes Model score: {bayes_score/count}')
    print(f'KNN Model score: {knn_score/count}')
    print(f'Random Forest Model score: {rf_score/count}')


def lin_regression(x, y, title, titleY):

    model = stats.linregress(x, y)
    score = model.pvalue

    # coefficients = model.coef_
    print(f'{title} score: {score}')
    save_dir = f'./plots/{title}'
    plot_regression(model, save_dir, title + '', 'Frequency of Steps', titleY, x, y, legends=['Scatter-plotted Data', 'Regression'])


