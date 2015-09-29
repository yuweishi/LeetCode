class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        count, m, n, pre = 0, len(low), len(high), [[''], ['0', '1', '8']]
        if m > n or not m:
            return 0
        if m == 1:
            for char in '018':
                if not (char < low or 1 == n and char > high):
                    count += 1
        for i in range(2, n + 1):
            cur = []
            for num in pre[i % 2]:
                cur.append('0' + num + '0')
                cur.append('1' + num + '1')
                cur.append('6' + num + '9')
                cur.append('8' + num + '8')
                cur.append('9' + num + '6')
                if i == m or i == n:
                    for item in cur[-4:]:
                        if not (i == m and item < low or i == n and item > high):
                            count += 1
            if i > m and i < n:
                count += len(cur) * 4 / 5
            pre[i % 2] = cur
        return count
