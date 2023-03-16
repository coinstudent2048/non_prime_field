# non_prime_fields
A stupid implementation of non-prime fields $\mathrm{GF}(p^n)$ with prime $p$ and $n>1$.

**Never use in production! All algorithms are naive, so it's not even efficient!**

As usual, non-prime fields are constructed using the polynomial ring with coefficients in $\mathrm{GF}(p)$ (denoted as $\mathrm{GF}(p)[X]$) and an irreducible polynomial $P \in \mathrm{GF}(p)[X]$ of degree $n$. Then we have $\mathrm{GF}(p^n) = \mathrm{GF}(p)[X]/P$.

#### Sample Usage
````python
from non_prime_fields import PrimeField, Polynomial, NonPrimeField

# GF(4). p is the irreducible polynomial
p = Polynomial([PrimeField(1, 2), PrimeField(1, 2), PrimeField(1, 2)], 2)
a = NonPrimeField(Polynomial([PrimeField(1, 2), PrimeField(1, 2)], 2), p)

# order. output should be 4
print(a.ord)

# integer representation. output should be 3
print(a.int)

# output should be '0 (mod [1, 1, 1] (mod 2))'
print(2 * a)

# output should be '2 (mod [1, 1, 1] (mod 2))'
print(a.invert())
````

**Note:** The polynomial representation `[c0, c1, ..., cN]` means $c_0 + c_1 x + \ldots + c_n x^n$. So for example, `[1, 1, 1]` is $1 + x + x^2$ and `[0, 1]` is just $x$.

#### What is this for?
I initially want to implement dumb12_381 (for BLS12-381 curve), but got lazy. Nonetheless this is still for playing with math and cryptography.

#### Testing
Just run `pytest` to test.
