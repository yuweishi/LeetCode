public class Vector2D {
    Iterator<List<Integer>> row;
    Iterator<Integer> col;
    public Vector2D(List<List<Integer>> vec2d) {
        row = vec2d.iterator();
        col = null;
    }

    public int next() {
        if (!hasNext()) return -1;
        return col.next();
    }

    public boolean hasNext() {
	//Use while instead of if in case of list contains empty list
        while (row.hasNext() && (col == null || !col.hasNext())) col = row.next().iterator();
        //check col != null, in case of the whole list is null/empty
	return col != null && col.hasNext();
    }
}

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i = new Vector2D(vec2d);
 * while (i.hasNext()) v[f()] = i.next();
 */
