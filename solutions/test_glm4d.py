""" Test glm4d module

Run with:

    py.test glmtools
"""

import numpy as np

from glmtools import glm_4d, t_test_3d, glm, t_test

from numpy.testing import assert_almost_equal, assert_equal


def test_glm4d():
    # Test GLM model on 4D data
    # LAB(begin solution)
    np.random.seed(1966)
    I, J, K, T = 2, 3, 4, 5
    P = 5
    Y = np.random.normal(10, 2, size=(I, J, K, T))
    X = np.ones((T, P))
    X[:, 1:] = np.random.normal(5, 1, size=(T, 4))
    # Run 4D code
    c = np.array([-2, -1, 1, 2, 0])
    B_4d, s_2_3d, df = glm_4d(Y, X)
    t_3d, p_3d = t_test_3d(c, X, B_4d, s_2_3d, df)
    assert B_4d.shape == (I, J, K, P)
    assert s_2_3d.shape == (I, J, K)
    assert t_3d.shape == (I, J, K)
    assert p_3d.shape == (I, J, K)
    # Test against 2D code
    Y_2d = Y.reshape((-1, T)).T
    B_2d, s_2_2d, df_2d = glm(Y_2d, X)
    assert_equal(B_2d.T.reshape((I, J, K, P)), B_4d)
    assert_equal(s_2_2d.T.reshape((I, J, K)), s_2_3d)
    assert df_2d == df
    t_2d, p_2d = t_test(c, X, B_2d, s_2_2d, df)
    assert_equal(t_2d.reshape((I, J, K)), t_3d)
    assert_equal(p_2d.reshape((I, J, K)), p_3d)
    # LAB(replace solution)
    # +++your code here+++
    return
    # LAB(end solution)
