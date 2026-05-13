from flask import Flask, render_template, redirect, request, url_for, session
import pymysql
from modelo import *

app = Flask(__name__, template_folder='template')
app.secret_key = "Holahshjendhbhgbdghxbs"

# Configuración de MySQL
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "hola1234",
    "database": "serendipity",
    "cursorclass": pymysql.cursors.DictCursor
}

def get_connection():
    return pymysql.connect(**db_config)

@app.route('/')
def inicio():
    mysql = get_connection()
    return ruta_inicio(mysql, session)

@app.route('/registro')
def registro():
    return ruta_registro()

@app.route('/acceso-login', methods=["GET", "POST"])
def login():
    mysql = get_connection()
    return ruta_login(mysql, session, request)

@app.route('/crear-registro', methods=["POST"])
def hacer_registro(): 
    mysql = get_connection()
    return ruta_hacer_registro(mysql, session, request)

@app.route('/nueva-publicacion', methods=['GET', 'POST'])
def nueva_publicacion():
    mysql = get_connection()
    return vnuevapub_route(mysql, session, request)

@app.route('/logout')
def cerrar_sesion():
    mysql = get_connection()
    return ruta_cerrar_sesion(mysql, session)

@app.route('/menu-principal')
def menu_principal():
    mysql = get_connection()
    return ruta_menu_principal(mysql, session)

@app.route('/VMisPub')
def mis_publicaciones():
    mysql = get_connection()
    return ruta_mis_publicaciones(mysql, session)

@app.route('/borrar-publicacion', methods=['POST'])
def borrar_publicacion():
    mysql = get_connection()
    return ruta_borrar_publicacion(mysql, session, request)

@app.route('/editar_publicacion/<int:id_publicacion>', methods=["GET", "POST"])
def editar_publicacion(id_publicacion):
    mysql = get_connection()
    return ruta_editar_publicacion(mysql, session, request, id_publicacion)

@app.route('/agrandar-publicacion', methods=["POST"])
def agrandar_publicacion():
    mysql = get_connection()
    return ruta_agrandar_publicacion(mysql, session, request)

@app.route('/ruta-reaccionar', methods=['POST'])
def reaccionar():
    mysql = get_connection()
    return ruta_reaccionar(mysql, session, request)

@app.route('/agregar-comentario', methods=['POST'])
def agregar_comentario():
    mysql = get_connection()
    return ruta_agregar_comentario(mysql, session, request)

@app.route('/mostrar-perfil')
def mostrar_perfil():
    mysql = get_connection()
    return ruta_mostrar_perfil(mysql, session)

@app.route('/editar-informacion-personal', methods=['POST'])
def editar_informacion_personal():
    mysql = get_connection()
    return ruta_editar_informacion_personal(mysql, session, request)

@app.route('/mostrar-grafica')
def mostrar_grafica():
    mysql = get_connection()
    return ruta_mostrar_grafica(mysql)


@app.route('/chat')
def chat():
    mysql = get_connection()
    return ruta_chat(mysql, session)
   

@app.route('/buscar_usuario', methods=['GET', 'POST'])
def buscar_usuario():
    if request.method == 'POST':
        mysql = get_connection()
        return buscar_e_iniciar_chat(mysql, session, request)

@app.route('/iniciar_conversacion/<int:id_usuario_destino>')
def iniciar_conversacion_route(id_usuario_destino):
    mysql = get_connection()
    return iniciar_conversacion(mysql, session, id_usuario_destino)

@app.route('/enviar_mensaje', methods=['POST'])
def enviar_mensaje():
    mysql = get_connection()
    return ruta_enviar_mensaje(mysql, session, request)

@app.route('/ver_conversacion/<int:conversacion_id>')
def ver_conversacion_route(conversacion_id):
    mysql = get_connection()
    return ver_conversacion(mysql, session, conversacion_id)


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
