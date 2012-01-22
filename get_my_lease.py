# -*- coding: utf-8 -*-
import sys
import argparse

parser = argparse.ArgumentParser(description='Calculate new property lease amount.')
parser.add_argument('-v', '--vecchio_canone', required=True, type=float, help='e.g. 1000.00')
parser.add_argument('-m', '--mesi_canone', required=True, type=int, help='e.g. 3')
parser.add_argument('-i', '--istat', required=True, type=float, help='e.g. 2.1')
parser.add_argument('-f', '--frazioneistat', required=True, type=float, help='e.g. 0.75')
parser.add_argument('-c', '--mesi_cauzione', required=True, type=int, help='e.g. 3')

args = parser.parse_args()

istatreale = args.istat*args.frazioneistat 


nuovo_canone=args.vecchio_canone*(1+istatreale/100)
adeguamento_cauzione=args.vecchio_canone*(istatreale/100)*(args.mesi_cauzione/args.mesi_canone)
tassa_di_registro=nuovo_canone*.02*(12/args.mesi_canone)

str = 'a trimestre' if ( args.mesi_canone==3 ) else 'al mese'
print 'Nuovo canone: €%.2f %s' % (nuovo_canone,str)
print 'Adeguamento cauzione: €%.2f' % adeguamento_cauzione
print 'Tassa di registro: €%.2f' % tassa_di_registro 
