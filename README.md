# CTestingScript
Python script to test stdin and stdout of C program
Script will compile c file and then run tests.

to run script type into terminal: python (python3) run_test.py 

Inside script file change:
  executable - name of testing C file 
  test_directory - directory where are test

Each test has its own folder where are stdin and stdout files.
Each test folder have to start with "test....."
stdin - testing input data
stdout - expected output
