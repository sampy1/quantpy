""" unitTestRunnerExample.py

    Example of how to process the .log file.
    Windows
    type results\<testrunner.log> | findstr /V "Path" | findstr "DATA"
    
    Unix
    cat results\<testrunner.log> | grep -v "Path" | grep "INFO"

"""
__author__ = "Samuel Stephens"
__copyright__ = "Copyright 2021, TwoBarSlash LLC"
__credits__ = [""]
__license__ = "All Rights Reserved."
__version__ = "0.1"
__maintainer__ = "Samuel Stephens"
__email__ = "sam@twobarslash.com"
__status__ = "Developement"

import sys, os
import unittest
import argparse
import logging
from time import perf_counter
import datetime
import uuid
import argparse

# uncomment for debug.
#import pdb # pdb.set_trace()

sys.path.extend([f'../{name}' for name in os.listdir("../") if os.path.isdir(f'../{name}')])

# general libraries
import common_routines as cr
from cli_interface import generic_cli

## import your test modules
from test_stock_ticker import Fundamental_TestFixtures


# allows for proper display.
cli = generic_cli()


#### Add tests to the test suite here ####
"""
The test_modules_to_run dictionary allow one to delineate which text Fixtures
and associated test should be loaded in a particular run.

The dictionary key is the class name where the list values are the test methods
that you want to call. Any particular list item can be '#'ed out.
"""
fixtures = {
    'Fundamental_TestFixtures':Fundamental_TestFixtures,
}

# List out modules and methods that will be run by defualt.
default_modules = {
        Fundamental_TestFixtures:
            [ "test_PE",
              "test_parameter",
              "test_beta"
            ],
}

parser = argparse.ArgumentParser()
parser.add_argument('-f','--fixture', help='specify which fixture to run')
parser.add_argument('-m','--method',  help='specify which method to run')
parser.add_argument('-l','--listit', action='store_true', help='list availible fixture and methods')
args = parser.parse_args()

if args.listit:
    """ This will create a menu and display to the user the availibe Fixtures and test methodes.
        basically a pretty print of the default_modules above.
    """
    cr.clear()
    for fixture in default_modules:
        menu_list = []
        for method in default_modules[fixture]:
            menu_list.append(method)
        menu = cli.make_tree(f"{fixture.__name__}", menu_list=menu_list)
        print(menu)
    sys.exit(0)

if args.fixture == None:
    """ Default set of test to run for PCIe.
    """
    tests_modules_to_run = default_modules

elif args.fixture and not args.method:
    print ("error on dependency, must specify a method")
    sys.exit(1)

else:
    print(args.fixture, args.method)
    tests_modules_to_run ={
        fixtures[args.fixture]: [args.method]
    }

# -------------- SETUP ENVIROMENT HERE ---------------- (Setup)

# Create uniqe data log sto save logged information in.
os.environ['datalog'] = './results/data_{:%Y%m%d_%H%M%S%f}.log'.format(datetime.datetime.now())
tickers = ['xom']
verbose = False

# -------------- SETUP LOG FILE HERE ---------------- (Setup)

# This configure file can only be set once at the beginning. 
# https://www.studytonight.com/python/python-logging-configuration
if not os.path.exists('results'): os.makedirs('results')
logging.basicConfig(level=logging.NOTSET, 
                    filename=os.environ['datalog'], # filename set above.
                    filemode='w', 
                    datefmt='%d-%b-%y,%H:%M:%S',
                    format='%(asctime)-15s,%(name)s,%(levelname)s,%(message)s',
                    )

# Default logging information.
logging.info("Date, Time, Username, Level, Info")
logging.error("Date, Time, Username, Level, Error")

# Example of methods to add information to the log file.
#logging.warning("test test")
#logging.info("my test")
#logging.debug("hello")
#logging.info("DATA: 1,2,3,4,5,6,7,8")

def logPoint(context, type='info'):
    # Reset all enviromental connditions here. ------------------------------------
    print(context)
    if type == 'info':
        logging.info(context)
    elif type == 'error':
        logging.error(context)
        
start_clock = perf_counter()
total_tests_runs = 0

for ticker in tickers:
    os.environ['ticker'] = str(ticker)
    
    logging.info(f"ticker: {os.environ['ticker']}")

    # initialize the test suite
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    # load modules and test
    for module in tests_modules_to_run:
        for test in tests_modules_to_run[module]:
            suite.addTests(loader.loadTestsFromName(test, module=module))

    # ------- logging info stored here.
    
    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=logging.NOTSET)
    result = runner.run(suite)
    
    #print((f"result: {dir(result)}"))
    
    print()
    for failure in result.failures:
        logPoint(f"{failure[0]}", type='error')
        for line in failure[1].split("\n"):
            logPoint(f"{line}", type='error')
    total_tests_runs = total_tests_runs + int(result.testsRun)

stop_clock = perf_counter()
total_time = stop_clock - start_clock



logPoint("TESTS COMPLETE".center(70, "="))
logPoint(f"Total Test Runs: {total_tests_runs}")
logPoint(f"Total Run Time: {total_time:.3f} s")
logPoint(f"OS:  {os.environ['OS']}")
logPoint(f"COMPUTERNAME:  {os.environ['COMPUTERNAME']}")
logPoint(f"Working Directory: {os.getcwd()}")
logPoint(f"Data Filename: {os.path.realpath(os.environ['datalog'])}")


#### Refernces / Cheets Sheets ####
#https://stackoverflow.com/questions/11662063/what-is-verbosity-level-exactly-in-pythondifference-between-each-level
# CRITICAL = 50 
# FATAL = CRITICAL
# ERROR = 40 
# WARNING = 30 
# WARN = WARNING
# INFO = 20 
# DEBUG = 10 
# NOTSET = 0
"""
https://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python
https://www.shellhacks.com/windows-grep-equivalent-cmd-powershell/
https://www.studytonight.com/python/python-logging-configuration
https://pythonexamples.org/python-datetime-format/
https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
https://exceptionshub.com/conditional-command-line-arguments-in-python-using-argparse.html
https://www.robvanderwoude.com/findstr.php#:~:text=Syntax%3A%20%20%20%2FB%20%20%20Matches%20pattern,file%20conta%20...%20%2014%20more%20rows%20
"""