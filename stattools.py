import math


def permutation(n, r):
    """Number of ways of ordering n distinct objects
    (total) taken r at a time (how many)"""
    return math.factorial(n) / math.factorial(n-r)


def combination(n, r):
    """Number of combinations n objects taken r at a time
    is the number of subsets, each of size r,
    that can be formed from objects."""
    return permutation(n, r) / math.factorial(r)

class discrete_random():
    """Discrete Random Variables and Their Probability Distributions"""

    def probability_distribution(self, y, n, a, t):
        """Random Variables - Probability Distribution
        All selections being equally likely
        n - number of elements being selected
        y - random variable for selected balls
        a - number of primary elements
        t - total elements
        Returns na
        """
        return combination(a, y) * combination(t-a, n-y)

    def pmf(self, y, n, a, t):
        """Probability mass function
        n - number of elements being selected
        y - random variable for selected balls
        a - number of primary elements
        t - total elements
        returns pmf(y) = P(A) = na / ns
        """
        return self.probability_distribution(y, n, a, t) / combination(t, n)


class binomial_distribution():
    """Binomial Distribution - Discrete Random"""

    def pmf(self, y, n, p, q=None):
        """Binomial Distribution

        y - number of successes
        n - number of trials
        p - probability of success
        q - probability of failure (1-p) if None
        """
        if not q:
            q = 1-p
        return combination(n, y) * (p ** y) * (q ** (n-y))

    def expected(self, n, p):
        """Binomial - Expected Value
        n - number of trials
        p - probability of success
        """
        return n * p

    def variance(self, n, p, q=None):
        """Binomial - Variance
        n - number of trials
        p - probability of success
        q - probability of failure (1-p) if None
        """
        if not q:
            q = 1-p
        return n * p * q


class geometric_distribution():
    """Geometric Distribution - Discrete Random"""

    def pmf(self, y, p, q=None):
        """Geometric Distribution

        y - number of trials up to and including first success
        p - probability of success
        q - probability of failure (1-p) if None
        """
        if not q:
            q = 1-p
        return (q ** (y-1)) * p

    def expected(self, p):
        """Geometric - Expected
        p - probability of success
        """
        return 1 / p

    def variance(self, p):
        """Geometric - Variance
        p - probability of success
        """
        return (1-p) / p ** 2

    def success_onorbefore(self, n, p):
        """Geometric - Success occurs on or before
        n - trial
        p - probability of success
        """
        return 1 - (1-p)**n

    def success_before(self, n, p):
        """Geometric - Success occurs before
        n - trial
        p - probability of success
        """
        return 1-(1-p)**(n-1)

    def success_onorafter(self, n, p):
        """Geometric - Success occurs on or after
        n - trial
        p - probability of success
        """
        return (1-p)**(n-1)

    def success_after(self, n, p):
        """Geometric - Success occurs after
        n - trial
        p - probability of success
        """
        return (1-p) ** n


class hypergeometric_distribution():

    def _numerator(self, N, n, r, y):
        """Hypergeometric Distribution
        Given a finite population (set) of N items which comprise r Type1 items N-r Type 2 items.
        Select n such objects from a population without replacement such that all selections are equally likely.
        Find y Type1 items in the selection.
        """
        return combination(r, y) * combination(N-r, n-y)

    def pmf(self, N, n, r, y):
        """Returns the Probability Mass Function of the hypergeometric Distribution"""
        return self._numerator(N, n, r, y) / combination(N, n)

    def expected(self, N, n, r):
        """Expected value of Hypergeometric Distribution
        Population mean (lowercase greek mu)
        mu = E(Y) = n*r / N
        """
        return (n*r)/N

    def variance(self, N, n, r):
        """Variance of Hypergeometric Distribution
        Hypergeometric Population Variance (lowercase sigma^2)
        sigma^2 = V(Y) = n(r/N)(N-r / N)(N-n / N-1)
        """
        return n * (r / N) * ((N-r)/N)*((N-n)/(N-1))


class poisson_distribution():
    def pmf(self, lam, y):
        """Poisson Distribution
        incidents (successes) occur independently in continuous time at a constant rate"""
        return (lam ** y) / (math.factorial(y) * math.e ** lam)

    def expected(self, lam):
        """Poisson Distribution
        lam - Expected value
        """
        return lam


class tchebysheff_distribution():
    def mean(self, mean):
        return mean

    def variance(self, v):
        return v

    def std(self, v):
        """Given a variance v, returns standard deviation"""
        return math.sqrt(v)

    def within_low(self, mean, std, lower):
        return (mean - lower) / std

    def within_upp(self, mean, std, upper):
        return (upper - mean) / std

    def pmf(self, k):
        """
        k - within value
        """
        return 1 - (1 / k ** 2)


class uniform_distribution():
    """Holds functions for Uniform Distributions"""

    def dist_density(self, a, b, c, d):
        """Uniform Distribution - Density function (Continuous)
        P(c <= Y <= d) = integrate(c, d) [1 / (a-b)]
        """
        return (d - c) / (b - a)

    def dist_expected(self, a, b):
        """Expected value for uniform distribution
        E(X) = integral(a, b) [xf(x)] = b-a / 2
        """
        return (b - a) / 2

    def dist_variance(self, a, b):
        """Variance of uniform distribution"""
        return (b - a) ** 2 / 12
