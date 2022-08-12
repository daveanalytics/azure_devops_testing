{"cells":[{"cell_type":"code","source":["# COMMAND -------------------\n\n# MAGIC %run ./main_tests_run\n\n# COMMAND -------------------\n\ndef run_tests():\n    test_classes_to_run = [MainUnitTests]\n    loader = unittest.TestLoader()\n    suites_list = []\n    for test_class in test_classes_to_run:\n        suite = loader.loadTestsFromTestCase(test_class)\n        suites_list.append(suite)\n        \n    all_suite = unittest.TestSuite(suites_list)\n    \n    runner = xmlrunner.XMLTestRunner(output=\"/dbfs/\")\n    runner.run(all_suite)\n    \nrun_tests()"],"metadata":{"application/vnd.databricks.v1+cell":{"title":"","showTitle":false,"inputWidgets":{},"nuid":"40c45064-3450-4f8f-9034-e2e42738d18e"}},"outputs":[],"execution_count":0},{"cell_type":"code","source":[""],"metadata":{"application/vnd.databricks.v1+cell":{"title":"","showTitle":false,"inputWidgets":{},"nuid":"d6b88cb9-daf2-4648-9951-69b760d77904"}},"outputs":[],"execution_count":0}],"metadata":{"application/vnd.databricks.v1+notebook":{"notebookName":"main_tests_run","dashboards":[],"notebookMetadata":{"pythonIndentUnit":4},"language":"python","widgets":{},"notebookOrigID":2418566750380705}},"nbformat":4,"nbformat_minor":0}
