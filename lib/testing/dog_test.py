#!/usr/bin/env python3


import io
import sys

class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog".'''
      
     
        
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
       
        sys.stdout = sys.__stdout__
        

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
      
        sys.stdout = sys.__stdout__
        

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
       
        sys.stdout = sys.__stdout__
       

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        

    def test_breed_not_in_list(self):
        '''prints "Breed must be in list of approved breeds." if not in breed list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        
        sys.stdout = sys.__stdout__
        
    def test_breed_in_list(self):
        '''saves breed if in breed list.'''
      
        