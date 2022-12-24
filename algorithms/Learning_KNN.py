
def knn_algo(input):
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    import pandas as pd

    from sklearn.metrics import accuracy_score

    dataset = pd.read_csv('..\\Satisfaction_cleand_rate.csv')


    x_train, x_test, y_train, y_test = train_test_split(
        dataset.iloc[:, 2:13], dataset.iloc[:, 13], test_size=0.1
    )


    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(x_train, y_train)

    prediction = knn.predict(x_test)

    testData = pd.DataFrame({'age': input[0], 'dept': input[1], 'location': input[2],
                             'education': input[3], 'recruitment_type': input[4],
                             'job_level': input[5],
                             'rating': input[6], 'onsite': input[7], 'awards': input[8],
                             'certifications': input[9], 'salary': input[10]},index=[0])

    # print(knn.predict(testData))
    return [knn.predict(testData),accuracy_score(y_test, prediction)]


    # print(x_test)
    # df = pd.DataFrame({'Actual': y_test, 'prediction': prediction})
    # print(df)


    # print()
    # print("Accuracy", accuracy_score(y_test, prediction))


