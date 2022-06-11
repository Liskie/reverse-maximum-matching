from typing import Union, NoReturn

from tqdm import tqdm


class RMMSegmentor:

    def __init__(self):
        self.dictionary: list[str] = []
        self.load_dictionary()
        self.max_word_len = max(map(lambda word: len(word), self.dictionary))

    def load_dictionary(self) -> NoReturn:
        with open('dictionary/dict-small.txt', 'r') as dictionary_file:
            for line in dictionary_file:
                self.dictionary.append(line.strip().split()[0])

    def rmm(self, line: str) -> list[str]:
        chars = list(line.strip())
        words = []
        while chars:
            if len(chars) < self.max_word_len:
                current_chars = chars[:]
            else:
                current_chars = chars[len(chars) - self.max_word_len:]
            for i, _ in enumerate(current_chars):
                word = ''.join(current_chars[i:])
                if word in self.dictionary or i == len(current_chars) - 1:
                    words.insert(0, word)
                    for j in range(len(current_chars) - i):
                        chars.pop()
                    break
        return words

    def segment(self, text: Union[str, list[str]]) -> list[list[str]]:
        if isinstance(text, str):
            text = [text]
        elif isinstance(text, list):
            pass
        else:
            raise NotImplementedError

        segmented_lines = []
        for line in tqdm(text, desc='Segmenting: '):
            segmented_lines.append(self.rmm(line))

        return segmented_lines


if __name__ == '__main__':
    sample = '你好世界！我很爱你。中华人民共和国万岁！'
    segmentor = RMMSegmentor()
    print(segmentor.segment(sample))