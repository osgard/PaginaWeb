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
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
########################################################################################################
#PRODUCTOS LIST
########################################################################################################
def producto_list(request):
		productos = Producto.objects.filter(published_date__year=2017).order_by('artista')
		return render(request, 'tienda/index.html', {'productos':productos})
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
					####################
					#if(str(request.user))in request.COOKIES:
					#	carrito = request.COOKIES[str(request.user)]
					#else:
					#	carrito =""
					#	cookies = HttpResponseRedirect('/')
					#	cookies.set_cookie(str(request.user),carrito)
					#	return cookies
					####################
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
#########################################################################################################
#REGISTER
#########################################################################################################
def cliente_new(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			post_values = request.POST.copy()
			post_values['password'] = post_values['password1']
			request.POST = post_values
			cliente_log(request)
			#cliente = form.save(commit=False)
			#cliente.save()
			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request, 'tienda/cliente_new.html', {'form': form})

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

################################################################################
#DETAILS
################################################################################
def producto_detail(request, pk):
		producto = get_object_or_404(Producto, pk=pk)
		return render(request, 'tienda/producto_detail.html', {'producto': producto})
##################################################################################
#CARRITO
#################################################################################

		
		
