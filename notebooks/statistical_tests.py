import numpy as np
from scipy import stats

def bootstrap_pearsonr(y_true, y_pred, n_samples=10000, seed=42):
    """Estimates a two-sided confidence interval for the Pearson correlation coefficient using the bootstrap method."""
    assert len(y_true) == len(y_pred)
    indices = np.arange(len(y_true))
    coefficients = []
    r = stats.pearsonr(y_true, y_pred)[0]
    rng = np.random.default_rng(seed)
    for i in range(n_samples):
        sample_indices = rng.choice(indices, size=len(indices), replace=True)
        y_true_sample = y_true[sample_indices]
        y_pred_sample = y_pred[sample_indices]
        r_boot = stats.pearsonr(y_true_sample, y_pred_sample)[0]
        coefficients.append(r_boot)
    quantiles = np.quantile(coefficients, q=[0.025, 0.975])
    return r, *quantiles

def permutation_pearsonr(y_true, y_pred, n_samples=10000, seed=42):
    """Performs a one-sided permutation test for the Pearson correlation coefficient.

    Under the null hypothesis that the Pearson correlation coefficient is zero, for n random permutations
    the p-value is the proportion of random permutations b for which the correlation coefficient is at least
    as large as the measured correlation coefficient, p. We use a permutation test as scipy's built-in method
    assumes normality of the distribution of both datasets.

    p = (b + 1) / (n + 1)
    """
    assert len(y_true) == len(y_pred)
    indices = np.arange(len(y_true))
    r = stats.pearsonr(y_true, y_pred)[0]
    rng = np.random.default_rng(seed)
    b = 0
    rng = np.random.default_rng(seed)
    for i in range(n_samples):
        sample_indices = rng.choice(indices, size=len(indices), replace=False)
        y_pred_sample = y_pred[sample_indices]
        r_perm = stats.pearsonr(y_true, y_pred_sample)[0]
        if r_perm > r:
            b += 1
    p = (b + 1) / (n_samples + 1)
    return r, p
