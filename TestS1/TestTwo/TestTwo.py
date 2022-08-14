import pytest
import yaml


class TestDemo:
    # @pytest.mark.parametrize('env', yaml.safe_load(open('./TestS1/TestTwo/env.yaml')))
    @pytest.mark.parametrize('env', yaml.safe_load(open('./env.yaml')))
    def test_demo(self, env):
        if 'test' in env:
            print('特使环境')
            print(env['test'])
        elif 'dev' in env:
            print('开发环境')

    def test_yaml(self):
        # print(yaml.safe_load('./TestS1/TestTwo/env.yaml'))
        print(yaml.safe_load('./env.yaml'))
