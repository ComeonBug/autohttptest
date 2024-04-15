import allure
import pytest

class TestBaidu:

    # @pytest.mark.parametrize('',[])
    @pytest.mark.P0
    def test_baidu_P0(self):
        casename = 'casename'
        allure.dynamic.title(casename)
        print('test_baidu_P0')
        assert 1 ==1

    # @pytest.mark.parametrize('',[])
    @pytest.mark.P0
    @pytest.mark.P1
    def test_baidu_P1(self):
        casename = 'casename'
        allure.dynamic.title(casename)
        print('test_baidu_P0_P1')
        assert 1 ==1


if __name__ == '__main__':
    pytest.main(['-vss','-m P0'])