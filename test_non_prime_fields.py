# Testing test_non_prime_fields.py
# Only "more complex" functions are tested because lazy

from non_prime_fields import PrimeField, Polynomial, NonPrimeField, zero_poly, one_poly


def test_primefield_invert():
    x = PrimeField(3, 7)
    assert x * x.invert() == PrimeField(1, 7)


def test_polynomial_init_trailing_zeros():
    x = Polynomial([PrimeField(2, 3), PrimeField(0, 3), PrimeField(1, 3), PrimeField(0, 3), PrimeField(0, 3)], 3)
    y = Polynomial([PrimeField(2, 3), PrimeField(0, 3), PrimeField(1, 3), PrimeField(0, 3)], 3)
    assert x == y


def test_polynomial_add():
    x = Polynomial([PrimeField(1, 3), PrimeField(1, 3), PrimeField(0, 3), PrimeField(1, 3)], 3)
    y = Polynomial([PrimeField(2, 3), PrimeField(0, 3), PrimeField(1, 3), PrimeField(1, 3), PrimeField(2, 3)], 3)
    z = Polynomial([PrimeField(0, 3), PrimeField(1, 3), PrimeField(1, 3), PrimeField(2, 3), PrimeField(2, 3)], 3)
    assert x + y == z


def test_polynomial_sub():
    x = Polynomial([PrimeField(1, 3), PrimeField(1, 3), PrimeField(0, 3), PrimeField(1, 3)], 3)
    y = Polynomial([PrimeField(2, 3), PrimeField(0, 3), PrimeField(1, 3), PrimeField(1, 3), PrimeField(2, 3)], 3)
    z = Polynomial([PrimeField(2, 3), PrimeField(1, 3), PrimeField(2, 3), PrimeField(0, 3), PrimeField(1, 3)], 3)
    assert x - y == z


