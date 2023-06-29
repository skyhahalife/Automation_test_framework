# this file is to manage fixtures
import pytest

# fixture 参数中 ids: 可以通过 -k 来运行参数化中的一部分用例，ids 可以通过function来生成
@pytest.fixture(scope="function", autouse=False, params=["用户名称", "用户操作"], ids=["01", "02"], name="p_data")
def prepare_data(request):
    print("用例前 ")
    yield request.param
    print("用例后")
    pass


@pytest.fixture(scope="function", autouse=False)
def clean_yaml(request):
    print("clean yaml---- ")
    yield
    yaml_util.clean_yaml()
    pass
