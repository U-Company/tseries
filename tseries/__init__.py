from sklearn.tree import DecisionTreeRegressor
import numpy as np


def any_to_01(line):
    return [[x_i / (len(line) - 1)] for x_i in np.arange(0, len(line))]


def get_functionals(time_serieses, max_depth=30):
    functionals = []
    for el in time_serieses:
        if len(el) == 0:
            el = [0, 0]
        if len(el) == 1:
            el = el * 2
        y = el
        x = any_to_01(y)
        dtr = DecisionTreeRegressor(max_depth=max_depth)
        dtr.fit(x, y)
        functionals.append(dtr)
    return functionals
