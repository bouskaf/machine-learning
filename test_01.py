from sklearn import tree
from sklearn import svm
from sklearn import linear_model
from sklearn import neighbors
from sklearn import preprocessing

# gender classifier using the sci-kit learn library

# try different classifiers
knn_classifier = neighbors.KNeighborsClassifier()
decision_tree_classifier = tree.DecisionTreeClassifier()
logistic_regression_classifier = linear_model.LogisticRegression()
svm_classifier = svm.SVC()

# train data
# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# train labels
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

# train each classifier on data
knn_classifier = knn_classifier.fit(X,Y)
decision_tree_classifier = decision_tree_classifier.fit(X, Y)
logistic_regression_classifier = logistic_regression_classifier.fit(X,Y)
svm_classifier = svm_classifier.fit(X, Y)


le = preprocessing.LabelEncoder()
le.fit(Y)
logistic_regression_classifier = logistic_regression_classifier.fit(X, le.transform(Y))

print(le.transform(Y))
le.transform(Y)
prediction = decision_tree_classifier.predict([[190, 70, 43]])
prediction_svm = svm_classifier.predict([[190, 70, 43]])
prediction_regr = logistic_regression_classifier.predict([[150, 50, 38]])


# CHALLENGE compare their reusults and print the best one!

print(prediction)
print(prediction_svm)
print(le.inverse_transform(prediction_regr))