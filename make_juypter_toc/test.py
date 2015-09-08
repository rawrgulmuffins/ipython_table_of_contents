"""
"""
from make_juypter_toc import headers_to_table

def test_headers_to_tables_no_headers():
    table = headers_to_table(None, "test")
    assert table is None

def test_headers_to_tables_one_level_nesting():
    example_data = [
            u'#Introduction',
            u'#Why Flask?\n',
            u'#Topics Not Covered\n']
    table = headers_to_table(example_data, "test_name")
    expected_table = [
            u'* [Introduction](http://localhost:8888/notebooks/test_name#Introduction)',
            u'* [Why Flask?](http://localhost:8888/notebooks/test_name#Why-Flask?)',
            u'* [Topics Not Covered](http://localhost:8888/notebooks/test_name#Topics-Not-Covered)',]
    assert table == expected_table

def test_headers_to_tables_two_level_nesting():
    example_data = [
            u'#Introduction',
            u'##Why Flask?\n',
            u'#Topics Not Covered\n']
    table = headers_to_table(example_data, "test_name")
    expected_table = [
            u'* [Introduction](http://localhost:8888/notebooks/test_name#Introduction)',
            u'    * [Why Flask?](http://localhost:8888/notebooks/test_name#Why-Flask?)',
            u'* [Topics Not Covered](http://localhost:8888/notebooks/test_name#Topics-Not-Covered)',]
    assert table == expected_table

def test_headers_to_tables_three_level_nesting():
    example_data = [
            u'#Introduction',
            u'##Why Flask?\n',
            u'###Topics Not Covered\n',
            u'#Routes\n',]
    table = headers_to_table(example_data, "test_name")
    expected_table = [
            u'* [Introduction](http://localhost:8888/notebooks/test_name#Introduction)',
            u'    * [Why Flask?](http://localhost:8888/notebooks/test_name#Why-Flask?)',
            u'        * [Topics Not Covered](http://localhost:8888/notebooks/test_name#Topics-Not-Covered)',
            u'* [Routes](http://localhost:8888/notebooks/test_name#Routes)',]
    assert table == expected_table
