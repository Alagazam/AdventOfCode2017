# pylint: disable=missing-docstring

class PassPhraseCheck:
    @staticmethod
    def is_pass_phrase_valid(pass_phrase):
        wordlist = [word for word in pass_phrase.split(" ")]
        wordset = set(wordlist)
        return len(wordlist) == len(wordset)

    @staticmethod
    def check_pass_phrases(pass_phrases):
        valid = 0
        for row in pass_phrases:
            print(row)
            if PassPhraseCheck.is_pass_phrase_valid(row):
                print("   VALID")
                valid += 1
        return valid

if __name__ == '__main__':
    FILE = open("input.txt", "r")
    INDATA = FILE.read().splitlines()
    FILE.close()
    print("PassPhraseCheck1: " + str(PassPhraseCheck.check_pass_phrases(INDATA)))
