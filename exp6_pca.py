""" Experiment 6: Perform PCA """
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X = iris.data

# Perform PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("Explained variance ratio:", pca.explained_variance_ratio_)
print("First 5 PCA-transformed samples:\n", X_pca[:5])
