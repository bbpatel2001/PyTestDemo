# We have our source file in other folder so either we need to set PYTHONPATH or 
#insert the parent folder in the path by following way.

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Src.bank import Bank, InSufficientBalance

def test_account_holder_name():
    b = Bank('py test', 10)
    assert b.name == 'Py Test'

