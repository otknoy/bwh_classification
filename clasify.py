#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans

def kmeans(features, k=8):
    km = KMeans(n_clusters=k, n_jobs=4)
    km.fit(features)
    return km.labels_

if __name__ == '__main__':
    from bwh import load_bwh_data
    names, features = load_bwh_data()


    labels = kmeans(features, k=10)

    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np

    features = np.array(features)
    x, y, z = features.T

    print x, y, z

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(x, y, z)

    plt.show()

    # print "label, name, b, w, h"
    # for l, n, f in zip(labels, names, features):
    #     b, w, h = f

    #     print "%d,%s,%d,%d,%d" % (l, n.encode('utf-8'), b, w, h)
