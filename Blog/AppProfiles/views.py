from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from AppProfiles.forms import UserEditForm

@login_required
def editar_perfil(request):
    usuario = request.user
    
    if request.method == "POST":
        formulario= UserEditForm(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            usuario.email=data['email']
            usuario.set_password(data['password1'])
            usuario.first_name=data['first_name']
            usuario.last_name=data['last_name']
            usuario.save()
            return redirect('inicio')
    else:
        formulario = UserEditForm ({'email': usuario.email})
        
    return render(request, 'AppBlog/editar_perfil.html', {'form': formulario})