from django.urls import path
from app_feria.views import *
from django.contrib.auth.views import LogoutView
from app_feria import views


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('editar_registro/', editar_registro, name="Editarosalir"),
    path('registro_inicio/', registro_inicio, name="Iniciar_o_registrar"),
    path('sobrenostros/', sobrenosotros, name="Sobrenosotros"),

    path('jean_detail/<int:codigo>/', views.jean_detail, name="Detalle"),
    path('remera_detail/<int:codigo>/', views.remera_detail, name="Detalle_remera"),
    path('camisa_detail/<int:codigo>/', views.camisa_detail, name="Detalle_camisa"),
    path('calzado_detail/<int:codigo>/', views.calzado_detail, name="Detalle_calzado"),
    path('todo100_detail/<int:codigo>/', views.todo100_detail, name="Detalle_todo100"),
    path('invernal_detail/<int:codigo>/', views.invernal_detail, name="Detalle_invernal"),
    path('pantalon_detail/<int:codigo>/', views.pantalon_detail, name="Detalle_pantalon"),
    path('campera_detail/<int:codigo>/', views.campera_detail, name="Detalle_campera"),


#URL DE CREACION
    path('formulario1/', formulariojean, name="Crear Jeans"),
    path('formulario2/', formularioremera, name="Crear Remera"),
    path('formulario3/', formulariocamisa, name="Crear Camisa"),
    path('formulario4/', formulariotodo, name="Crear todo por 100"),
    path('formulario5/', formulariocalzado, name="Crear Calzado"),
    path('formulario6/', formularioinvernal, name="Crear Invernal"),
    path('formulario7/', formulariopantalon, name="Crear Pantalon"),
    path('formulario8/', formulariocampera, name="Crear Campera"),



#URL DE LEER
    path('leerJeans',leerJeans, name="Leer Jeans"),
    path('leerRemera/',leerRemera, name="Leer Remera"),
    path('leerCamisas/',leerCamisa, name="Leer Camisas"),
    path('leerTodo100/',leerTodo, name="Leer todo por 100"),
    path('leerCalzado/',leerCalzado, name="Leer Calzado"),
    path('leerInvernal/',leerInvernal, name="Leer Invernal"),
    path('leerPantalon/',leerPantalon, name="Leer Pantalon"),
    path('leerCampera',leerCampera, name="Leer Campera"),



#URL DE EDICION
    path('editaJean/<numJean>/', editaJean, name = "EditaJean"),
    path('editarRemera/<generoRemera>/', editarRemera, name = "EditarRemera"),
    path('editarCamisa/<generoCamisa>/', editarCamisa, name = "EditarCamisa"),
    path('editarTodo/<generoTodo>/', editarTodo, name = "Editar todo por 100"),
    path('editarCalzado/<generoCalzado>/', editarCalzado, name = "EditarCalzado"),
    path('editarInvernal/<generoInvernal>/', editarInvernal, name = "EditarInvernal"),
    path('editarPantalon/<generoPantalon>/', editarPantalon, name = "EditarPantalon"),
    path('editarCampera/<generoCampera>/', editarCampera, name = "EditarCampera"),


#URL DE ELIMINACION
    path('eliminaJean/<numJean>/', eliminaJean, name = "EliminaJean"),
    path('eliminaRemera/<generoRemera>/', eliminaRemera, name = "EliminaRemera"),
    path('eliminaCamisa/<generoCamisa>/', eliminaCamisa, name = "EliminaCamisa"),
    path('eliminaTodo/<generoTodo>/', eliminaTodo, name = "Elimina todo por 100"),
    path('eliminaCalzado/<generoCalzado>/', eliminaCalzado, name = "EliminaCalzado"),
    path('eliminaInvernal/<generoInvernal>/', eliminaInvernal, name = "EliminaInvernal"),
    path('eliminaPantalon/<generoPantalon>/', eliminaPantalon, name = "EliminaPantalon"),
    path('eliminaCampera/<generoCampera>/', eliminaCampera, name = "EliminaCampera"),


#URL DE BUSQUEDAS
    path('bus/', bus, name="Buscar"),

##
    path('buscar_campe/',buscar_campe),
    path('buscar_panta/',buscar_panta),
    path('buscar_inve/',buscar_inve),
    path('buscar_calza/',buscar_calza),
    path('buscar_cami/',buscar_cami),
    path('buscar_rem/',buscar_rem),
    path('buscar/',buscar),


#URL DE LOGIN Y LOGOUT
    path('login/',InicioSesion, name="Login"),
    path('registro/',registro, name="Registrarse"),
    path('logout/', LogoutView.as_view(template_name="app_feria/logout.html"), name="Logout"),


#URL DE EDICIONUSUARIO
    path('editUser/',editarUsuario, name="Editar Usuario"),
    
    ]


"""
<li align="center"; class="nav-item"><a class="m-0 text-center text-white" href="{% url 'Sobrenosotros' %}">About</a></li>

"""