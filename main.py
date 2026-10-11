#!/usr/bin/env python3
"""
Tiny embedding similarity search utility.
"""

import argparse, math, sys

def load_embeddings(path):
    embeddings={}
    with open(path,"r",encoding="utf-8") as f:
        for line in f:
            parts=line.strip().split()
            if not parts: continue
            key=parts[0]
            vec=list(map(float,parts[1:]))
            embeddings[key]=vec
    return embeddings

def cosine_similarity(a,b):
    dot=sum(x*y for x,y in zip(a,b))
    norm_a=math.sqrt(sum(x*x for x in a))
    norm_b=math.sqrt(sum(y*y for y in b))
    return dot/(norm_a*norm_b) if norm_a and norm_b else 0.0

def top_n(embeddings, query_vec, n=5):
    sims=[(k,cosine