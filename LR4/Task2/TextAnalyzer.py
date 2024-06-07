# -*- coding: utf-8 -*-

import re
import Task2.PasswordChecker as PasswordChecker
class TextAnalyzer:
    def __init__(self, filename):
        """Initializer of class"""
        self._text = None
        self._filename = filename

    def read_text(self):
        """Read text from file"""
        with open(self._filename, 'r', encoding='utf-8') as file:
            self._text = file.read()

    def count_sentences(self):
        """Count amount of sentences"""
        sentences = re.split(r'[.!?]', self._text)
        return len(sentences)

    def count_sentence_types(self):
        """Count types of sentences"""
        narration = len(re.findall(r'[^\.\?!]*(\.[^\.!?\n]*)', self._text))
        questions = len(re.findall(r'[^\.\?!]*(\?[^\.!?\n]*)', self._text))
        imperatives = len(re.findall(r'[^\.\?!]*(![^\.!?\n]*)', self._text))
        return narration, questions, imperatives

    def average_sentence_length(self):
        sentences = re.split(r'[.!?]', self._text)
        total_chars = 0
        total_sentences = len(sentences)
        for sentence in sentences:
            cleaned_sentence = re.sub(r'[^\w\s]', '', sentence)
            total_chars += len(cleaned_sentence)

        if total_sentences > 0:
            return total_chars / total_sentences
        else:
            return 0

    def average_word_length(self):
        words = re.findall(r'\b\w+\b', self._text)
        total_chars = sum(len(word) for word in words)
        return total_chars / len(words)

    def count_smiles(self):
        smiles = re.findall(r'[:;]-*[\(\)\[\]]+', self._text)
        return len(smiles)

    def find_words_with_uppercase_symbols(self):
        words = re.findall(r'\b[A-Z]+\d+[A-Z]*\b', self._text)
        return words

    def count_words_in_each_line(self):
        lines = self._text.split('\n')
        _str = ""
        i = 1
        for line in lines:
            words = re.findall(r'\b\w+\b', line)
            _str += f"Line {i}: Number of words = {len(words)}\n"
            i += 1
        return _str

    def find_longest_word(self):
        #lines = self._text.split('\n')
        words = re.findall(r'\b\w+\b', self._text)
        longest_word = max(words, key=len)
        i = 1
        for word in words:
            if word == longest_word:
                return longest_word, i
            i += 1
        return 0, 0
    def print_even_words(self):
        lines = self._text.split('\n')
        _str = ""
        for i, line in enumerate(lines, 1):
            words = re.findall(r'\b\w+\b', line)
            for j, word in enumerate(words, 1):
                if j % 2 == 0:
                    _str += f"Line {i}, Word {j}: {word} \n"
        return _str

    def save_results_to_file(self, output_filename):
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write("Количество предложений в тексте:" + str(self.count_sentences()) + "\n")
            file.write("Количество повествовательных предложений:" + str(self.count_sentence_types()[0])+"\n")
            file.write("Количество вопросительных предложений: " + str(self.count_sentence_types()[1]) + "\n")
            file.write("Количество побудительных предложений: " + str(self.count_sentence_types()[2]) + "\n")
            file.write("Средняя длина предложения: " + str(self.average_sentence_length()) + " символов\n")
            file.write("Средняя длина слова: " + str(self.average_word_length()) + " символов\n")
            file.write("Количество смайликов: " + str(self.count_smiles()) + "\n")
            file.write("Слова с сочетанием букв верхнего регистра и цифр:\n")
            for word in self.find_words_with_uppercase_symbols():
                file.write(word + "\n")
            words = re.findall(r'\b\w+\b', self._text)
            first_word = words[0] if words else ""
            file.write("Надежность пароля для первого слова: " + PasswordChecker.PasswordChecker.check_strength(first_word) + "\n")
            file.write("Количество слов в строке: " + self.count_words_in_each_line() + "\n" )
            longest_word, i = self.find_longest_word()
            file.write("Самое длинное слово: " + str(longest_word) + ", и его порядковый номер: " + str(i) + "\n")
            file.write("Вывести каждое четное слово: " + self.print_even_words())
