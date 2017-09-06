class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 2:
            return True
        if word[0].islower():
            return word == word.lower()
        else:
            if word[1].isupper():
                return word == word.upper()
            else:
                return word[1:] == word[1:].lower()
