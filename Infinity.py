class Infinity:
    """ An infinity object """
    def __lt__(_,__): return False
    def __le__(_,__): return isinstance(__, type(_)) or __ == float("inf")
    def __eq__(_,__): return isinstance(__, type(_)) or __ == float("inf")
    def __gt__(_,__): return True
    def __ge__(_,__): return isinstance(__, type(_)) or __ == float("inf")
