""" Run GLM on final dimension of 4D arrays
"""

import numpy as np

from .glm import glm, t_test


def glm_4d(Y, X):
    """ Run GLM on on 4D data `Y` and design `X`

    Parameters
    ----------
    Y : array shape (I, J, K, T)
        4D array to fit to model with design `X`.  Column vectors are vectors
        over the final length T dimension.
    X : array ahape (T, P)
        2D design matrix to fit to data `Y`.

    Returns
    -------
    B : array shape (I, J, K, P)
        parameter array, one length P vector of parameters for each voxel.
    sigma_2 : array shape (I, J, K)
        unbiased estimate of variance for each voxel.
    df : int
        degrees of freedom due to error.
    """
    # LAB(begin solution)
    I, J, K, T = Y.shape
    P = X.shape[1]
    Y_2d = Y.reshape((-1, T)).T
    B_2d, s_2_2d, df = glm(Y_2d, X)
    return B_2d.T.reshape((I, J, K, P)), s_2_2d.reshape((I, J, K)), df
    # LAB(replace solution)
    # +++your code here+++
    return
    # LAB(end solution)


def t_test_3d(c, X, B, sigma_2, df):
    """ Two-tailed t-test on 3D estimates given contrast `c`, design `X`

    Parameters
    ----------
    c : array shape (P,)
        contrast specifying conbination of parameters to test.
    X : array shape (N, P)
        design matrix.
    B : array shape (I, J, K, P)
        parameter array, one length P vector of parameters for each voxel.
    sigma_2 : array shape (I, J, K)
        unbiased estimate of variance for each voxel.
    df : int
        degrees of freedom due to error.

    Returns
    -------
    t : array shape (I, J, K)
        t statistics for each data vector.
    p : array shape (V,)
        two-tailed probability value for each t statistic.
    """
    # LAB(begin solution)
    I, J, K, P = B.shape
    t_1d, p_1d = t_test(c, X, B.reshape((-1, P)).T, sigma_2.ravel(), df)
    return t_1d.reshape((I, J, K)), p_1d.reshape((I, J, K))
    # LAB(replace solution)
    # Your code code here
    return
    # LAB(end solution)
