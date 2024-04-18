import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.hashTable_linearProbing import HashTable

def test_getItem():
    table = HashTable()
    table['hello'] = 'world'
    assert table['hello'] == 'world'

def test_setItem():
    table = HashTable()
    table["march 6"] = 20
    table["march 17"] = 88
    assert table["march 6"] == 20
    assert table["march 17"] == 88

def test_setItemCollision():
    table = HashTable()
    table["march 6"] = 20
    table["march 17"] = 88
    table["march 17"] = 29
    assert table["march 6"] == 20
    assert table["march 17"] == 29

def test_linearProbing():
    table = HashTable()
    table["march 6"] = 20
    table["march 17"] = 88
    table["march 17"] = 29
    table["nov 17"] = 1
    table["dec 17"] = 33
    table["march 33"] = 233
    table["march 33"] = 29
    assert table["march 6"] == 20
    assert table["march 17"] == 29
    assert table["nov 17"] == 1
    assert table["dec 17"] == 33