def input_string():
    """This function is the entry point in this module (task 4, variant 30). The function displays comments
                 for the user and also calls functions to execute the task."""
    print("Task 4 (30):\n"
          "а) определить, сколько слов имеют максимальную длину;\n"
          "б) вывести все слова, за которыми следует запятая или точка;\n"
          "в) найти самое длинное слово, которое заканчивается на 'е'\n")
    text = ""
    print("Do you want to input text? (y/n):")
    if input("Input answer(y/n): ") == "y":
        text = input("Input text: ")
    else:
        text = ("So she was considering in her own mind, as well as she could, \n"
                "for the hot day made her feel very sleepy and stupid, whether \n"
                "the pleasure of making a daisy-chain would be worth the trouble \n"
                "of getting up and picking the daisies, when suddenly a White Rabbit \n"
                "with pink eyes ran close by her.")
    print(f"Your text is:\n{text}\n")
    max_len_task(text)
    words_with_punctuation(text)
    the_longest_word_ends_with_e(text)


def max_len_task(text):
    """This function determines how many words of the transmitted text have the maximum length."""
    strings = text.split()

    arr_with_len = []
    for str in strings:
        if(str.endswith(",") or str.endswith(".")):
            arr_with_len.append(len(str)-1)
        else: arr_with_len.append(len(str))

    max_len_count = arr_with_len.count(max(arr_with_len))

    print(f"a) {max_len_count} words have max len")


def words_with_punctuation(text):
    """This function outputs all words and transmitted text followed by a comma or period."""
    strings = text.split()
    print("b) words followed by a comma or period:")
    for str in strings:
        if str.endswith(".") or str.endswith(","):
            print(str[:len(str)-1:])


def the_longest_word_ends_with_e(text):
    """This function finds and outputs the longest word in the passed text that ends with 'e'."""
    print("c) Words with max length and ends with \'e\':")
    text = text.replace(',', '')
    text = text.replace('.', '')
    strings = text.split()
    words_with_e = []
    arr_with_lens = []
    for string in strings:
        if string.endswith("e"):
            words_with_e.append(string)
            arr_with_lens.append(len(string))

    for string in words_with_e:
        if len(string) == max(arr_with_lens):
            print(string)

