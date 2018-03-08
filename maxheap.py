class MaxHeap:
    def __init__( self, maxSize ):
        self._elements = Array( maxSize +1)
        self._count = 1
    def __len__( self ):
        return self._count
    def capacity( self ):
        return len( self._elements)
    def add( self, value ):
        assertself._count < self.capacity(), "Cannot add to a full heap."   # Add the new value to the end of the list.
        self._elements[ self._count ] = value
        self._count += 1                     # Sift the new value up the tree.
        self._siftUp( self._count -1 )
    def _siftUp( self, ndx ):
        if ndx > 1:
            parent = ndx // 2
            if self._elements[ndx] > self._elements[parent]:
                tmp = self._elements[ndx]
                self._elements[ndx] = self._elements[parent]
                self._elements[parent] = tmpself._siftUp( parent )

