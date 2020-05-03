'''
exit_codes.py

Library that terminates python execution with an exit code. The purpose is to provide uniformity and make integration into Jenkins automation easier.
The exit code is determined by the test status, PASS, FAIL, USTABLE. The relationship between the status and exit code explained below:

    -A test script with a PASS status will exit with code 0
    -A test script with a FAIL status will exit with code 1
        -FAIL status implies a legitimate test-related failure
    -A test script with an UNSTABLE status will exit with code 2
        -UNSTABLE status implies a non-test related or infrastructure related failure

Usage:
    The exit code is based on a keyword.
        -If you want to exit with a status, pass a string of that status to the exit_codes.exit() method
            exit_codes.exit("FAIL")
            exit_codes.exit("FAILED")
            exit_codes.exit("PASS")
            exit_codes.exit("PASSED")
            exit_codes.exit("UNSTABLE")
            exit_codes.exit("pass")
            exit_codes.exit("Fail")
            exit_codes.exit("uNsTaBlE")
        -Note that case is ignored. Any test status that is passed will be transformed to upper case.
        -PASS and PASSED correspond to the same exit code, as does FAIL and FAILED
        -If a status does not exist in exit_codes, it will print an error, and exit UNSTABLE
'''

import sys

#Exit code dictionary
exit_codes = {
    "PASS": 0,
    "PASSED": 0,
    "FAIL": 2,
    "FAILED": 2,
    "UNSTABLE":1
}

def exit(test_status, verbose=True):
    test_status_upper = test_status.upper()
    #check if test status exists in exit_codes dict
    if test_status_upper not in exit_codes: #test_status does not exist, exit with UNSTABLE
        print('ERROR: "%s" is not a valid test status!' % test_status)
        sys.exit(exit_codes["UNSTABLE"])
    else:
        if verbose:
            print('Exiting test script execution with "%s" status' % test_status)
        sys.exit(exit_codes[test_status_upper])