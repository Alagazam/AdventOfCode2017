# pylint: disable=missing-docstring

class PassPhraseCheck:
    @staticmethod
    def is_pass_phrase_valid1(pass_phrase):
        wordlist = [word for word in pass_phrase.split(" ")]
        wordset = set(wordlist)
        return len(wordlist) == len(wordset)

    @staticmethod
    def is_pass_phrase_valid2(pass_phrase):
        wordlist = [''.join(sorted(word)) for word in pass_phrase.split(" ")]
        print(wordlist)
        wordset = set(wordlist)
        return len(wordlist) == len(wordset)

    @staticmethod
    def check_pass_phrases(pass_phrases):
        valid1 = 0
        valid2 = 0
        for row in pass_phrases:
            print(row)
            if PassPhraseCheck.is_pass_phrase_valid1(row):
                valid1 += 1
            if PassPhraseCheck.is_pass_phrase_valid2(row):
                valid2 += 1
        return valid1, valid2

if __name__ == '__main__':
    FILE = open("input.txt", "r")
    INDATA = FILE.read().splitlines()
    FILE.close()
    print("PassPhraseCheck1: " + str(PassPhraseCheck.check_pass_phrases(INDATA)))
