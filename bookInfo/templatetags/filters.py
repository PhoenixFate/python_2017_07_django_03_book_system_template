# 自定义过滤器
# 过滤器本事是python函数
from django import template

# 创建一个Library对象
register = template.Library()


# 自定义的过滤器至少有一个参数，最多有两个参数
@register.filter()
def is_even(num):
    """判断num是否是偶数"""
    return num % 2 == 0


@register.filter()
def is_even_value(num, value):
    """判断num是否是被value整除以"""
    return num % value == 0
