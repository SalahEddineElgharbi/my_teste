from django.shortcuts import render


def index(request):

    # 3la khater temlpate fiter 
    context_dict = {'text':'hello world','number':100 }
    return render(request,'basic_app/index.html',context_dict)



def index1(request):
    return render(request,'basic_app/index1.html')
    

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_urls.html')


  