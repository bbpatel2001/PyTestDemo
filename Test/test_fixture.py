# We have our source file in other folder so either we need to set PYTHONPATH or 
#insert the parent folder in the path by following way.

import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Src.bank import Bank, InSufficientBalance

@pytest.fixture
def empty_bank_account():
    '''Returns a Bank instance with a account holder name and zero balance'''
    return Bank('')

@pytest.fixture
def bank():
    '''Returns a Bank instance with  account Holder name and  balance of 20'''
    return Bank('Xeevi Computer',20)


def test_holder_name(empty_bank_account):
    assert empty_bank_account.name == ''

def test_initial_amount(bank):
    assert bank.balance == 20
    
