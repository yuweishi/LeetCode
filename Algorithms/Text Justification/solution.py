class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        n, res, start = len(words), [], 0
        while start < n:
            total, count = len(words[start]), 0
            #produce left justified text without extra space between words
            while start + count + 1 < n and total + count + len(words[start + count + 1]) + 1 <= maxWidth:
                total += len(words[start + count + 1])
                count += 1
            #if this's the last line, pad to right; otherwise add exrta space
            if start + count != n - 1 and count != 0:
                cur = words[start]
                base = (maxWidth - total) / count
                left = (maxWidth - total) % count
                for i in xrange(1, count + 1):
                    cur += " " * ((base + 1) if i <= left else base) + words[start + i]
            else:
                cur = " ".join(words[start: start + count + 1]) + " " * (maxWidth - total - count)
            res += [cur]
            start += count + 1
        return res
