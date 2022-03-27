def letters_generator():
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current)+1)

for letter in letters_generator():
    print(letter)


class Letters:
    def __init__(self, start='a', end='e'):
        self.start = start
        self.end = end
    def __iter__(self):
        return LetterIter(self.start, self.end)

def all_pairs(s):
    for item1 in s:
        for item2 in s:
            yield (item1, item2)

class LettersWithYield:
    def __init__(self, start='a', end='e'):
        self.start = start
        self.end = end
    def __iter__(self):
        next_letter = self.start
        while next_letter < self.end:
            yield next_letter
            next_letter = chr(ord(next_letter)+1)

class LetterIter:
    """An iterator over letters of the alphabet in ASCII order."""
    def __init__(self, start='a', end='e'):
        self.next_letter = start
        self.end = end
    def __next__(self):
        if self.next_letter == self.end:
            raise StopIteration
        letter = self.next_letter
        self.next_letter = chr(ord(letter)+1)
        return letter

class Positives:
    def __init__(self):
        self.next_positive = 1
    def __next__(self):
        result = self.next_positive
        self.next_positive += 1
        return result