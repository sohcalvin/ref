import unittest
# import sys
# sys.path.append('.')
def list_of_tests_gen(s):
  for test in s:
    if unittest.suite._isnotsuite(test):
      yield test
    else:
      for t in list_of_tests_gen(test):
        yield t

import re, os
import unittest
from selenium import webdriver
class TestCase(unittest.TestCase) :
    def getEnvDriver(self) :
        driver = os.environ.get("DRIVER")
        driver = "chrome('../chromedriver.exe')"
        if(driver is None) : return None
        driver = re.sub(r'\"',"'",driver)
        ss= re.split(r'\s*\(\s*\'|\'\s*\)\s*',driver)
        driver_name = ss[0]
        driver_exe = ss[1]
        if(re.match("chrome$", driver_name, flags=re.IGNORECASE)) :
            return webdriver.Chrome(driver_exe)
        if(re.match("chrome$", driver_name, flags=re.IGNORECASE)) :
            return webdriver.PhantomJS(driver_exe)
        if(re.match("firefox$", driver_name, flags=re.IGNORECASE)) :
            return webdriver.Firefox(driver_exe)
        return None
unittest.TestCase = TestCase





if __name__ == "__main__":
    # unittest.main()
    # unittest.load_tests()

    # suite1 = unittest.TestLoader().loadTestsFromTestCase(GoogleDonkey)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(GoogleDonkey())
    #
    # alltests = unittest.TestSuite((suite1, suite2))
    # unittest.TextTestRunner(verbosity=2).run(alltests)
    # print(type(apple.__new__()))

    testloader = unittest.TestLoader()
    testSuites = testloader.discover(".")
    unittest.TextTestRunner(verbosity=2).run((testSuites))

    # for t in list_of_tests_gen(testSuites) :
    #     test_case_names = testloader.getTestCaseNames(t)
    #     suite = unittest.TestSuite()
    #     for n in test_case_names :
    #         atest = t.__class__(n)
    #
    #
    #         suite.addTest(atest)
    #     unittest.TextTestRunner(verbosity=2).run((suite))




    # testnames = testloader.getTestCaseNames(testJobmatcher.OpenSubmitFileForRecommendation)
    # suite = unittest.TestSuite()
    #
    # for name in testnames:
    #     print(">>>", name)
    #     atest = testJobmatcher.OpenSubmitFileForRecommendation(name)
    #     atest.driver = webdriver.Chrome('../chromedriver.exe')
    #     suite.addTest(atest)
    #
    # unittest.TextTestRunner(verbosity=2).run((suite))
