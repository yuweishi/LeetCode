// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
class PeekingIterator implements Iterator<Integer> {
    Iterator<Integer> iter;
    int peeknum;
    boolean hasPeek;
	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    iter = iterator;
	    hasPeek = false;
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        if (!hasPeek) {
            hasPeek = true;
            peeknum = iter.next();
        }
        return peeknum;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    if (hasPeek) {
            hasPeek = false;
            return peeknum;
        }
        return iter.next();
	}

	@Override
	public boolean hasNext() {
	    return (hasPeek || iter.hasNext());
	}
}
