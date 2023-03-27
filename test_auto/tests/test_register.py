import pytest
import time
from pages.register import register_pages
from common.yaml_handler import config_yaml
from operator import itemgetter

keys = ['user1', 'user2', 'user3']
data = itemgetter(*keys)(config_yaml)


class Testregister:
    @pytest.mark.parametrize('user_info', data)
    def test_register_success(self, get_driver, user_info):
        info = itemgetter(*['username', 'password', 'email'])(user_info)
        username, password, reg_email = info
        driver = get_driver
        register = register_pages(driver)
        register.load_pages().register(username, password, reg_email)
        time.sleep(20)
        result = register.register_assert(username)
        assert result


if __name__ == '__main__':
    pytest.main()
