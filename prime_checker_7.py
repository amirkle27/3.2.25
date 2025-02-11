from Prime_Component import PrimeComponent
from typing import override


class Prime7(PrimeComponent):

    @override
    def prime_checker(self,number):
        if number <= 1:
            return f"{number} is NOT Prime!"
        if number % 7 == 0:
            return f"{number} is NOT prime, It's divisible by 7!"
        if not number % 7 == 0:
            if self.next:
                return self.next.prime_checker(number)
            else:
                return f"{number} is Prime!"