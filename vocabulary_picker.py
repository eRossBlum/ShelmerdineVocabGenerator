#!/usr/bin/env python3

# Word-classes: N = Noun, V = Verb, Adj = Adjective, Adv = Adverb, Oth = Other
from typing import List


def main() -> None:
    filters = solicit_criteria()
    vocab_list = load_vocab_list('./vocab_list.txt')
    filtered = filter_by_pos(filter_by_chapter(vocab_list, filters[0]), filters[1])
    for entry in filtered:
        print(f"Ch. {entry[0]}, {entry[1]}, {entry[2]}")


def solicit_criteria() -> tuple:
    print("What chapters do you want? \nType in the form \"beginning-end\" (e.g. \"5-7\". If you want only"
          "one chapter, just type the single number.\nIf you want all chapters, hit enter.")
    chap_text = input()
    if chap_text == '':
        chap_range = None
    else:
       # chap_range = range(*tuple(int(x) for x in chap_text.split('-'))) if '-' in chap_text else range(int(chap_text),
                                                                                                       # int(chap_text))
        chap_range = range(int(chap_text.split('-')[0]), int(chap_text.split('-')[1]) + 1)

    pos_text = input("Do you want any particular part of speech? If you want *all* parts of speech\n"
                     "hit enter. If you want a particular set, type in the letters here corresponding\n"
                     "to the parts of speech you want with spaces in between:\n"
                     "N: Noun\n"
                     "V: Verb\n"
                     "Adj: Adj\n"
                     "Adv: Adv\n"
                     "Prep: Preposition\n"
                     "Oth: Other\n"
                     "E.g. type \"N V Adv\" for Nouns, Verbs, and Adverbs:\n")
    if pos_text == '':
        desired_pos = None
    else:
        desired_pos = tuple(pos_text.upper().split(' '))
        #   print(chap_range, desired_pos)
    return chap_range, desired_pos


def load_vocab_list(path: str) -> List[tuple]:
    out_list = list()
    with open(path, encoding='utf-8') as file:
        for line in file:
            entry_as_strs = line.rstrip('\n').replace(' ', '').split(',')
            out_list.append((int(entry_as_strs[0]), entry_as_strs[1], entry_as_strs[2]))
  #  print(out_list)
    return out_list


def filter_by_chapter(vocab_list: List[tuple], chap_range: range) -> List[tuple]:
    if chap_range is None:
        return vocab_list
    out_list = list()
    for entry in vocab_list:
        #   print (entry[0], chap_range, entry[0] in chap_range)
        if entry[0] in chap_range:
            out_list.append(entry)
    return out_list


def filter_by_pos(vocab_list: List[tuple], desired_pos: tuple) -> List[tuple]:
    if desired_pos is None:
        return vocab_list
    out_list = list()
    for entry in vocab_list:
        if entry[2] in desired_pos:
            out_list.append(entry)
    return out_list


def sort_by_alph(vocab_list: List[tuple]) -> List[tuple]:
    return sorted(vocab_list, key=lambda x: x[[1]])


if __name__ == '__main__':
    main()
