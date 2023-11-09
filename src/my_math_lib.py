class simple_math_lib:
    
    def add(self, *args):

        total = 0

        for n in args:
            total += n

        return total
    
    def multiply(self, *args):
        product = 1

        for n in args:
            product *= n

        return product
    