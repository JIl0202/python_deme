import os

# path.py当前文件路径
path_path = os.path.abspath(__file__)

# config package的路径
config_path = os.path.dirname(path_path)

# config yaml文件的路径
config_yaml_path = os.path.join(config_path, 'config.yaml')

# project项目路径
project_path = os.path.dirname(config_path)

# data package的路径
data_path = os.path.join(project_path, 'data')

# 判断datapath是否存在,如果不存在则创建datapackage
if not os.path.exists(data_path):
    os.mkdir(data_path)

# yaml文件路径

yaml_path = os.path.join(data_path, 'yaml.yaml')
