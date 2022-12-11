from unicodedata import decomposition
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from app_feria.models import *
from app_feria.forms import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #se importa el AuthenticationForm para el inicio de sesion
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.edit import CreateView

# Create your views here.

############
#  INICIO  #
############

def inicio(request):
    return render(request,'app_feria/inicio.html')


############
#  LOGIN  #
############


def InicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contra)
            if user:
                login(request, user)
                return render(request, "app_feria/inicio.html", {"mensaje":f"Bienvenido/a {user}"})
        else:
            return render(request, "app_feria/inicio.html", {"mensaje": "Datos incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, "app_feria/login.html", {"f1":form})


def registro(request):
    if request.method == "POST":
        formu = FormularioRegistro(request.POST)
        if formu.is_valid():
            username = formu.cleaned_data["username"]
            formu.save()
            return render(request, "app_feria/inicio.html", {"mensaje": f"Usuario {username} creado"})
    else:
        formu = FormularioRegistro()
    return render(request, "app_feria/registro.html", {"f2":formu})





############
#  JEANS  #
############

def jean(request):
    return render(request,'app_feria/jean.html')


#CREACION DE JEANS
def formulariojean(request):
    if request.method=="POST":#si yo le doy al boton GO
        formulariojean = FormuJean(request.POST, request.FILES)
        if formulariojean.is_valid():
            info = formulariojean.cleaned_data
            jeanf = Jean(codigo = info["codigo"], talle = info["talle"], color = info["color"], precio = info["precio"], imagen = info["imagen"], imagen_b = info["imagen_b"], genero = info["genero"])#lee la informacion de las cajas de texto
            jeanf.save()#guardar en la base de datos
            return render(request,"app_feria/inicio.html")#despues de enviar salta esta pagina
    else:
        formulariojean = FormuJean()
    return render(request,"app_feria/FJean.html",{"formulario1":formulariojean})#cuando entro a la pagina web por primera vez sale este return

#BUSQUEDA DE JEANS
def busquedaJeans(request):
    return render(request,"app_feria/busquedaJeans.html")

def buscar(request):
    if request.GET["genero"]:
        busqueda = request.GET["genero"]
        jeans = Jean.objects.filter(genero__icontains=busqueda.capitalize())#puede ir tambien camada__icontains = busqueda
        return render(request,"app_feria/jean_b.html",{"jeans":jeans, "busqueda":busqueda})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando jeans para {busqueda}")
 

#LEER JEANS
def leerJeans(request):
    fly = Jean.objects.all()
    contexto = {"fly":fly}
    return render(request,"app_feria/jean.html",contexto)


#ELIMINAR JEANS
def eliminaJean(request, numJean):
    idcodigo= Jean.objects.get(codigo=numJean)
    idcodigo.delete()
    jeans = Jean.objects.all()
    contextov = {"fly":jeans}
    return render (request, "app_feria/jean.html", contextov)


#EDITAR JEANS
def editaJean(request, numJean):
    idcodigo = Jean.objects.get(codigo=numJean)

    if request.method == "POST":
        formulariojean = FormuJean(request.POST,request.FILES)##,request.FILES
        if formulariojean.is_valid():
            
            info = formulariojean.cleaned_data
            
            idcodigo.imagen = info["imagen"]
            idcodigo.imagen_b = info["imagen_b"]
            idcodigo.codigo = info["codigo"]
            idcodigo.talle = info["talle"]
            idcodigo.color = info["color"]
            idcodigo.genero = info["genero"]
            idcodigo.precio = info["precio"]

            idcodigo.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariojean = FormuJean(initial={"codigo":idcodigo.codigo,"talle":idcodigo.talle,
        "color": idcodigo.color, "precio": idcodigo.precio, "imagen": idcodigo.imagen, "imagen_b": idcodigo.imagen_b, "genero": idcodigo.genero})
    return render(request,"app_feria/editarJean.html", {"formulario1":formulariojean, "idJean": numJean})


#DETALLE JEANS
def jean_detail(request,codigo):
    jean = get_object_or_404(Jean, pk=codigo)
    return render(request,'app_feria/jean_detail.html',{'jean':jean})







############
# REMERA #
############

def remera(request):
    return render(request,'app_feria/remera.html')


#CREACION DE REMERA
def formularioremera(request):
    if request.method=="POST":
        formularioremera = FormuRemera(request.POST, request.FILES)
        if formularioremera.is_valid():
            info = formularioremera.cleaned_data
            remeraf = Remera(codigo = info["codigo"], talle = info["talle"], color = info["color"], precio = info["precio"], imagen = info["imagen"], imagen_b = info["imagen_b"], genero = info["genero"])
            remeraf.save()
            return render(request,"app_feria/inicio.html")
    else:
        formularioremera = FormuRemera()
    return render(request,"app_feria/FRemera.html",{"formulario2":formularioremera})


#BUSQUEDA DE REMERA
def busquedaRemera(request):
    return render(request,"app_feria/busquedaRemera.html")


def buscar_rem(request):
    if request.GET["genero"]:
        busqueda_rem = request.GET["genero"]
        remeras = Remera.objects.filter(genero__icontains = busqueda_rem.capitalize())#puede ir tambien camada__icontains = busqueda
        return render(request,"app_feria/remera_b.html",{"remeras":remeras, "busqueda_rem":busqueda_rem})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando remeras para {busqueda_rem}")


#LEER REMERA
def leerRemera(request):
    persona = Remera.objects.all()
    contexto = {"persona":persona}
    return render(request,"app_feria/remera.html",contexto)


#ELIMINAR REMERA
def eliminaRemera(request, generoRemera):
    generoPe= Remera.objects.get(codigo=generoRemera)
    generoPe.delete()
    remeraElim = Remera.objects.all()
    contextoPe = {"persona":remeraElim}
    return render (request, "app_feria/remera.html", contextoPe)


#EDITAR REMERA
def editarRemera(request, generoRemera):
    codigo= Remera.objects.get(codigo=generoRemera)

    if request.method=="POST":
        formularioremera = FormuRemera(request.POST, request.FILES)
        if formularioremera.is_valid():
            
            info = formularioremera.cleaned_data
           
            codigo.codigo = info["codigo"]
            codigo.talle = info["talle"]
            codigo.color = info["color"]
            codigo.precio = info["precio"]
            codigo.genero = info["genero"]
            codigo.imagen = info["imagen"]
            codigo.imagen_b = info["imagen_b"]
            codigo.save()
            return render(request,"app_feria/inicio.html")
    else:
        formularioremera = FormuRemera(initial={"codigo":codigo.codigo,"talle":codigo.talle,
        "color":codigo.color, "precio":codigo.precio, "genero":codigo.genero, "imagen":codigo.imagen, "imagen_b":codigo.imagen_b})
    return render(request,"app_feria/editarRemera.html",{"formulario2":formularioremera, "generoRemera": generoRemera })  


#DETALLE REMERA
def remera_detail(request,codigo):
    remera = get_object_or_404(Remera, pk=codigo)
    return render(request,'app_feria/remera_detail.html',{'remera':remera})





############
# CAMISAS #
############

def camisa(request):
    return render(request,'app_feria/camisa.html')


# CREACION DE CAMISA
def formulariocamisa(request):
    if request.method=="POST":
        formulariocamisa = FormuCamisa(request.POST, request.FILES)
        if formulariocamisa.is_valid():
            info = formulariocamisa.cleaned_data
            editCamisa = Camisa(codigo = info["codigo"], talle = info["talle"], color = info["color"], precio = info["precio"], imagen = info["imagen"], imagen_b = info["imagen_b"], genero = info["genero"])
            editCamisa.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariocamisa = FormuCamisa()
    return render(request,"app_feria/FCamisa.html",{"formulario3":formulariocamisa})


#BUSQUEDA DE CAMISA
def busquedaCamisa(request):
    return render(request,"app_feria/busquedaCamisa.html")

def buscar_cami(request):
    if request.GET["genero"]:
        busqueda_cami = request.GET["genero"]
        camisas = Camisa.objects.filter(genero__icontains = busqueda_cami.capitalize())#puede ir tambien camada__icontains = busqueda
        return render(request,"app_feria/camisa_b.html",{"camisas":camisas, "busqueda_cami":busqueda_cami})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando camisa para {busqueda_cami}")


#LEER CAMISA
def leerCamisa(request):
    pasa = Camisa.objects.all()
    contexto = {"pasa":pasa}
    return render(request,"app_feria/camisa.html",contexto)  


#ELIMINAR CAMISA
def eliminaCamisa(request, generoCamisa):
    elimCamisa= Camisa.objects.get(codigo=generoCamisa)
    elimCamisa.delete()

    camisaElim = Camisa.objects.all()
    contextoPa = {"pasa":camisaElim}
    return render (request, "app_feria/camisa.html", contextoPa)


#EDITAR CAMISA
def editarCamisa(request, generoCamisa):
    genero= Camisa.objects.get(codigo=generoCamisa)

    if request.method=="POST":
        formulariocamisa = FormuCamisa(request.POST, request.FILES)
        if formulariocamisa.is_valid():
            
            info = formulariocamisa.cleaned_data
           
            genero.codigo = info["codigo"]
            genero.talle = info["talle"]
            genero.color = info["color"]
            genero.precio = info["precio"]
            genero.genero = info["genero"]
            genero.imagen = info["imagen"]
            genero.imagen_b = info["imagen_b"]
            genero.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariocamisa = FormuCamisa(initial={"codigo":genero.codigo,"talle":genero.talle,
        "color":genero.color, "precio":genero.precio, "genero":genero.genero, "imagen":genero.imagen, "imagen_b":genero.imagen_b})
    return render(request,"app_feria/editarCamisa.html",{"formulario3":formulariocamisa, "generoCamisa": generoCamisa })  


#DETALLE CAMISA
def camisa_detail(request,codigo):
    camisa = get_object_or_404(Camisa, pk=codigo)
    return render(request,'app_feria/camisa_detail.html',{'camisa':camisa})




#############
# BUSCADOR #
#############


#BUSCADOR
def bus(request):
    return render(request,"app_feria/buscar.html")


#################
# EDITARUSUARIO #
#################

@login_required
def editarUsuario(request):
    usuarioConectado= request.user
    if request.method=="POST":
        miFormulario = FormularioEditarUsuario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            usuarioConectado.first_name = info["first_name"]
            usuarioConectado.last_name = info["last_name"]
            usuarioConectado.email = info["email"]
            usuarioConectado.password1 = info["password1"]
            usuarioConectado.password2 = info["password2"]
            usuarioConectado.save()
            return render(request,"app_feria/inicio.html")
    else:
        miFormulario = FormularioEditarUsuario(initial={
            "first_name": usuarioConectado.first_name,
            "last_name": usuarioConectado.last_name,
            "email": usuarioConectado.email,
            })
    return render(request,"app_feria/editarUsuario.html",{"miForm":miFormulario, "usuario": usuarioConectado })

##########
# About #
##########

@login_required
def sobrenosotros(request):
    return render(request,'app_feria/sobrenosotros.html')



############
# TODO100 #
############

def todo100(request):
    return render(request,'app_feria/camisa.html')


# CREACION DE TODO100
def formulariotodo(request):
    if request.method=="POST":
        formulariotodo = FormuTodo100(request.POST, request.FILES)
        if formulariotodo.is_valid():
            info = formulariotodo.cleaned_data
            editTodo = Todo100(codigo = info["codigo"], talle = info["talle"], color = info["color"], precio = info["precio"], imagen = info["imagen"], imagen_b = info["imagen_b"], genero = info["genero"])
            editTodo.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariotodo = FormuTodo100()
    return render(request,"app_feria/FTodo.html",{"formulario4":formulariotodo})


#LEER TODO100
def leerTodo(request):
    todo = Todo100.objects.all()
    contexto = {"todo":todo}
    return render(request,"app_feria/todo.html",contexto)  


#ELIMINAR TODO100
def eliminaTodo(request, generoTodo):
    elimTodo= Todo100.objects.get(codigo=generoTodo)
    elimTodo.delete()

    todoElim = Todo100.objects.all()
    contextoPa = {"todo":todoElim}
    return render (request, "app_feria/todo.html", contextoPa)


#EDITAR TODO100
def editarTodo(request, generoTodo):
    elimTodo= Todo100.objects.get(codigo=generoTodo)

    if request.method=="POST":
        formulariotodo = FormuTodo100(request.POST, request.FILES)
        if formulariotodo.is_valid():
            
            info = formulariotodo.cleaned_data
           
            elimTodo.codigo = info["codigo"]
            elimTodo.talle = info["talle"]
            elimTodo.color = info["color"]
            elimTodo.precio = info["precio"]
            elimTodo.genero = info["genero"]
            elimTodo.imagen = info["imagen"]
            elimTodo.imagen_b = info["imagen_b"]
            elimTodo.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariotodo = FormuTodo100(initial={"codigo":elimTodo.codigo,"talle":elimTodo.talle,
        "color":elimTodo.color, "precio":elimTodo.precio, "genero":elimTodo.genero, "imagen":elimTodo.imagen, "imagen_b":elimTodo.imagen_b})
    return render(request,"app_feria/editarTodo.html",{"formulario4":formulariotodo, "generoTodo": generoTodo })  


#DETALLE TODOPOR 100
def todo100_detail(request,codigo):
    todo100 = get_object_or_404(Todo100, pk=codigo)
    return render(request,'app_feria/todo100_detail.html',{'todo100':todo100})




############
# CALZADO #
############

def calzado(request):
    return render(request,'app_feria/calzado.html')


#CREACION DE Calzado
def formulariocalzado(request):
    if request.method=="POST":
        formulariocalzado = FormuCalzado(request.POST, request.FILES)
        if formulariocalzado.is_valid():
            info = formulariocalzado.cleaned_data
            calzadof = Calzado(codigo = info["codigo"], talle = info["talle"], color = info["color"], precio = info["precio"], imagen = info["imagen"], imagen_b = info["imagen_b"], genero = info["genero"])
            calzadof.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariocalzado = FormuCalzado()
    return render(request,"app_feria/FCalzado.html",{"formulario5":formulariocalzado})


#BUSQUEDA DE CALZADO
def busquedaCalzado(request):
    return render(request,"app_feria/busquedaCalzado.html")


def buscar_calza(request):
    if request.GET["genero"]:
        busqueda_calza = request.GET["genero"]
        calzados = Calzado.objects.filter(genero__icontains= busqueda_calza.capitalize())#puede ir tambien camada__icontains = busqueda
        return render(request,"app_feria/calzado_b.html",{"calzados":calzados, "busqueda_calza":busqueda_calza})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando calzado para {busqueda_calza}")


#LEER CALZADO
def leerCalzado(request):
    calza = Calzado.objects.all()
    contexto = {"calza":calza}
    return render(request,"app_feria/calzado.html",contexto)


#ELIMINAR CALZADO
def eliminaCalzado(request, generoCalzado):
    generoCalza= Calzado.objects.get(codigo=generoCalzado)
    generoCalza.delete()
    calzadoElim = Calzado.objects.all()
    contextoP = {"calza":calzadoElim}
    return render (request, "app_feria/calzado.html", contextoP)



#EDITAR CALZADO
def editarCalzado(request, generoCalzado):
    generoCalza= Calzado.objects.get(codigo=generoCalzado)
    if request.method=="POST":
        formulariocalzado = FormuCalzado(request.POST, request.FILES)
        if formulariocalzado.is_valid():
            info = formulariocalzado.cleaned_data
            generoCalza.codigo = info["codigo"]
            generoCalza.talle = info["talle"]
            generoCalza.color = info["color"]
            generoCalza.precio = info["precio"]
            generoCalza.genero = info["genero"]
            generoCalza.imagen = info["imagen"]
            generoCalza.imagen_b = info["imagen_b"]
            generoCalza.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariocalzado = FormuCalzado(initial={"codigo":generoCalza.codigo,"talle":generoCalza.talle,
        "color":generoCalza.color, "precio":generoCalza.precio, "genero":generoCalza.genero, "imagen":generoCalza.imagen, "imagen_b":generoCalza.imagen_b})
    return render(request,"app_feria/editarCalzado.html",{"formulario5":formulariocalzado, "generoCalzado": generoCalzado })  


#DETALLE CALZADO
def calzado_detail(request,codigo):
    calzado = get_object_or_404(Calzado, pk=codigo)
    return render(request,'app_feria/calzado_detail.html',{'calzado':calzado})







############
# INVERNAL #
############

def invernal(request):
    return render(request,'app_feria/invernal.html')


# CREACION DE INVERNAL
def formularioinvernal(request):
    if request.method=="POST":
        formularioinvernal = FormuInvernal(request.POST, request.FILES)
        if formularioinvernal.is_valid():
            info = formularioinvernal.cleaned_data
            editInvernal = Invernal(codigo = info["codigo"], talle = info["talle"], color = info["color"], precio = info["precio"], imagen = info["imagen"], imagen_b = info["imagen_b"], genero = info["genero"])
            editInvernal.save()
            return render(request,"app_feria/inicio.html")
    else:
        formularioinvernal = FormuInvernal()
    return render(request,"app_feria/FInvernal.html",{"formulario6":formularioinvernal})


#BUSQUEDA DE INVERNAL
def busquedaInvernal(request):
    return render(request,"app_feria/busquedaInvernal.html")

def buscar_inve(request):
    if request.GET["genero"]:
        busqueda_inve = request.GET["genero"]
        invernales = Invernal.objects.filter(genero__icontains = busqueda_inve.capitalize())#puede ir tambien camada__icontains = busqueda
        return render(request,"app_feria/invernal_b.html",{"invernales":invernales, "busqueda_inve":busqueda_inve})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando ropa de invierno para {busqueda_inve}")


#LEER INVERNAL
def leerInvernal(request):
    inve = Invernal.objects.all()
    contexto = {"inve":inve}
    return render(request,"app_feria/invernal.html",contexto)  


#ELIMINAR INVERNAL
def eliminaInvernal(request, generoInvernal):
    elimInvernal= Invernal.objects.get(codigo=generoInvernal)
    elimInvernal.delete()

    invernalElim = Invernal.objects.all()
    contextoIn = {"inve":invernalElim}
    return render (request, "app_feria/invernal.html", contextoIn)


#EDITAR INVERNAL
def editarInvernal(request, generoInvernal):
    elimInvernal= Invernal.objects.get(codigo=generoInvernal)

    if request.method=="POST":
        formularioinvenal = FormuInvernal(request.POST, request.FILES)
        if formularioinvenal.is_valid():
            
            info = formularioinvenal.cleaned_data
           
            elimInvernal.codigo = info["codigo"]
            elimInvernal.talle = info["talle"]
            elimInvernal.color = info["color"]
            elimInvernal.precio = info["precio"]
            elimInvernal.genero = info["genero"]
            elimInvernal.imagen = info["imagen"]
            elimInvernal.imagen_b = info["imagen_b"]
            elimInvernal.save()
            return render(request,"app_feria/inicio.html")
    else:
        formularioinvenal = FormuInvernal(initial={"codigo":elimInvernal.codigo,"talle":elimInvernal.talle,
        "color":elimInvernal.color, "precio":elimInvernal.precio, "genero":elimInvernal.genero, "imagen":elimInvernal.imagen, "imagen_b":elimInvernal.imagen_b})
    return render(request,"app_feria/editarInvernal.html",{"formulario6":formularioinvenal, "generoInvernal": generoInvernal })  


#DETALLE INVERNAL
def invernal_detail(request,codigo):
    invernal = get_object_or_404(Invernal, pk=codigo)
    return render(request,'app_feria/invernal_detail.html',{'invernal':invernal})





############
# PANTALON #
############

def pantalon(request):
    return render(request,'app_feria/pantalon.html')


#CREACION DE PANTALON
def formulariopantalon(request):
    if request.method=="POST":
        formulariopantalon = FormuPantalon(request.POST, request.FILES)
        if formulariopantalon.is_valid():
            info = formulariopantalon.cleaned_data
            pantalonf = Pantalon(codigo = info["codigo"], talle = info["talle"], color = info["color"], precio = info["precio"], imagen = info["imagen"], imagen_b = info["imagen_b"], genero = info["genero"])
            pantalonf.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariopantalon = FormuPantalon()
    return render(request,"app_feria/FPantalon.html",{"formulario7":formulariopantalon})


#BUSQUEDA DE PANTALON
def busquedaPantalon(request):
    return render(request,"app_feria/busquedaPantalon.html")


def buscar_panta(request):
    if request.GET["genero"]:
        busqueda_panta = request.GET["genero"]
        pantalones = Pantalon.objects.filter(genero__icontains = busqueda_panta.capitalize())#puede ir tambien camada__icontains = busqueda
        return render(request,"app_feria/pantalon_b.html",{"pantalones":pantalones, "busqueda_panta":busqueda_panta})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando pantalon o short para {busqueda_panta}")


#LEER PANTALON
def leerPantalon(request):
    panta = Pantalon.objects.all()
    contexto = {"panta":panta}
    return render(request,"app_feria/pantalon.html",contexto)


#ELIMINAR PANTALON
def eliminaPantalon(request, generoPantalon):
    generoPanta= Pantalon.objects.get(codigo=generoPantalon)
    generoPanta.delete()
    pantalonElim = Pantalon.objects.all()
    contextoPe = {"panta":pantalonElim}
    return render (request, "app_feria/pantalon.html", contextoPe)



#EDITAR PANTALON
def editarPantalon(request, generoPantalon):
    generoPanta= Pantalon.objects.get(codigo=generoPantalon)
    if request.method=="POST":
        formulariopantalon = FormuPantalon(request.POST, request.FILES)
        if formulariopantalon.is_valid():
            info = formulariopantalon.cleaned_data
            generoPanta.codigo = info["codigo"]
            generoPanta.talle = info["talle"]
            generoPanta.color = info["color"]
            generoPanta.precio = info["precio"]
            generoPanta.genero = info["genero"]
            generoPanta.imagen = info["imagen"]
            generoPanta.imagen_b = info["imagen_b"]
            generoPanta.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariopantalon = FormuPantalon(initial={"codigo":generoPanta.codigo,"talle":generoPanta.talle,
        "color":generoPanta.color, "precio":generoPanta.precio, "genero":generoPanta.genero, "imagen":generoPanta.imagen, "imagen_b":generoPanta.imagen_b})
    return render(request,"app_feria/editarPantalon.html",{"formulario7":formulariopantalon, "generoPantalon": generoPantalon })  


#DETALLE PANTALON
def pantalon_detail(request,codigo):
    pantalon = get_object_or_404(Pantalon, pk=codigo)
    return render(request,'app_feria/pantalon_detail.html',{'pantalon':pantalon})





############
# CAMPERA #
############

def campera(request):
    return render(request,'app_feria/pantalon.html')


#CREACION DE CAMPERA
def formulariocampera(request):
    if request.method=="POST":
        formulariocampera = FormuCampera(request.POST, request.FILES)
        if formulariocampera.is_valid():
            info = formulariocampera.cleaned_data
            camperaf = Campera(codigo = info["codigo"], talle = info["talle"], color = info["color"], precio = info["precio"], imagen = info["imagen"], imagen_b = info["imagen_b"], genero = info["genero"])
            camperaf.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariocampera = FormuCampera()
    return render(request,"app_feria/FCampera.html",{"formulario8":formulariocampera})


#BUSQUEDA DE CAMPERA
def busquedaCampera(request):
    return render(request,"app_feria/busquedaCampera.html")


def buscar_campe(request):
    if request.GET["genero"]:
        busqueda_campe = request.GET["genero"]
        camperas = Campera.objects.filter(genero__icontains = busqueda_campe.capitalize())#puede ir tambien camada__icontains = busqueda
        return render(request,"app_feria/campera_b.html",{"camperas":camperas, "busqueda_campe":busqueda_campe})
    else:
        mensaje="No enviaste datos."
    return HttpResponse(f"Estoy buscando campera para {busqueda_campe}")


#LEER CAMPERA
def leerCampera(request):
    campe = Campera.objects.all()
    contexto = {"campe":campe}
    return render(request,"app_feria/campera.html",contexto)


#ELIMINAR CAMPERA
def eliminaCampera(request, generoCampera):
    generoCampe= Campera.objects.get(codigo=generoCampera)
    generoCampe.delete()
    camperaElim = Campera.objects.all()
    contextoPe = {"campe":camperaElim}
    return render (request, "app_feria/campera.html", contextoPe)


#EDITAR CAMPERA
def editarCampera(request, generoCampera):
    generoCampe= Campera.objects.get(codigo=generoCampera)
    if request.method=="POST":
        formulariocampera = FormuCampera(request.POST, request.FILES)
        if formulariocampera.is_valid():
            info = formulariocampera.cleaned_data
            generoCampe.codigo = info["codigo"]
            generoCampe.talle = info["talle"]
            generoCampe.color = info["color"]
            generoCampe.precio = info["precio"]
            generoCampe.genero = info["genero"]
            generoCampe.imagen = info["imagen"]
            generoCampe.save()
            return render(request,"app_feria/inicio.html")
    else:
        formulariocampera = FormuCampera(initial={"codigo":generoCampe.codigo,"talle":generoCampe.talle,
        "color":generoCampe.color, "precio":generoCampe.precio, "genero":generoCampe.genero, "imagen":generoCampe.imagen, "imagen_b":generoCampe.imagen_b})
    return render(request,"app_feria/editarCampera.html",{"formulario8":formulariocampera, "generoCampera": generoCampera })  


#DETALLE CAMPERA
def campera_detail(request,codigo):
    campera = get_object_or_404(Campera, pk=codigo)
    return render(request,'app_feria/campera_detail.html',{'campera':campera})










#EDICION O SALIDA
def editar_registro(request):
    return render(request,'app_feria/editar_salir.html')

#REGISTRO O INICIO
def registro_inicio(request):
    return render(request,'app_feria/registro_inicio.html')


"""

 
<main class="conteiner">
        <div class="col-md-4 offset-md-4">

            <form method="POST" class="card-body">
                <h1>Registrarse</h1>
                {% csrf_token %}

                <div class="mb-3">
                    <label for="username">
                        <strong>
                            Usuario:
                        </strong>
                    </label>
                    <input type="text" name="username" id="username" class="form-control" placeholder="Usuario">
                </div>

                <div class="mb-3">
                    <label for="password1">
                        <strong>
                            Contraseña:
                        </strong>
                    </label>
                    <input type="password" name="password1" id="password1" class="form-control" placeholder="Contraseña">
                </div>

                <div class="mb-3">
                    <label for="password2">
                        <strong>
                            Confirmar contraseña:
                        </strong>
                    </label>
                    <input type="password" name="password2" id="password2" class="form-control" placeholder="Contraseña">
                </div>
            
                <button class="btn btn-secondary">
                    Registrate
                </button>
            
            </form>
        </div>


</main>


"""








"""

<!DOCTYPE html>
<html lang="en">
    <head>
        {% load static %}
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Feria web</title>
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="{% static 'app_feria/assets/favicon.ico' %}" />
        <!-- Font Awesome icons (free version)-->
        <script src="https://use.fontawesome.com/releases/v6.1.0/js/all.js" crossorigin="anonymous"></script>
        <!-- Google fonts-->
        <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css" />
        <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="{% static 'app_feria/css/styles.css' %}" rel="stylesheet" />
        <style>
            h3{
                color:rgb(250, 254, 250);
                text-shadow: 1px 2px 2px black, 0 0 25px rgb(255, 0, 0), 0 0 5px rgb(255, 0, 0);
                font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
                font-size: 159%;
                width: 99%;
                padding: 10px 0;
            }
        </style>
    </head>
    <body id="page-top">
        <!-- Responsive navbar-->
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container">

                {% if request.user.is_authenticated %}
                
                <a class="navbar-brand" href="{% url 'Editarosalir' %}"><strong>Hola </strong>{{user.username}}</a>
                <a class="navbar-brand" href="{% url 'Inicio' %}">¡¡Feria Americana!!</a>



                {% else %}
                <a class="navbar-brand" href="{% url 'Iniciar_o_registrar' %}"><strong>Hola</strong>, Inicia tu sesión</a>
                <a class="navbar-brand" href="{% url 'Inicio' %}">¡¡Feria Americana!!</a>

                {% endif %}

                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">

                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        
                        <li class="nav-item"><a class="nav-link" href="{% url 'Leer Remera' %}"><img src="https://cdn-icons-png.flaticon.com/512/5258/5258010.png" style="
                            width: 50px;
                            height: 50px;"></a></li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Leer Camisas' %}"><img src="https://cdn-icons-png.flaticon.com/512/4722/4722182.png" style="
                            width: 50px;
                            height: 50px;"></a></li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Leer Campera' %}"><img src="https://cdn-icons-png.flaticon.com/512/7394/7394962.png" style="
                            width: 50px;
                            height: 50px;"></a></li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Leer Invernal' %}"><img src="https://cdn-icons-png.flaticon.com/512/3752/3752147.png" style="
                            width: 50px;
                            height: 50px;"></a></li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Leer Pantalon' %}"><img src="https://cdn-icons-png.flaticon.com/512/2793/2793865.png" style="
                            width: 50px;
                            height: 50px;"></a></li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Leer Jeans' %}"><img src="https://cdn-icons-png.flaticon.com/512/2806/2806058.png" style="
                            width: 50px;
                            height: 50px;"></a></li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Leer Calzado' %}"><img src="https://cdn-icons-png.flaticon.com/512/3199/3199876.png" style="
                            width: 50px;
                            height: 50px;"></a></li>
                        <li class="nav-item"><a class="nav-link" href="{% url 'Leer todo por 100' %}"><img src="https://cdn-icons-png.flaticon.com/512/5084/5084399.png" style="
                            width: 50px;
                            height: 50px;"></a></li>
                    </ul>
                    
                </div>
            </div>
        </nav>
        <!-- Header - set the background image for the header in the line below-->
        <header class="py-5 bg-image-full" style="background-image: url('https://www.diarioelinforme.com.ar/contenido/noticias/original/1550839520.jpeg');
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
        width: 100%;
        height: 100%;
        position: relative;">
            <div class="text-center my-1">
                <img class="img-fluid rounded-circle mb-4" src="https://cdn.icon-icons.com/icons2/3150/PNG/512/clothing_shop_bag_tshirt_icon_192654.png"
                style="
                background-color: rgb(127, 255, 193);
                width: 230px;
                height: 250px;
                position: relative;">
                
            

                {% block titulo %}


                {% endblock %}

                <p class="text-white-50 mb-0"></p>
                
                {% block descripcion %}



                {% endblock %}

            </div>
        </header>

        {% block pie %}


        {% endblock %}

        <!-- Footer-->
        <footer class="py-5 bg-dark">
            <div class="container">
                <div class="m-0 text-center text-white ">
                    <p class="m-0 text-center text-white">Copyright &copy; outlet_ini2 2022</p>
                </div>
            </div>
            <div class="conteiner">
                <div class="m-0 text-center text-white " >
                    <br>
                    <a href="https://www.instagram.com/outlet_ini2/?next=%2F" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" style="
                        width: 4%;
                        margin-right: 1%;"> outlet_ini2</a>
                    
                </div>
            </div>
        
        </footer>   
        <!-- Core theme JS-->
        <script src="{% static 'app_feria/js/scripts.js' %}"></script>
    </body>
</html>



"""








"""



<!DOCTYPE html>
<html lang="en">
    <head>
        {% load static %}
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Feria web</title>
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="{% static 'app_feria/assets/favicon.ico' %}" />
        <!-- Font Awesome icons (free version)-->
        <script src="https://use.fontawesome.com/releases/v6.1.0/js/all.js" crossorigin="anonymous"></script>
        <!-- Google fonts-->
        <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css" />
        <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="{% static 'app_feria/css/styles.css' %}" rel="stylesheet" />
        <style>
            body{
                background-image: url('https://www.diarioelinforme.com.ar/contenido/noticias/original/1550839520.jpeg');
                background-size: cover;
                width: 100%;
                position: relative;
            }
            nav{
                max-width: 100%;
                margin:auto;
                
                font-size: 25px;
            }
            .menu-horizontal{
                list-style: none;
                display:flex ;
                position: relative;
            }
            .menu-horizontal > li > a{
                
                display:block;
                padding: 5% 25%;
                color:white;
                text-decoration: none;
            }

            .menu-vertical{
                position:absolute;
                display:none;
                list-style: none;
                width: 200px;
                background-color: rgba(0, 0, 0, .5);
            }
            .menu-horizontal li:hover .menu-vertical{
                display: block;
            }
            .menu-vertical li:hover{
                background-color: black;
            }
            .menu-vertical li >a{
                display: block;
                color: white;
                padding: 15px 15px 15px 20px;
                text-decoration: none;
            }
           
        </style>
    </head>
    <body>
        <!-- Responsive navbar-->
        <nav class="bg-dark">
            <ul class="menu-horizontal">

                <li>

                    <a href="#"><img src="https://cdn-icons-png.flaticon.com/512/2099/2099043.png" style="
                        width: 17%;"></a>

                    <ul class="menu-vertical">
                        
                        <li><a href="{% url 'Iniciar_o_registrar' %}"><strong>Hola</strong>, Inicia tu sesión</a></li>

                        <li><a href="{% url 'Leer Remera' %}"><img src="https://cdn-icons-png.flaticon.com/512/5258/5258010.png" style="
                            width: 50px;"></a></li>

                        <li><a href="{% url 'Leer Camisas' %}"><img src="https://cdn-icons-png.flaticon.com/512/4722/4722182.png" style="
                            width: 50px;"></a></li>
                        
                        <li><a href="{% url 'Leer Campera' %}"><img src="https://cdn-icons-png.flaticon.com/512/7394/7394962.png" style="
                            width: 50px;"></a></li>
                        
                        <li><a href="{% url 'Leer Invernal' %}"><img src="https://cdn-icons-png.flaticon.com/512/3752/3752147.png" style="
                            width: 50px;"></a></li>
                        
                        <li><a href="{% url 'Leer Pantalon' %}"><img src="https://cdn-icons-png.flaticon.com/512/2793/2793865.png" style="
                            width: 50px;"></a></li>
                        
                        <li><a href="{% url 'Leer Jeans' %}"><img src="https://cdn-icons-png.flaticon.com/512/2806/2806058.png" style="
                            width: 50px;"></a></li>
                        
                        <li><a href="{% url 'Leer Calzado' %}"><img src="https://cdn-icons-png.flaticon.com/512/3199/3199876.png" style="
                            width: 50px;"></a></li>
                        
                        <li><a href="{% url 'Leer todo por 100' %}"><img src="https://cdn-icons-png.flaticon.com/512/5084/5084399.png" style="
                            width: 50px;"></a></li>
                    </ul>

                </li>
                <li>
                    {% if request.user.is_authenticated %}
                
                    <li><a href="{% url 'Inicio' %}">¡¡Feria Americana!!</a></li>
                    <li><a class="navbar-brand" href="{% url 'Editarosalir' %}"><strong>Hola </strong>{{user.username}}</a></li>

                    {% else %}
                    
                    <li><a href="{% url 'Inicio' %}">¡¡Feria Americana!!</a></li>
                    
                    {% endif %}
                </li>

            </ul>
            
        </nav>
        
        <!-- Header - set the background image for the header in the line below-->
        <div class="text-center my-1">
            <img class="img-fluid rounded-circle mb-4" src="https://cdn.icon-icons.com/icons2/3150/PNG/512/clothing_shop_bag_tshirt_icon_192654.png"
            style="
            background-color: rgb(127, 255, 193);
            width: 230px;
            height: 250px;
            position: relative;
            margin-top: 50px;">
            
        

            {% block titulo %}


            {% endblock %}

            <p class="text-white-50 mb-0"></p>
            
            {% block descripcion %}



            {% endblock %}

        </div>

        {% block pie %}


        {% endblock %}

        <!-- Footer-->
        <footer class="py-5 bg-dark" style="margin-top: 90px;">
            <div class="container">
                <div class="m-0 text-center text-white ">
                    <p class="m-0 text-center text-white">Copyright &copy; outlet_ini2 2022</p>
                </div>
            </div>
            <div class="conteiner">
                <div class="m-0 text-center text-white " >
                    <br>
                    <a href="https://www.instagram.com/outlet_ini2/?next=%2F" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" style="
                        width: 4%;
                        margin-right: 1%;"> outlet_ini2</a>
                    
                </div>
            </div>
        
        </footer>   
        <!-- Core theme JS-->
        <script src="{% static 'app_feria/js/scripts.js' %}"></script>
    </body>
</html>



"""