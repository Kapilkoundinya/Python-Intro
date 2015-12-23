"""
Calculator Application, with basic mathematical functionality
"""

import Calculator


def main():
    calculator = Calculator.Calculator()
    sumv = calculator.add(10, 20)
    sub = calculator.sub(10, 20)
    mul = calculator.mul()
    div = calculator.div(10, 100)
    pwr = calculator.pwr(3, 0.25)
    log = calculator.log(1,7)
    exp = calculator.exp(-1.5)

if __name__ == '__main__':
    main()

