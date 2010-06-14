import unittest

def suite():
	modules = ['connection', 'transaction', 'logging']
	alltests = unittest.TestSuite()
	for module in map(__import__, modules):
		alltests.addTest(unittest.findTestCases(module))
		
	return alltests

if __name__ == "__main__":
	unittest.main(defaultTest="suite")