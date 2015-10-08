class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dict = collections.defaultdict(set)
        for word in dictionary:
            unify = word[0] + str(len(word) - 2) + word[-1]
            self.dict[unify].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        unify = word[0] + str(len(word) - 2) + word[-1]
        return len(self.dict[unify]) == int(word in self.dict[unify])


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
