def isPalindrome(self, s: str):
        test_str = ''.join(letter for letter in s if letter.isalnum())
        test = test_str.lower()
        strg = test[::-1]
        if strg == test:
            return True
        else:
            return False