#import dependancies
from sklearn import tree
#our labelled data
#the first number is the horsepower of the car
#the second number is the number of seats
features=[300,2],[450,2],[200,8],[150,9]
#0 is the label for a sports car
#1 is the  label for a minivan
labels=[0,0,1,1]
#load our classifier
classifier=tree.DecisionTreeClassifier()
#the fit function is used to train our classifier on the training data
classifier.fit(features,labels)
#test drive
print classifier.predict([350,2])
#visualization of our tree
classifier = classifier.fit(features, labels)
tree.export_graphviz(clf,out_file='tree.dot')

