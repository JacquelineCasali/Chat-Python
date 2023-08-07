from django.contrib.auth import login

from django.shortcuts import render, redirect

from .forms import SignUpForm
# Create your views here.
def frontpage(request):
        context={}
        return render(request,'core/frontpage.html',context)

def cadastro(request):
       context={}
       return render(request,'core/cadastro.html', context)


# def cadastro(request):
      
#        if request.method == 'POST':
#               form =SignUpForm(request.POST)

#               if form.is_valid():
#                      user=form.save()
#                      login(request, user)
#                      return redirect ('frontpage')
#               else :
#                      form = SignUpForm()
#                      return render (request,'core/cadastro.html',{'form': form})
