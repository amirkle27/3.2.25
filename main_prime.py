from Prime_Component import PrimeComponent
from prime_checker_2 import Prime2
from prime_checker_3 import Prime3
from prime_checker_5 import Prime5
from prime_checker_7 import Prime7
from prime_range import PrimeRange


chain7 = Prime7()
chain5 = Prime5()
chain3 = Prime3()
chain2 = Prime2()
chainPrimeRange = PrimeRange()
head = chainPrimeRange

chainPrimeRange.next = chain2
chain2.next = chain3
chain3.next = chain5
chain5.next = chain7
chain7.next = None # just for clarification


numbers = [12 ,17 ,23 ,100, 121,49,169]
for number in numbers:
    print(head.prime_checker(number))
    print()
