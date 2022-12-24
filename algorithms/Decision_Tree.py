

def decision_algo(input):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score

    dataset = pd.read_csv('..\\Satisfaction_cleand_rate.csv')



    # x = dataset.iloc[:, 2:13].values
    # y = dataset.iloc[:, 13].values

    x_train, x_test, y_train, y_test = train_test_split(
        dataset.iloc[:, 2:13], dataset.iloc[:, 13], test_size=0.1, random_state=0)

    # st_x = StandardScaler()
    # x_train = st_x.fit_transform(x_train)
    # x_test = st_x.transform(x_test)

    classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)

    # accuracy = accuracy_score(y_test, y_pred)
    # print(accuracy)

    testData = pd.DataFrame({'age': input[0], 'dept': input[1], 'location': input[2],
                             'education': input[3], 'recruitment_type': input[4],
                             'job_level': input[5],
                             'rating': input[6], 'onsite': input[7], 'awards': input[8],
                             'certifications': input[9], 'salary': input[10]}, index=[0])

    # print(classifier.predict(testData))
    return [classifier.predict(testData), accuracy_score(y_test, y_pred)]
