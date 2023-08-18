import matplotlib.pyplot as plt


# todo
def plot_classifier(model, xt, yt, title, path):
    plt.figure(figsize=(10, 5))
    plt.subtitle(f'Predictions of {title}')
    plt.subplot(1, 2, 1)
    plt.title('Inputs')
    plt.xlabel()
    plt.savefig(f'{path}.png')


def plot_after_transformation(o_df, u_df, tran_df, directory):

    plt.figure()
    plt.plot(tran_df['frequency'], tran_df['acc'])
    plt.title('Linear Acceleration (transformed)')
    plt.xlabel('Frequency')
    plt.savefig(f'{directory}/after_transformation.png')
    plt.close()


def plot_graph(save_dir, title, x_axis_title, y_axis_title, x_axis, y_axis):
    plt.figure()
    plt.plot(x_axis, y_axis)
    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)
    plt.title(title)
    plt.savefig(save_dir + '.png')
    plt.close()


def plot_regression(model, save_dir, title, x_axis_title, y_axis_title, x_axis, y_axis, legends):
    plt.figure()
    plt.plot(x_axis, y_axis, 'g.')
    plt.plot(x_axis, x_axis*model.slope + model.intercept, 'b-')
    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)
    plt.legend(legends)
    plt.title(title)
    plt.savefig(save_dir + '.png')
    plt.close()


def plot_piechart(save_dir, data_summary, selected_attribute, title):
    plt.figure()
    grouped_data = data_summary.groupby(data_summary[selected_attribute])[
        'avg_freq'].sum()
    plt.axis('equal')
    plt.pie(grouped_data, autopct='%1.1f%%', labels=grouped_data.index,
            shadow=True, startangle=90, wedgeprops={"edgecolor": "black",
                                                    'linewidth': 1,
                                                    'antialiased': True})
    plt.title(title)
    plt.legend(title="Legend:", loc='lower right')
    # plt.show()
    plt.savefig(save_dir + '.png')
    plt.close()
