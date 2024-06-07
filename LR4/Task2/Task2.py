# -*- coding: utf-8 -*-
import Task2.TextAnalyzer as TextAnalyzer
import zipfile

def general_func():
    """General function that is used in main.py"""

    text_analyzer = TextAnalyzer.TextAnalyzer('Task2/input.txt')
    text_analyzer.read_text()
    text_analyzer.save_results_to_file('Task2/output.txt')

    with zipfile.ZipFile('Task2/result_archive.zip', 'w') as zip_file:
        zip_file.write('Task2/output.txt')

    print('Результаты анализа сохранены в файл output.txt и архивированы в result_archive.zip')
