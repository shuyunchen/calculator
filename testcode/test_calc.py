#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/24 16:35
# @Author  : 陈庆云
# @File    : test_calc.py
# @Software: PyCharm Community Edition
import pytest
import yaml
from pythoncode.calculator import Calculator


def get_data():
    with open("test_calc.yaml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        print(datas)
        return datas


class TestCalc:
    def setup_class(self):
        # 实例化类对象
        self.calc = Calculator()

    def setup_method(self):
        print("\n【开始计算】")

    def teardown_method(self):
        print("\n【计算结束】")

    @pytest.mark.parametrize("a, b, expect", get_data()["add_datas"], ids=get_data()["add_myids"])
    def test_add(self, a, b, expect):
        res = self.calc.add(a, b)
        print("实际计算结果为：", res)
        assert res == expect

    @pytest.mark.parametrize("a, b, expect", get_data()["sub_datas"], ids=get_data()["sub_myids"])
    def test_sub(self, a, b, expect):
        res = self.calc.sub(a, b)
        print("实际计算结果为：", res)
        assert res == expect

    @pytest.mark.parametrize("a, b, expect", get_data()["mul_datas"], ids=get_data()["mul_myids"])
    def test_mul(self, a, b, expect):
        res = self.calc.mul(a, b)
        print("实际计算结果为：", res)
        assert res == expect

    @pytest.mark.parametrize("a, b, expect", get_data()["div_datas"], ids=get_data()["div_myids"])
    def test_div(self, a, b, expect):
        res = self.calc.div(a, b)
        print("实际计算结果为：", res)
        assert res == expect
