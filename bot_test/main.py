if __name__ == '__main__':

    import pytest,os
    pytest.main(['-q','./tests/test_api.py','--alluredir','./report/allure_report','--project_name','scello-9100','--html','./report/html_report/report.html'])
    pytest.main(['-q','./tests/test_api.py','--alluredir','./report/allure_report','--project_name','DM','--html','./report/html_report/report.html'])
    pytest.main(['-q','./tests/test_api.py','--alluredir','./report/allure_report','--project_name','client','--html','./report/html_report/report.html'])
    pytest.main(['-q','./tests/test_api.py','--alluredir','./report/allure_report','--project_name','scello-9106','--html','./report/html_report/report.html'])
    pytest.main(['-q','./tests/test_api.py','--alluredir','./report/allure_report','--project_name','pranbo','--html','./report/html_report/report.html'])
    pytest.main(['-q','./tests/test_api.py','--alluredir','./report/allure_report','--project_name','scello','--html','./report/html_report/report.html'])
    pytest.main(['-q','./tests/test_api.py','--alluredir','./report/allure_report','--project_name','scello-9101','--html','./report/html_report/report.html'])
    pytest.main(['-q','./tests/test_api.py','--alluredir','./report/allure_report','--project_name','scello-DM','--html','./report/html_report/report.html'])
    # pytest.main(['-q','./tests/test_api.py','--alluredir','./report/allure_report','--project_name','api','--html','./report/html_report/report.html'])
    os.system('allure serve ./report/allure_report')
