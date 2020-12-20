class FiledElement:
    """构建有限域，有限域的加法和减法，乘法，指数，除法运算"""
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'num {} not in field range 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

# 有限域的加法
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

# 有限域的减法
    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot sub two numbers in different Fields')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

# 有限域的乘法
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot mul two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

# 有限域的指数运算,注意指数的幂部分是一个整数
    def __pow__(self, exponent):
        # 使指数最后转到0到prime-2的范围内
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

# 有限域的除法
    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
        num = self.num * pow(other.num, self.prime - 2, self.prime) % self.prime
        return self.__class__(num, self.prime)
