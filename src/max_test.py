import json
import os
import allure
import pytest
from yaml_util import YamlUtil
import requests


env = 'prod'
# env = 'test'

def max(values):
    _max = values[0]
    for val in values:
        if val > _max:
            _max = val
    return _max


def min(values):
    _min = values[0]
    for val in values:
        if val < _min:
            _min = val
    return _min


@allure.feature("TestClass 测试类")
class TestClass:

    @staticmethod
    def setup_class():
        print("Start Test Class")

    @staticmethod
    def teardown_class():
        print("End Test Class")

    # Test environment return token and so on
    @pytest.mark.skipif(env != 'prod', reason='This is product environment')
    def test_01(self):
        # business logical code
        print("This is test_01")
        #
        assert 1 == 1
        # return the information you need
        return print("after assert")

    @pytest.mark.skipif(env != 'test', reason='This is test environment')
    def test_02(self):
        print("This is test_02")

    @pytest.mark.smoke
    def test_03(self):
        print("This is test_03")

    @allure.issue("https://www.baidu.com", "这是一个bug需要修复")
    @allure.severity(allure.severity_level.NORMAL)
    def test_04(self):
        print("This is test_04")

    @allure.story("link test")
    @allure.link("https://www.baidu.com", name="百度")
    def test_05(self):
        print("This is test_05")

    @allure.story("link test")
    @allure.testcase("https://www.baidu.com", name="测试用例")
    def test_06(self):
        print("This is test_06")

    # 改变默认执行顺序 注解不能控制执行顺序，
    # 如果未生效，原因可能为当前python环境未安装pytest-ordering
    @pytest.mark.run(order=1)
    def test_07(self):
        print("This is test_07")

    @pytest.mark.skip
    def test_min(self):
        values = (2, 3, 1, 4, 6)
        val = min(values)
        assert val == 1

    @allure.story("模拟测试用例失败")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_max(self):
        allure.attach("<body>这是一个attach测试</body>", name='attach测试', attachment_type=allure.attachment_type.HTML)
        values = (2, 3, 1, 4, 6)
        val = max(values)
        assert val == 5

    # "prepare_date" 该fixture 已有别名 "p_data"，不能用原来的方法名引用
    def test_fixture(self, p_data):
        print("prepared date:", p_data)

    @pytest.mark.parametrize("case_info", YamlUtil().read_yaml("./get_token.yaml"))
    @pytest.mark.smoke
    def test_data_drive(self, case_info):
        json.dumps(case_info)
        method = case_info["request"]["method"]
        url = case_info["request"]["url"]
        response = requests.request(method, url)
        assert response.status_code == case_info["validate"]["code"]


if __name__ == '__main__':
    #pytest.main(['-vs'])
    # pytest.main(['-vs', './max_test.py', '--alluredir', './temp'])
    # # http://localhost:63342/xxxxxx/src/reports/index.html
    # # 1）allure-pytest插件：2）allure工具：3）allure工具需要java jdk：
    # os.system('allure generate ./temp -o ./reports --clean')
    # print("http://localhost:63342/Automation_test_framework/src/reports/index.html")

    # 如果pytest.main()中传入的参数没生效，并且修改了默认运行为pytest，
    # 右键运行时默认运行了当前文件的所有用例，因为程序识别到了pytest框架，
    # 默认pytest运行，如果main主函数运行，需要修改python解释器配置
    pytest.main(['-vs', './max_test.py', '-m', 'smoke'])

    # pytest.main(['-vs','./maxtest.py'])
