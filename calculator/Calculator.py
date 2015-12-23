"""
This package contains basic mathematical implementation with the following functionality

    1. add - addition
    2. sub - subtraction
    3. mul - multiplication
    4. div - division
    5. pwr - power
    6. log - logarithm
    7. exp - exponential
"""

import math
import Constants


class Calculator:

    # Methods
    def __init__(self):
        """
        Constructor for the class
        :param: none
        :return: nothing
        """
        self.result = 0

    def add(self, num1=0, num2=0):
        """
        Addition of two numbers
        add(a,b) -> sum of a and b
        :param num1: int, float, double, const or long
        :param num2: int, float, double, const or long
        :return: num1 + num2
        """
        self.result = num1 + num2
        print 'Sum is: %f' % self.result
        return self.result

    def sub(self, num1=0, num2=0):
        """
        Difference of two numbers
        sub(a,b) -> difference of a and b
        :param num1: int, float, double, const or long
        :param num2: int, float, double, const or long
        :return: num1 - num2
        """
        self.result = num1 - num2
        print 'Difference is: %f' % self.result
        return self.result

    def mul(self, num1=0, num2=0):
        """
        Multiplication of two numbers
        mul(a,b) -> multiplication of a and b
        :param num1: int, float, double, const or long
        :param num2: int, float, double, const or long
        :return: num1 * num2
        """
        self.result = num1 * num2
        print 'Product is: %f' % self.result
        return self.result

    def div(self, num1=1, num2=1):
        """
        Division of two numbers
        div(a,b) -> division of a and b
        :param num1: int, float, double, const or long
        :param num2: int, float, double, const or long
        :return: num1 / num2
        """
        try:
            self.result = num1 / float(num2)
        except ZeroDivisionError:
            print "Division not possible, cannot divide with zero"
        else:
            print 'Division is: %f' % self.result
            return self.result

    def pwr(self, b=1, n=0):
        """
        Exponentiation with base b and exponent n
        pwr(b,n) ->  exponentiation with base b and exponent n
        :param b: base (can be int, float, double, const or long)
        :param n: exponent (can be int, float, double, const or long)
        :return: b ** n
        """
        try:
            self.result = b ** float(n)
        except ValueError:
            print "Negative number cannot be raised to a fractional power"
        else:
            print 'Power is: %f' % self.result
            return self.result

    def log(self, a, b=10):
        """
        Logarithm of a with base b
        log(a,n) ->  exponentiation with base a and exponent n
        :param a: int, float, double, const or long
        :param b: base (can be int, float, double, const or long)
        :return: log(a,b)
        """
        try:
            self.result = math.log(a, b)
        except ValueError:
            print "Logarithm doesn't exist for the specified value"
        else:
            print 'Logarithm is: %f' % self.result
            return self.result

    def exp(self, n=1):
        """
        Exponential with power n
        exp(n) ->  exponentiation with base a and exponent n
        :param n: power (can be int, float, double, const or long)
        :return: exp(n)
        """
        self.result = self.pwr(Constants.e, n)
        print 'Exponential is: %f' % self.result
        return self.result
