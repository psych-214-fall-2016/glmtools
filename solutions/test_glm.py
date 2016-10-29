""" py.test test for glmtools code

Run with:

    py.test glmtools
"""

import numpy as np

# LAB(begin solution)
from scipy.stats import linregress, ttest_ind
# LAB(end solution)

from glmtools import glm, t_test

from numpy.testing import assert_almost_equal


def test_glm_t_test():
    # Test glm and t_test against scipy
    # LAB(begin solution)
    np.random.seed(1966)
    n = 100
    v = 3
    Y = np.random.normal(12, 3, size=(n, v))
    x = np.random.normal(5, 2, size=n)
    # GLM simple regression
    X = np.ones((n, 2))
    X[:, 1] = x
    B, s_2, df = glm(Y, X)
    c = np.array([0, 1])
    t, p = t_test(c, X, B, s_2, df)
    # scipy.stats.linregress
    for data_col_no in range(v):
        res = linregress(x, Y[:, data_col_no])
        assert_almost_equal(res.intercept, B[0, data_col_no])
        assert_almost_equal(res.slope, B[1, data_col_no])
        # Test against two-tailed p value
        assert_almost_equal(res.pvalue, p[data_col_no])
    # Two sample t-test
    X2 = np.zeros((n, 2))
    # Size of first group
    n_1 = 25
    X2[:n_1, 0] = 1
    X2[n_1:, 1] = 1
    B, s_2, df = glm(Y, X2)
    c = np.array([1, -1])
    t, p = t_test(c, X2, B, s_2, df)
    # scipy.stats.ttest_ind
    for data_col_no in range(v):
        y = Y[:, data_col_no]
        res = ttest_ind(y[:n_1], y[n_1:])
        assert_almost_equal(res.statistic, t[data_col_no])
        assert_almost_equal(res.pvalue, p[data_col_no])
    # LAB(replace solution)
    # Your test code here
    return
    # LAB(end solution)
