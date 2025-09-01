# Typing & Modern Patterns------------------------------------------------------------------------------
# Type Hints
from typing import list, Dict

from rpds import List

Name = List[str]
Team = Dict[str, int]

def top(n: int, names: Name) -> Name:
    return names[:n]


print(top(2, ["Aadi", "Raj", "Mira"]))

#dataclasses & pydantic (runtime validation)------------------------------------------------------------------------------------------------

from dataclasses import dataclass

@dataclass
class User:
 name: str
 age: int


#Concurrency & Parallelism-------------------------------------------------------------
