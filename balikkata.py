# -*- coding: utf-8 -*-
"""Balikkata

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tBFX4O_iNKLqINrOdLvxhD88lSDdgwPJ
"""

def reverse(s):
    if len(s)<2:
        return s

    first,rest = s[0],s[1:]
    return reverse (rest)+first

reverse('kasur')