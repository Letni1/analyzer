import argparse
import sys
import os
from bs4 import BeautifulSoup
from bs4.element import Tag
from get_xpath import xpath_soup
from typing import TextIO, Optional


def get_features(doc: BeautifulSoup, tag_id: str) -> dict:
    elem = doc.find(id=tag_id)
    return elem.attrs


def count_max_matches(doc: BeautifulSoup, features: dict) -> Tag:
    match_dict = {}
    for k, v in features.items():
        elem = doc.find('a', {k: v})
        if elem:
            if elem not in match_dict:
                match_dict[elem] = 0
            match_dict[elem] += 1
    result = max(match_dict, key=match_dict.get)
    return result


def convert_to_bs4(doc: TextIO):
    file = open(doc, 'r')
    soup = BeautifulSoup(file.read(), features='html.parser', multi_valued_attributes=None)
    return soup


def gen_xpath(origin_file: BeautifulSoup, sample_file: BeautifulSoup, tag_id: Optional[str] = None):
    origin_file = convert_to_bs4(origin_file)
    sample_file = convert_to_bs4(sample_file)
    feats = get_features(origin_file, tag_id)
    element = count_max_matches(sample_file, feats)
    return xpath_soup(element)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_origin_file_path')
    parser.add_argument('input_other_sample_file_path')
    parser.add_argument('--id', help='optional id',
                            default='make-everything-ok-button')
    args = parser.parse_args()

    input_origin_file_path = args.input_origin_file_path
    input_other_sample_file_path = args.input_other_sample_file_path
    elem_id = args.id
    print(gen_xpath(input_origin_file_path, input_other_sample_file_path, elem_id))