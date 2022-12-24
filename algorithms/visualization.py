
def visualization():
    from pandas import read_csv
    from matplotlib import pyplot
    from seaborn import lineplot, distplot, scatterplot, boxplot

    dataset = read_csv('..\\Satisfaction_cleand_rate.csv')

    lineplot(data=dataset['salary'])

    distplot(a=dataset['rating'], hist=True, bins=3)

    # scatterplot(data=dataset['salary'])

    # boxplot(data=dataset['salary'])

    pyplot.show()