def test_polynomial_mul():
    x = Polynomial([PrimeField(1, 2), PrimeField(1, 2)], 2)
    y = Polynomial([PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    z = Polynomial([PrimeField(1, 2), PrimeField(1, 2), PrimeField(1, 2), PrimeField(1, 2)], 2)
    assert x * y == z


def test_polynomial_div():
    x0 = Polynomial([PrimeField(0, 2), PrimeField(1, 2), PrimeField(1, 2), PrimeField(1, 2)], 2)
    x1 = Polynomial([PrimeField(1, 2), PrimeField(1, 2), PrimeField(1, 2), PrimeField(1, 2)], 2)
    y = Polynomial([PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    z = Polynomial([PrimeField(1, 2), PrimeField(1, 2)], 2)
    assert x0.divmod(y) == (z, one_poly(2))
    assert x0.divmod(y, mod_only=True) == (None, one_poly(2))
    assert x1.divmod(y) == (z, zero_poly(2))
    assert x1.divmod(y, mod_only=True) == (None, zero_poly(2))


def test_polynomial_pow():
    x = Polynomial([PrimeField(1, 2), PrimeField(1, 2)], 2)
    y = Polynomial([PrimeField(1, 2), PrimeField(0, 2), PrimeField(0, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    assert x ** 0 == one_poly(2)
    assert x ** 4 == y


def test_polynomial_lt():
    x0 = Polynomial([PrimeField(0, 2), PrimeField(1, 2)], 2)
    y0 = Polynomial([PrimeField(1, 2), PrimeField(1, 2)], 2)
    x1 = Polynomial([PrimeField(0, 2), PrimeField(1, 2), PrimeField(1, 2)], 2)
    y1 = Polynomial([PrimeField(0, 2), PrimeField(1, 2)], 2)
    x2 = Polynomial([PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    y2 = Polynomial([PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    assert x0 < y0
    assert not x1 < y1
    assert not x2 < y2


def test_polynomial_gt():
    x0 = Polynomial([PrimeField(0, 2), PrimeField(1, 2)], 2)
    y0 = Polynomial([PrimeField(1, 2), PrimeField(1, 2)], 2)
    x1 = Polynomial([PrimeField(0, 2), PrimeField(1, 2), PrimeField(1, 2)], 2)
    y1 = Polynomial([PrimeField(0, 2), PrimeField(1, 2)], 2)
    x2 = Polynomial([PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    y2 = Polynomial([PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    assert not x0 > y0
    assert x1 > y1
    assert not x2 > y2


def test_polynomial_le():
    x0 = Polynomial([PrimeField(0, 2), PrimeField(1, 2)], 2)
    y0 = Polynomial([PrimeField(1, 2), PrimeField(1, 2)], 2)
    x1 = Polynomial([PrimeField(0, 2), PrimeField(1, 2), PrimeField(1, 2)], 2)
    y1 = Polynomial([PrimeField(0, 2), PrimeField(1, 2)], 2)
    x2 = Polynomial([PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    y2 = Polynomial([PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    assert x0 <= y0
    assert not x1 <= y1
    assert x2 <= y2


def test_polynomial_ge():
    x0 = Polynomial([PrimeField(0, 2), PrimeField(1, 2)], 2)
    y0 = Polynomial([PrimeField(1, 2), PrimeField(1, 2)], 2)
    x1 = Polynomial([PrimeField(0, 2), PrimeField(1, 2), PrimeField(1, 2)], 2)
    y1 = Polynomial([PrimeField(0, 2), PrimeField(1, 2)], 2)
    x2 = Polynomial([PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    y2 = Polynomial([PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    assert not x0 >= y0
    assert x1 >= y1
    assert x2 >= y2


def test_polynomial_neg():
    x = Polynomial([PrimeField(0, 3), PrimeField(2, 3), PrimeField(1, 3)], 3)
    y = Polynomial([PrimeField(0, 3), PrimeField(1, 3), PrimeField(2, 3)], 3)
    assert -x == y


def test_nonprimefield_init():
    # a possible confusion: even though x0 = [0, 0, 1] is 'less than' p0 = [1, 1, 1], the
    # remainder is NOT x0, because the remainder would be x0 iff degree(x0) < degree(p0).
    p0 = Polynomial([PrimeField(1, 2), PrimeField(1, 2), PrimeField(1, 2)], 2)
    x0 = NonPrimeField(Polynomial([PrimeField(0, 2), PrimeField(0, 2), PrimeField(1, 2)], 2), p0)
    y0 = Polynomial([PrimeField(1, 2), PrimeField(1, 2)], 2)
    # source: https://math.stackexchange.com/a/844238
    # retrieved: 16/03/2023
    p1 = Polynomial([PrimeField(1, 2),PrimeField(1, 2),PrimeField(0, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    x1 = NonPrimeField(Polynomial([PrimeField(1, 2), PrimeField(1, 2), PrimeField(0, 2), PrimeField(0, 2),
                                  PrimeField(0, 2), PrimeField(1, 2)], 2), p1)
    y1 = Polynomial([PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    assert x0.x == y0
    assert x1.x == y1


def test_nonprimefield_invert():
    # source: https://math.stackexchange.com/a/124313
    # retrieved: 16/03/2023
    p0 = Polynomial([PrimeField(1, 3), PrimeField(2, 3), PrimeField(0, 3), PrimeField(1, 3)], 3)
    x0 = NonPrimeField(Polynomial([PrimeField(1, 3), PrimeField(0, 3), PrimeField(1, 3)], 3), p0)
    y0 = NonPrimeField(Polynomial([PrimeField(2, 3), PrimeField(1, 3), PrimeField(2, 3)], 3), p0)
    x0_invert = x0.invert()
    # source: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Example_2
    # retrieved: 16/03/2023
    p1 = Polynomial([PrimeField(1, 2), PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2), PrimeField(1, 2),
                     PrimeField(0, 2), PrimeField(0, 2), PrimeField(0, 2), PrimeField(1, 2)], 2)
    x1 = NonPrimeField(Polynomial([PrimeField(1, 2), PrimeField(1, 2), PrimeField(0, 2), PrimeField(0, 2),
                                   PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2)], 2), p1)
    y1 = NonPrimeField(Polynomial([PrimeField(0, 2), PrimeField(1, 2), PrimeField(0, 2), PrimeField(1, 2),
                                   PrimeField(0, 2), PrimeField(0, 2), PrimeField(1, 2), PrimeField(1, 2)], 2), p1)
    x1_invert = x1.invert()
    assert x0_invert == y0
    assert x0 * x0_invert == x0 * x0_invert.x == NonPrimeField(one_poly(3), p0)
    assert x1_invert == y1
    assert x1 * x1_invert == x1 * x1_invert.x == NonPrimeField(one_poly(2), p1)


def test_nonprimefield_repr():
    p = Polynomial([PrimeField(1, 2), PrimeField(1, 2), PrimeField(1, 2)], 2)
    x0 = NonPrimeField(Polynomial([PrimeField(0, 2), PrimeField(0, 2), PrimeField(1, 2)], 2), p)
    x1 = NonPrimeField(p, p)
    assert str(x0) == f"3 (mod { p })"
    assert str(x1) == f"0 (mod { p })"
