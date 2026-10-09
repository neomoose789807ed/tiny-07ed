"""
Tiny embedding similarity search utility.
Loads space-separated embeddings from a file and finds the top‑k nearest items to a query vector.
"""

import argparse, math, sys

def load(file):
    d={}
    for line in open(file):
        parts=line.strip().split()
        if not parts: continue
        key, vec=parts[0], [float(x) for x in parts[1:]]
        d[key]=vec
    return d

def vec_from_str(s):
    return [