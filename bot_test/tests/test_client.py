#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 14:33
# @Author  : Smile_Mr
# @File    : test_client.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 14:42
# @Author  : Smile_Mr
# @File    : test_api.py
import pytest
from tools.AssertHandle import assert_handle
from tools.RquestHandle import RequestHandle

global_data = None

class Testdata:

    def test_start(self, autotest, write_book):

        # if autotest.get('row', None):
        #
        #     row = autotest['row']
        #     result = 'Pass'
        #     actual_result = None
        #     try:
        #         response = RequestHandle(autotest).get_response()
        #         actual_result = response.json()
        #         assert assert_handle(actual_result, autotest['Expect'], autotest['Validate_Type'])
        #     except Exception as e:
        #         result = 'Fail'
        #         raise AssertionError(e)
        #     finally:
        #         write_book.write_back_result(row, str(actual_result), result)
        # else:
        act_data = autotest['steps']
        for autotest in act_data:

            row = autotest['row']
            result = 'Pass'
            actual_result = None
            try:
                response = RequestHandle(autotest,global_data).get_response()
                actual_result = response.json()
                if actual_result['result'].get('version'):
                    global global_data
                    global_data = actual_result['result'].get('version')

                assert assert_handle(actual_result, autotest['Expect'], autotest['Validate_Type'])
            except Exception as e:
                result = 'Fail'
                raise AssertionError(e)
            finally:
                write_book.write_back_result(row, str(actual_result), result)


if __name__ == '__main__':
    pytest.main(['-s', 'test_client.py', '--project_name', 'client'])

