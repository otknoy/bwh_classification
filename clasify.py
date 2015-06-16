#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer

def kmeans(features, k=8):
    km = KMeans(n_clusters=k, n_jobs=4)
    km.fit(features)
    return km.labels_

def dimension_reduction(features, dim):
    lsa = TruncatedSVD(dim)
    return lsa.fit_transform(features)

def normalize(features):
    return Normalizer().fit_transform(features)

if __name__ == '__main__':
    from bwh import load_bwh_data
    names, features = load_bwh_data()
    features = np.array(features)

    k = 10
    labels = kmeans(features, k=k)

    for l, n, f in zip(labels, names, features):
        print l, n.encode('utf-'), f

    exit()


    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt

    colors = ['b', 'b', 'r', 'c', 'm', 'y', 'k', 'w']
    fig = plt.figure()
    ax = Axes3D(fig)
    for l, n, f in zip(labels, names, features):
        ax.scatter3D(f[0], f[1], c=colors[l%len(colors)], alpha=0.5)
    plt.show()

    # print "label, name, b, w, h"
    # for l, n, f in zip(labels, names, features):
    #     b, w, h = f

    #     print "%d,%s,%d,%d,%d" % (l, n.encode('utf-8'), b, w, h)
