# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uXSVR3Yho3F22hTi0nxxbdGJLlzpEaV8
"""

import math
#import sys

image_input = [1.32, 0.12, -1.44, 0.32, 0.15, 0.61, 0.87, 1.109, 0.201]#, 245] #, 98, 23, 4, 56, -1, 23, 35, 45, 21, 6, -87, 9, 45, 125, 19]
print('Input size: ' + str(len(image_input)))
weight = [1.2313, 0.6542, 1.23145, -0.54123, 0.31451, 0.132, 1.231, -0.4, -0.451200, -1.0, 0.231, 0.51, -1.64, 1.8522, -1.452, 1.123, -0.254, 0.5878, 1.253, 1.58, -0.898, 0.35, -0.5856, -0.455, 0.685, 0.5874, 0.367]
teste2 = [1.253, 1.58, -0.898, 0.35, -0.5856, -0.455, 0.685, 0.5874, 0.367]
teste = [-1.0, 0.231, 0.51, -1.64, 1.8522, -1.452, 1.123, -0.254, 0.5878]
print('Weight size: ' + str(len(weight)))

total = 0
for i in range(9):
  total = total + (float(image_input[i]) * float(teste2[i]))
print('Dot product: ' + str(total))

'''if len(sys.argv) != 2:
    print('Invalid amount of arguments.')
    print('Syntax: python3 FloatToBin.py \n\t\t<-t: Print on terminal | -o: Make bitList.txt file>')
    sys.exit()'''

print('-' * 50)
print('Codificador de Ponto Fixo')
print('Versao Beta 1.0')
print('-' * 50)
print('')

def float_bin(number, places = 32):
    
    if number < 0.0:
        signal = True
        number = abs(number)
    else:
        signal = False

    whole, dec = str(number).split('.')
    
    whole = int(whole)
    dec = int(dec)
    res = bin(whole).lstrip("0b") + '.'
    for x in range(places):
        whole, dec = decimal_converter(dec)
        dec = int(dec)
        res += whole
    
    res = res.split('.')
    if len(res[0]) != 3:
      res[0] = ('0' * (3-len(res[0]))) + res[0]
    parcial = res[0] + res[1]
    if signal == True:
      return complement_two(parcial)
    else:
      return parcial

def complement_two(num):
    not_num = ''
    complement = ''
    carry = False

    for bit in num:
      if bit == '1':
        not_num = '0' + not_num
      elif bit == '0':
        not_num = '1' + not_num
      else:
        not_num = bit + not_num
    
    if not_num[0] == '1':
      complement = '0'
      carry = True
      for bit in not_num[1:]:
        if carry == True:
          if bit == '1':
            complement = '0' + complement
            continue
          elif bit == '0':
            complement = '1' + complement
            carry = False
            continue
          elif bit == '.':
            complement = bit + complement
        else:
            complement = bit + complement
    if not_num[0] == '0':
      complement = '1'
      for bit in not_num[1:]:
        complement = bit + complement
    
    #print(complement)
    return complement

def decimal_converter(num):
    while num > 1:
        num /= 10
    str_num = ( str(num * 2) + '.0').split('.')
    return str_num[0], str_num[1]

def result(num):
    result = float_bin(num, 8)
    result = result.split('.')

    if len(result[0]) != 8:
        result[0] = ('0' * (8 - len(result[0]))) + result[0]  
    return (result[0] + '.' + result[1])
    #return (result[0] + result[1])

def main():    
    #print('Input coding: ')
    for each_input in image_input:
      #print(str(each_input) + ': ' + float_bin(float(each_input)) )
      print(float_bin(float(each_input)))
    print('-' * 50)

    #print('Weight coding: ')
    for each_weight in weight:
      #print(str(each_weight) + ': ' + float_bin(float(each_weight)))
      print(float_bin(float(each_weight)))
    print('-' * 50)

if __name__ == '__main__':
    main()