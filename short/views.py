from django.shortcuts import redirect, render
from .models import Link
# Create your views here.
def Home(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        if Link.objects.filter(original=link).count() == 0:
            new = Link(original=link)
            new.save()
            new_link = Link.objects.get(original=link).short
            context = {'link':new_link}

        else:
            get_link = Link.objects.get(original=link).short
            context = {'link':get_link}
    else:
            context ={'link':None}

    return render(request,'index.html',context)


def Send(request,code):
    if Link.objects.filter(short=code).count() == 0:
        context = {'link':None,"message":"Link dose Not exites "}
        return render(request,'index.html',context)
    else:
        link = Link.objects.get(short=code).original
        return redirect(link)