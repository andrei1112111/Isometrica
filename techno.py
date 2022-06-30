from dataclasses import dataclass, KW_ONLY, asdict
from typing import TypeAlias


def sum_numbers(number1: int | float, number2: int | float) -> float | int:
    return sum([number1, number2])


print(sum_numbers(1, 1.1))
#


@dataclass
class Point:
    x: int | float
    y: int | float
    n: KW_ONLY = 1


a = Point(1, 1)
try:
    b = Point(1, 1, 2)
except Exception:
    pass
print(a.x)
print(asdict(a))
#
FileName: TypeAlias = str
file: FileName = 'nna.py'


#
def check(s: int) -> int:
    return s // 2


k = 10
if (x := check(k)) >= 0:
    print(x)
#
