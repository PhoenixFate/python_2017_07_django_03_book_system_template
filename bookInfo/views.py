from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from .models import Book


# Create your views here.
def index1(request):
    # 1.加载模板文件 获取一个模板对象
    template = loader.get_template("bookInfo/index.html")
    # 2.定义模板上下文，给模板文件传数据
    # context = RequestContext(request)
    # 3.模板渲染，产生一个替换后的html页面
    response_html = template.render({})
    # 4.返回响应
    return HttpResponse(response_html)


def index2(request):
    return render(request, "bookInfo/index.html", {})


def index3(request):
    """
    模板文件的加载顺序
    1.首先去配置的模板目录下面找模板文件
    2.去installed_apps 下面的每个应用下面的templates找模板文件，前提应用中必须有templates文件夹

    """

    return render(request, "bookInfo/index3.html", {})


def temp_var(request):
    """模板变量"""
    my_dict = {"title": "title_test"}
    my_list = [0, 1, 2, 3]
    book = Book.objects.get(id=1)

    # 定义模板上下文
    context = {'my_dict': my_dict, 'my_list': my_list, 'book': book}
    return render(request, "bookInfo/template_parameters.html", context)


def template_tag(request):
    """模板标签"""
    all_books = Book.objects.all()

    return render(request, "bookInfo/template_tags.html", {"all_books": all_books})


def template_filter(request):
    """模板过滤器"""
    all_books = Book.objects.all()
    return render(request, "bookInfo/template_filter.html", {"all_books": all_books})


def template_extend(request):
    """模板继承"""
    return render(request, "bookInfo/child1.html")


def html_escape(request):
    """html 转义"""

    return render(request, "bookInfo/escape.html", {'content': "<h1>hello</h1>"})
