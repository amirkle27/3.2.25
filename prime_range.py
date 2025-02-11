from Prime_Component import PrimeComponent
from typing import override

class PrimeRange(PrimeComponent):

    @override
    def prime_checker(self,number):
        if 10>number or number > 100:
            return f"The number {number} is out of range.\nPlease enter a number between 10 and 100!"
        else:
            return self.next.prime_checker(number)
