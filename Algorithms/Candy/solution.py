class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        #Method 1: go through twice
        if not ratings:
            return 0
        n, new = len(ratings), [1]
        for i in xrange(1, n):
            new += [1 if ratings[i] <= ratings[i - 1] else new[i - 1] + 1]
        sum = new[-1]
        for i in xrange(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                new[i] = max(new[i], new[i + 1] + 1)
            sum += new[i]
        return sum

	#Method 2: one traverse
        if not ratings: return 0
        total, up, down = 1, 1, 0
        for i in xrange(1, len(ratings)):
            if ratings[i] >= ratings[i-1]:
                if down:
                    total += down * (down + 1) / 2
                    if down >= up:#peak should be (down + 1) other than up
                        total += down + 1 - up
                    down = 0
                    up = 1
                up = 1 if ratings[i] == ratings[i-1] else up + 1
                total += up
            else:
                down += 1
        if down:
            total += down * (down + 1) / 2
            if down >= up: total += down + 1 - up
        return total
