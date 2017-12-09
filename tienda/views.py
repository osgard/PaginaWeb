from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Cliente, Genero, Artista, Disquera, Producto, Compra
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import ClienteForm
from .forms import ClienteLog
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.
########################################################################################################
#PRODUCTOS LIST
########################################################################################################
def producto_list(request):
		productos = Producto.objects.filter(published_date__year=2017).order_by('artista')
		return render(request, 'tienda/index.html', {'productos':productos})
#########################################################################################################
#REGISTER
#########################################################################################################
def cliente_new(request):
	if request.method == "POST":
		form = ClienteForm(request.POST)
		if form.is_valid():
			cliente = form.save(commit=False)
			cliente.save()
			return redirect('index')
	else:
		form = ClienteForm()
	return render(request, 'tienda/cliente_new.html', {'form': form})
###########################################################################################################
#LOGIN
###########################################################################################################	
def cliente_log(request):
	if request.method == "POST":
		formulario = ClienteLog(request.POST)
		if formulario.is_valid:
			usuarioo = request.POST['username']
			clave = request.POST['password']
			user = authenticate(username=usuarioo, password=clave)
			if user is not None:
				if user.is_active:
					login(request, user)
					#usuario = User.objects.get(username=usuarioo)
					return redirect('index')
				else:
					message = "tu usuario esta inactivo"
			else:
				message = "usuaro y/o contraseña erroneos"
				#formulario = ClienteLog()
				#return formulario
				return render(request, 'tienda/cliente_log.html', {'formulario': formulario})
	else:
		formulario = ClienteLog()
	#return formulario
	return render(request, 'tienda/cliente_log.html', {'formulario': formulario})
#################################################################################################################
#LOGOUT
################################################################################################################
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')
	
###################################################################################################################
#COCKIES
####################################################################################################################3
def crear_cookie (request):
    response = HttpResponse('')
    usuario = request.user
    if not request.COOKIES.has_key(str(usuario)):
        response.set_cookie(str(usuario), '')
    return response

############################################################################
#ACTULIZAR_COCKIES
############################################################################
def actualizar_cookie (request, articulo, cantidad):
    actualizado = False
    usuario = request.user
    response = HttpResponseRedirect(request.GET.get('next'))
    print (request.GET.get('next'))
    if request.COOKIES.has_key(str(usuario)):
        carrito = request.COOKIES[str(usuario)]
        print (carrito)
        if carrito != "" :
            lista = carrito.split(';')
            carrito = ""
            for element in lista:
                if element != "":
                    element = element.split('=')
                    if element[0] == articulo:
                        element[1] = int(cantidad)
                        actualizado = True
                    if element[1]!= 0:
                        carrito += str(element[0]) + "=" + str(element[1]) + ";"
        if actualizado == False :
            carrito += articulo + '=' + cantidad + ';'
        response.set_cookie(str(usuario), carrito)
    else:
        response.set_cookie(str(usuario), articulo + '=' + cantidad + ';')
    print (request.COOKIES)
    return response
################################################################################
#DETAILS
################################################################################
def producto_detail(request, pk):
		producto = get_object_or_404(Producto, pk=pk)
		return render(request, 'tienda/producto_detail.html', {'producto': producto})
##################################################################################
#CARRITO
#################################################################################
def carrito(request):
    pagina = 'tienda/cart.html'
    usuario = request.user
    formulario = nuevo_usuario(request)
    formulario2 = ingresar(request)
    listado = []
    if request.COOKIES.has_key(str(usuario)):
        carrito = request.COOKIES[str(usuario)]
        if carrito != "" :
            productos = Producto.objects.all()
            lista = carrito.split(';')
            carrito = ""
            for element in lista:
                if element != "":
                    element = element.split('=')
                    for producto in productos:
                        if (str(element[0]) == str(producto.nombreP)):
                            total = int(element[1]) * int(Producto.precio)
                            encontrado = {"nombre": producto.nombreP),"cantidad": element[1], "Precio": Producto.precio, "total": total, "Portada": producto.Portada, "Articulo": element[0]}
                            listado.append(encontrado)
    contexto = {'articulos' : listado, 'usuario':usuario, 'formulario':formulario, 'formulario2':formulario2}
    return render(request, pagina, contexto)
	


		
		
