from django.shortcuts import render,redirect


def logout_view(request):
    return redirect('home')


def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    return render(request, 'core/index.html')

def registro(request):
    return render(request, 'core/registro.html')

def recuperar_contrasena(request):
    return render(request, 'core/recuperar.html')

def perfil(request):
    return render(request, 'core/perfil.html')

def admin_panel(request):
    return render(request, 'core/admin-panel.html')

def feria_emprendedores(request):
    return render(request, 'core/feria-emprendedores.html')

def feria_comida(request):
    return render(request, 'core/feria-comida.html')

def concierto(request):
    return render(request, 'core/concierto-parque.html')

def trekking(request):
    return render(request, 'core/trekking-quebrada.html')
