""" Experiment 8: CART Algorithm for Categorization """
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Decision Tree (CART)
clf = DecisionTreeClassifier(criterion='gini', random_state=42)
clf.fit(X_train, y_train)

# Evaluation
print("Decision Tree Accuracy:", clf.score(X_test, y_test))
print("\nTree Structure:\n", export_text(clf, feature_names=iris.feature_names))
