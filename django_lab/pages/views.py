from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('''
<html>
    <title>hello</title>
    <body>你好</body>
</html>
    ''',content_type="text/html; charset=utf-8")


def hello_name(request,name):
    return HttpResponse(f"歡迎 {name}", content_type="text/plain; charset=utf-8")

def search(request):
    keyword=request.GET.get('q',"")
    return HttpResponse(f"查詢：{keyword}", content_type="text/plain; charset=utf-8")

def catalog(request):
    data=3
    products=["鍵盤","筆記本","滑鼠","麥克風"]
    mydict={"name":"ntub","age":18}
    return render(request,  
                  "pages/catalog.html",{
                    "products":products,
                    "data":data,
                    "mydict":mydict,
                  })