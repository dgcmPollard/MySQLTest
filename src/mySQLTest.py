'''
Created on Mar 23, 2012
Test for MySQL access, data in/out of TestValDb
and NumPy, SciPy functionality
@author: dpollard2
'''

#import sys
import mySQLLib as dbf


if __name__ == '__main__':
    print("\nHello World from python")
    
    dbf.test_numpy()
    dbf.test_scipy()
    dbf.test_mysql()
    