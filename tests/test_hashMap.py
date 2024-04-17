import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.hashMap import HashTable

def test_getHash():
    table = HashTable()
    assert table.getHash('hello') == 32
    assert table.getHash('world') == 52

def test_setItem():
    # this also tests getItem
    table = HashTable()
    table['hello'] = 'world'
    assert table['hello'] == 'world'

def test_add():
    # this also tests get()
    table = HashTable()
    table.add('hello', 'world')
    assert table.get('hello') == 'world'

def test_delItem():
    table = HashTable()
    table['hello'] = 'world'
    del table['hello']
    assert table.get('hello') == None

def test_delete():
    table = HashTable()
    table.add('hello', 'world')
    table.delete('hello')
    assert table.get('hello') == None