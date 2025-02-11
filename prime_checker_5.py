from Prime_Component import PrimeComponent
from typing import override


class Prime5(PrimeComponent):

    @override
    def prime_checker(self, number):
        if number <= 1:
            return f"{number} is NOT Prime!"
        if number % 5 == 0:
            return f"{number} is NOT prime, It's divisible by 5!"
        if not number % 5 == 0:
            if self.next:
                return self.next.prime_checker (number)
            else:
                return f"{number} is Prime!"