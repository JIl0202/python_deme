import pytest
from operator import itemgetter
from common.yaml_handler import config_yaml

keys = ['user1','user2','user3']
data = itemgetter(*keys)(config_yaml)


class Test_login:
    @pytest.mark.parametrize('user_info', data)
    def test_register_success(self, get_driver, user_info):
        info = itemgetter(*['username', 'password', 'email'])(user_info)
        username, password, reg_email = info
        driver = get_driver

