#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SPARQLWrapper import SPARQLWrapper, JSON

def fetch_bwh():
    sparql = SPARQLWrapper("http://ja.dbpedia.org/sparql")
    sparql.setQuery("""
    SELECT ?name ?b ?w ?h
WHERE {
    ?name <http://ja.dbpedia.org/property/バスト> ?b ;
        <http://ja.dbpedia.org/property/ウエスト> ?w ;
        <http://ja.dbpedia.org/property/ヒップ> ?h .
}
""")

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    d = []
    for result in results["results"]["bindings"]:
        name = result['name']['value']
        b = result['b']['value']
        w = result['w']['value']
        h = result['h']['value']

        if not all([e.isdigit() for e in [b, w, h]]):
            continue

        b = int(float(b))
        w = int(float(w))
        h = int(float(h))

        if not all([0 < e <= 150 for e in [b, w, h]]):
            continue

        d.append({'name': name, 'b': b, 'w': w, 'h': h})

    return d

def make_feature(data):
    labels = []
    features = []
    for d in data:
        labels.append(d['name'].split('/')[-1])
        features.append([d['b'], d['w'], d['h']])

    return labels, features

def load_bwh_data():
    return make_feature(fetch_bwh())

if __name__ == '__main__':
    print load_bwh_data()
