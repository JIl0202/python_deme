import yaml
from config.path import config_yaml_path


# 解析yaml中的测试数据 需要用到yaml库
def read_yaml(ypath):
    """ypath:yaml文件的路径"""
    with open(ypath, encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data


def read(ypath):
    """ypath:yaml文件的路径"""
    with open(ypath, encoding="utf-8") as f:
        data = f.read()
        return data


config_yaml = read_yaml(config_yaml_path)


if __name__ == '__main__':
    result = read_yaml(config_yaml_path)
    res = read(config_yaml_path)
    print(result, "\n", res)
