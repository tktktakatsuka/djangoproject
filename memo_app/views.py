from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # 先ほど作成したhtmlを第2引数に指定する