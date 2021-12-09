""" unitTestExamples.py
    This is an example of using unit test with fixtures.
    
    Execute the following on the command line console:
    python -m unittest -q test_stock_ticker.Fundamental_TestFixtures
    
    
"""

__author__ = "Samuel Stephens"
__copyright__ = "Copyright 2021, TwoBarSlash LLC"
__credits__ = [""]
__license__ = "All Rights Reserved."
__version__ = "0.1"
__maintainer__ = "Samuel Stephens"
__email__ = "sam@twobarslash.com"
__status__ = "Developement"

import os, sys
import unittest
import inspect
from time import perf_counter, sleep
import logging

sys.path.extend([f'../{name}' for name in os.listdir("../") if os.path.isdir(f'../{name}')]) 

verbose = False

def logPoint(context, verbose=verbose):
    """ utility function used for module functions and class methods
        context:
        verbose:
    """
    callingFunction = inspect.stack()[1][3] 
    if type(context) == dict:
        logging.info(f"{context['context']} test time: {context['testtime']}")
    if globals()['verbose']: print ('in {} - {}()'.format(context, callingFunction))



def setUpModule():
    """  called once, before anything else in this module """

    # SET UP Ticker)
    print(f"Ticker:  {os.environ['ticker']}")

    logPoint(f'module {__name__}')

def tearDownModule():
    """ called once, after everything else in this module """
    # print(inspect.stack())
    logPoint(f'module {__name__}')

class Fundamental_TestFixtures(unittest.TestCase):
    """ """
    
    @classmethod
    def setUpClass(cls):
        """  called once, before any tests"""
        logPoint(f'class {cls.__name__}')

    @classmethod
    def tearDownClass(cls):
        """  called once, after all tests, if setUpClass successful """
        logPoint(f'class {cls.__name__}')

    def setUp(self):
        """  called multiple times, before every test method """
        self.tick = perf_counter()
        logPoint("setUp")

    def tearDown(self):
        """  called multiple times, after every test method """
        self.tock = perf_counter()
        diff = self.tock - self.tick
        print (f"{diff:.3f} s")
        logPoint({'testtime':f'{diff:.3f}s', 'context':os.environ['current_method']})

    def test_PE(self):
        """  TTX_UTJ See Page(1029), 8.3.5.8 TX Uncorrelated Total Jitter """
        TTX_UTJ_2p5GTs_Max = 100e-12 # seconds PP
        
        ## do work here, if you want retries you will have to 
        ## think about how to hadle setUps and Teardowns.

        result = 100e-12

        self.assertLessEqual(result, TTX_UTJ_2p5GTs_Max)
        self.logPoint()
    
    def get_beta_value(self):
        return 100e-12
    
    def test_beta(self):
        """
        High betas may mean price volatility over the near term, but they don't
        always rule out long-term opportunities.
        https://www.investopedia.com/investing/beta-know-risk/ 
        """
        beta = self.get_beta_value()
        print(f'beta_value = {beta}')    
        ## do work here, if you want retries you will have to 
        ## think about how to hadle setUps and Teardowns.

        result = 100e-12
        
        self.assertEqual(result, beta, msg="beta fail")
           
        
        self.logPoint()

    def test_parameter(self):
        """  TTX_UTJ See Page(1029), 8.3.5.8 TX Uncorrelated Total Jitter """
        TTX_UTJ_2p5GTs_Max = 100e-12 # seconds PP
        
        ## do work here, if you want retries you will have to 
        ## think about how to hadle setUps and Teardowns.

        result = 100e-12
        
        self.assertLessEqual(result, TTX_UTJ_2p5GTs_Max)
        
        self.logPoint()

    def logPoint(self, log_type=None):
        """ utility method to trace control flow. Logs that test was run and amount of
            time that test took.
        """
        callingFunction = inspect.stack()[1][3]
        callingClass = self.id().split('.')[1]
        message = f'Ran {callingClass}  {callingFunction}()'
        message = f'{message:<62}'
        logging.debug(message)
        os.environ['current_method'] =  message
        print (message, end="")


""" References
        https://pythontesting.net/framework/unittest/unittest-fixtures/
        https://www.askpython.com/python-modules/python-inspect-module
        https://www.internalpointers.com/post/run-painless-test-suites-python-unittest
        https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
        https://stackoverflow.com/questions/32899/how-do-you-generate-dynamic-parameterized-unit-tests-in-python
        https://pythonhosted.org/proboscis/
"""