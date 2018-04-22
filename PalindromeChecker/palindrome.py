# code to check if input string is a palindrome


class Palindrome(object):
    # Class to handle palindrome logic

    @staticmethod
    def palindrome_check(n):
        return str(n) == str(n)[::-1]