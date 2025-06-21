# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    @classmethod
    def _flatten(cls, nestedList) -> Iterable[int]:
        for n in nestedList:
            if n.isInteger():
                yield n.getInteger()
            else:
                yield from cls._flatten(n.getList())
        
    def __init__(self, nestedList: [NestedInteger]):
        self._iter = self._flatten(nestedList)
        self._next = None
    
    def next(self) -> int:
        return self._next
    
    def hasNext(self) -> bool:
        try:
            self._next = next(self._iter)
        except StopIteration:
            return False
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())