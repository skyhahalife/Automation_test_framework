import yaml


# yaml is used to save certain extract values etc. token uuid
class YamlUtil:

    def read_yaml(self, filepath):
        with open(filepath, encoding="utf-8", mode="r") as f:
            content = yaml.load(stream=f, Loader=yaml.FullLoader)
        return content

    def write_yaml(self, file_path, data):
        with open(file_path, encoding="utf-8", mode="w") as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    def add_yaml(self, file_path, data):
        with open(file_path, encoding="utf-8", mode="a") as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    def clean_yaml(self, file_path):
        with open(file_path, encoding="utf-8", mode='w') as f:
            f.truncate()


if __name__ == '__main__':
    yaml_util = YamlUtil()

    # read yaml
    # value = yaml_util.read_yaml(key='password')
    # print(value)

    # add yaml
    extract_value_name = {
        "name": "jack"
    }
    extract_value_password = {
        "password": "123456"
    }
    yaml_util.write_yaml(extract_value_name)
    yaml_util.add_yaml(extract_value_password)

    # clean yaml
    # yaml_util.clean_yaml()
