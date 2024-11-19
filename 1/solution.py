def strict(func):
    def validator(a, b):
        if isinstance(a,(bool,float,str)) or isinstance(b,(bool,float,str)):
            raise TypeError
        else:
            return func(a, b)
    return validator


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError