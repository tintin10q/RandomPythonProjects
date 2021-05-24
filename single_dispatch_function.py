from functools import singledispatch


@singledispatch
def merge(first, second):
    return first + second


@merge.register
def _(first: list, second: list) -> list:
    first.extend(second)
    return first


@merge.register
def _(first: dict, second: dict) -> dict:
    return first | second


a = merge({'2': 'a'}, {'b': 'c'})
b = merge(2, 3)
c = [2]
d = [3,4]
merge(c, d)
print(c) # it doesn't have to return for merge I guess a deep copy is needed