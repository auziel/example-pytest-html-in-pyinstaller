import os
import sys
import pytest 

def calc(a, b):
    return a+b


def resource_path(relative):
    """
    pyinstaller unpacks data into a temporary folder, 
    and stores this directory path in the _MEIPASS environment variable.
    
    relative - name of the resource
    """
    try:
        if getattr(sys, 'frozen') and hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative)
    except:
        return os.path.join(os.path.abspath("."), relative)


if __name__ == "__main__":
    test_module = resource_path("tests")
    print("Running tests, tests_file = {}".format(test_module))
    pytest.main(["-vvv", "-p", 
                "pytest_html", 
                "--html=report.html", 
                "--self-contained-html", 
                "--capture=tee-sys", 
                "--junitxml=report.xml", test_module])

