from Prime_Component import PrimeComponent
from typing import override

class Prime2(PrimeComponent):

    # def __init__(self):
    #     super().__init__()
    #     self.number = None

    # def __init__(self):
    #     super().__init__()
    #     self.number = None

    @override
    def prime_checker(self,number:int):
        if number <= 1:
            return f"{number} is NOT Prime!"
        if number % 2 == 0:
            return f"{number} is NOT prime, It's divisible by 2!"
        if not number % 2 == 0:
            if self.next:
                return self.next.prime_checker(number)
            else:
                return f"{number} is Prime!!!"


        # for i in range (2,int(self.number ** 0.5 +1)):
        #     if self.number % i == 0:
        #         return f"{self.number} is devisable by {i}. It's NOT prime!. \n{self.number}/{i}= {self.number/i}"
        #
        # return f"{self.number} is prime!"


# number86 = CompositePrime(86)
# number87 = CompositePrime(87)
#
#
# print(number86.check_prime())
# print(number87.check_prime())