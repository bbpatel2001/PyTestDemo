# We have our source file in other folder so either we need to set PYTHONPATH or 
#insert the parent folder in the path by following way.

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Src.bank import Bank, InSufficientBalance

def test_holder_name():
    b = Bank('py test', 10)
    assert b.name == 'Py Test'

def test_initial_amount():
    b = Bank('Xeevi Computer')
    assert b.balance == 0

def test_set_inital_amount():
    b =Bank('Xeevi Computer',100)
    assert b.balance == 100
    
