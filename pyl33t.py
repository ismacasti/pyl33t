#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pyl33t, a Python module to translate from annoying l33t text
#to a not so annoying English text.
#Tested on Python 2.7.6 and Python 3.3.3 in Linux i686
#Copyright 2013 Ismael Castiñeira.

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#Example l33t: 
#"!f_y0u_c4n_r34d_th15,_y0u_m16ht_b3_th3_1_w3’r3_l00k!n6_f0r ;)"

l33tReplacements = ( ('_1_', '_one_'), ('!', 'i'), ('0', 'o'), ('4', 'a'), ('3', 'e'), ('1', 'i'), ('5', 's'), ('6', 'g') )

def l33t2Plain(l33tText):
    plainText = l33tText
    for old, new in l33tReplacements:
        plainText = plainText.replace(old, new)
    
    return removeUnderscores(plainText)

def removeUnderscores(text):
    return text.replace('_', ' ')



if __name__ == "__main__":
    import sys
    try:
        print(l33t2Plain(sys.argv[1]))
    except IndexError:
        print("Usage: {} 'some annoying l33t text'".format(sys.argv[0]))





