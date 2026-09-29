import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "solutions"))
sys.setrecursionlimit(200)  # the exam solutions must not rely on deep recursion


def source(name):
    with open(os.path.join(os.path.dirname(__file__), "..", "solutions", name + ".py")) as f:
        return f.read()
