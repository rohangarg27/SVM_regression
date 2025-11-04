""" Experiment 5: K-means, Gaussian Mixture, and Hierarchical Clustering """
from sklearn import datasets
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture

# Load dataset
iris = datasets.load_iris()
X = iris.data

# K-means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X)

# Gaussian Mixture
gmm = GaussianMixture(n_components=3, random_state=42)
gmm_labels = gmm.fit_predict(X)

# Hierarchical Clustering
hier = AgglomerativeClustering(n_clusters=3)
hier_labels = hier.fit_predict(X)

print("KMeans Labels:", kmeans_labels[:10])
print("GMM Labels:", gmm_labels[:10])
print("Hierarchical Labels:", hier_labels[:10])
