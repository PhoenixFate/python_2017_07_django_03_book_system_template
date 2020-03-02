from django.shortcuts import render, redirect
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


def login(request):
    """显示登录页面"""
    # 判断用户是否已经登录
    if request.session.get("user"):
        return redirect("/index")
    # 取出cookie中的值
    if "username_cookie" in request.COOKIES:
        username_cookie = request.COOKIES["username_cookie"]
    else:
        username_cookie = ""
    return render(request, "bookInfo/login.html", {"username_cookie": username_cookie})


def login_check(request):
    """校验登录"""
    # request.POST 保存的是post提交的参数
    # request.GET 保存的是get提交的参数
    request_path = request.path
    print(request_path)
    method_type = request.method
    print(method_type)
    # 1.获取用户名和密码
    username = request.POST.get("username")
    password = request.POST.get("password")
    remember = request.POST.get("remember")
    gender = request.POST.get('gender')
    is_tuanyuan = request.POST.get('is_tuanyuan')
    joy = request.POST.getlist('joy')
    city = request.POST.get('city')
    more_text = request.POST.get('more_text')
    print("username: %s " % username)
    print("password: %s " % password)
    print("remember: ", remember)
    print("gender: ", gender)
    print("is_tuanyuan: ", is_tuanyuan)
    print("joy: ", joy)
    print("city: ", city)
    print("more_text: ", more_text)
    # 2.进行登录的校验
    if username == "admin" and password == "123456":
        response = redirect("/index")
        # 判断是否记住用户名
        if remember == "on":
            response.set_cookie("username_cookie", username, max_age=7 * 24 * 3600)
        # 记住登录状态
        request.session["user"] = {"username": username, "password": password}
        return response
    # 3.返回应答
    return redirect("/login/")


def change_password(request):
    """显示修改密码页面"""
    if not request.session.get("user"):
        return redirect("/login")
    return render(request, "bookInfo/change_password.html", {})


def change_password_action(request):
    """修改密码action"""
    new_password = request.POST.get("new_password")
    print("new_password:%s" % new_password)
    user = request.session.get("user")
    return HttpResponse("%s 修改密码为： %s" % (user["username"], new_password))
