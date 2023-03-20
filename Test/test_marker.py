# We have our source file in other folder so either we need to set PYTHONPATH or 
#insert the parent folder in the path by following way.
import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Src.bank import Bank, InSufficientBalance

@pytest.mark.positive
def test_deposit():
    b = Bank("Test Account", 10)
    assert b.balance == 10
    bal = b.get_balance()
    b.deposit(100)
    assert b.balance == bal + 100


    
    
