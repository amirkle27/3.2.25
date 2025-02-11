from Prime_Component import PrimeComponent
from typing import override


class Prime3(PrimeComponent):

    @override
    def prime_checker(self, number):
        if number <= 1:
            return f"{number} is NOT Prime!"
        if number % 3 == 0:
            return f"{number} is NOT prime, it's divisible by 3!"
        if not number % 3 == 0:
            if self.next:
                return self.next.prime_checker(number)
            else:
                return f"{number} is Prime!"