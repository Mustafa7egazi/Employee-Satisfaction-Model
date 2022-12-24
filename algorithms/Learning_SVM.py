def svm_algo(input):
    from sklearn.model_selection import train_test_split
    import pandas as pd
    from sklearn import svm
    from sklearn.metrics import mean_squared_error, accuracy_score

    dataset = pd.read_csv('..\\Satisfaction_cleand_rate.csv')



    # x = dataset.drop('satisfied', 1)
    # y = dataset['satisfied']

    x_train, x_test, y_train, y_test = train_test_split(
        dataset.iloc[:, 2:13], dataset.iloc[:, 13], test_size=0.1
    )

    supportVM = svm.SVC(kernel='rbf')
    supportVM.fit(x_train, y_train)
    # print(y_test)

    prediction = supportVM.predict(x_test)

    testData = pd.DataFrame({'age': input[0], 'dept': input[1], 'location': input[2],
                             'education': input[3], 'recruitment_type': input[4],
                             'job_level': input[5],
                             'rating': input[6], 'onsite': input[7], 'awards': input[8],
                             'certifications': input[9], 'salary': input[10]}, index=[0])

    # predict from GUI
    print(supportVM.predict(testData))
    return [supportVM.predict(testData), accuracy_score(y_test, prediction)]

    # print(prediction)
    # df = pd.DataFrame({'Actual': y_test, 'prediction': prediction})
    # print(df)

    # lin_mse = mean_squared_error(y_test, prediction)
    # lin_rmse = np.sqrt(lin_mse)
    # print(lin_rmse)
    # print("Accuracy ", accuracy_score(y_test, prediction))
