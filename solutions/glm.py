""" Functions for running GLM on 2D and 3D data
"""

import numpy as np
import numpy.linalg as npl

# LAB(begin solution)
import scipy.stats
# LAB(end solution)


def glm(Y, X):
    """ Run GLM on on data `Y` and design `X`

    Parameters
    ----------
    Y : array shape (N, V)
        1D or 2D array to fit to model with design `X`.  `Y` is column
        concatenation of V data vectors.
    X : array ahape (N, P)
        2D design matrix to fit to data `Y`.

    Returns
    -------
    B : array shape (P, V)
        parameter matrix, one column for each column in `Y`.
    sigma_2 : array shape (V,)
        unbiased estimate of variance for each column of `Y`.
    df : int
        degrees of freedom due to error.
    """
    # LAB(begin solution)
    B = npl.pinv(X).dot(Y)
    E = Y - X.dot(B)
    df = X.shape[0] - npl.matrix_rank(X)
    sigma_2 = np.sum(E ** 2, axis=0) / df
    return B, sigma_2, df
    # LAB(replace solution)
    # +++your code here+++
    return
    # LAB(end solution)


def t_test(c, X, B, sigma_2, df):
    """ Two-tailed t-test given contrast `c`, design `X`

    Parameters
    ----------
    c : array shape (P,)
        contrast specifying conbination of parameters to test.
    X : array shape (N, P)
        design matrix.
    B : array shape (P, V)
        parameter estimates for V vectors of data.
    sigma_2 : float
        estimate for residual variance.
    df : int
        degrees of freedom due to error.

    Returns
    -------
    t : array shape (V,)
        t statistics for each data vector.
    p : array shape (V,)
        two-tailed probability value for each t statistic.
    """
    # LAB(begin solution)
    t_dist = scipy.stats.t(df=df)
    b_cov = npl.pinv(X.T.dot(X))
    t = c.dot(B) / np.sqrt(sigma_2 * c.dot(b_cov).dot(c))
    p_values = (1 - t_dist.cdf(np.abs(t))) * 2
    return t, p_values
    # LAB(replace solution)
    # Your code code here
    return
    # LAB(end solution)
