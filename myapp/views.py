from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        document = request.FILES['document']
        terms = 'terms' in request.POST

        # Aquí puedes añadir la lógica para guardar el miembro en la base de datos

        return render(request, 'register.html', {'message': 'Registration successful!'})

    return render(request, 'register.html')
