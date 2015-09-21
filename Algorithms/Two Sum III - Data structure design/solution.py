class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.dict = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.dict:
            self.dict[number] += 1
        else:
            self.dict[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        dict = self.dict
        for k in dict:
            if value - k in dict and (k != value - k or dict[k] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
