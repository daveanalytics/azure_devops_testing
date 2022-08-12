# Databricks notebook source
# COMMAND -------------------

# MAGIC %run ./main_tests_run

# COMMAND -------------------

def run_tests():
    test_classes_to_run = [MainUnitTests]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
        
    all_suite = unittest.TestSuite(suites_list)
    
    runner = xmlrunner.XMLTestRunner(output="/dbfs/")
    runner.run(all_suite)
    
run_tests()

# COMMAND ----------


