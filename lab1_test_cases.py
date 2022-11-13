# Test cases for Lab1: http://lanlab.org/course/2022f/ooad/Lab1/Lab1.pdf
#
# Note: Your Journal implementation should at least pass the following test cases.
# You are welcome to come up with more distinct test cases. Importantly, you must
# test the case (manually) where there are two diary entries, one from today and another from
# yesterday.  Make sure the today property returns only today's diary entry.
#
# Please run this script in the command line using the following command:
#
#   python -m pytest lab1_test_cases.py
#
# Copyright (c) Hui Lan 2020
# Last modified on 17 Nov 2021

from lab1 import *
# import os
import pytest

# Test cases for class Journal

def test_case_01():
    ''' Normal case -- one entry '''
    remove_file('hui-journal-01.sqlite3')
    j = Journal('hui-journal-01.sqlite3')
    j.today = 'Visited Pujiang County.'
    assert j.today == 'Visited Pujiang County.'
    
def test_case_02():
    ''' Normal case -- two entries '''
    remove_file('hui-journal-02.sqlite3')
    j = Journal('hui-journal-02.sqlite3')
    j.today = 'Visited Pujiang County.'
    j.today = 'Visited Wuyi County.'
    assert j.today == 'Visited Pujiang County.\nVisited Wuyi County.'

def test_case_03():
    ''' Normal case -- many entries '''
    remove_file('hui-journal-03.sqlite3')
    j = Journal('hui-journal-03.sqlite3')
    expected_result = ''
    for i in range(100):
        j.today = 'Wrote %d.' % (i)
        expected_result += 'Wrote %d.\n' % (i)
    assert j.today == expected_result.rstrip()

def test_case_04():
    ''' Undesired event --  diary entry is an empty string.'''
    remove_file('hui-journal-04.sqlite3')
    j = Journal('hui-journal-04.sqlite3')
    j.today = ''
    assert j.today == None


def test_case_05():
    ''' Undesired event --  diary entry is a number.'''
    remove_file('hui-journal-05.sqlite3')
    j = Journal('hui-journal-05.sqlite3')
    j.today = 123
    assert j.today == None


def test_case_06():
    ''' test that deleter works '''
    remove_file('hui-journal-06.sqlite3')
    j = Journal('hui-journal-06.sqlite3')
    j.today = 'Visited Pujiang County.'
    with pytest.raises(EntryNotFoundError, match='No diary entry'):
        del j.today
        assert j.today