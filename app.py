from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Cambia esto a una clave secreta más segura

@app.route('/')
def index():
    productos = session.get('productos', [])
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        id_producto = request.form['id']
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        fecha_vencimiento = request.form['fecha_vencimiento']
        categoria = request.form['categoria']

        # Verificar que el ID sea único
        productos = session.get('productos', [])
        if any(prod['id'] == id_producto for prod in productos):
            flash('El ID del producto ya existe. Intenta con otro.', 'error')
            return redirect('/agregar')

        nuevo_producto = {
            'id': id_producto,
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio,
            'fecha_vencimiento': fecha_vencimiento,
            'categoria': categoria
        }

        productos.append(nuevo_producto)
        session['productos'] = productos
        flash('Producto agregado exitosamente.', 'success')
        return redirect('/')

    return render_template('agregar_producto.html')

@app.route('/eliminar/<id_producto>', methods=['POST'])
def eliminar_producto(id_producto):
    productos = session.get('productos', [])
    productos = [prod for prod in productos if prod['id'] != id_producto]
    session['productos'] = productos
    flash('Producto eliminado exitosamente.', 'success')
    return redirect('/')

@app.route('/editar/<id_producto>', methods=['GET', 'POST'])
def editar_producto(id_producto):
    productos = session.get('productos', [])
    producto_a_editar = next((prod for prod in productos if prod['id'] == id_producto), None)

    if request.method == 'POST':
        producto_a_editar['nombre'] = request.form['nombre']
        producto_a_editar['cantidad'] = request.form['cantidad']
        producto_a_editar['precio'] = request.form['precio']
        producto_a_editar['fecha_vencimiento'] = request.form['fecha_vencimiento']
        producto_a_editar['categoria'] = request.form['categoria']

        session['productos'] = productos
        flash('Producto editado exitosamente.', 'success')
        return redirect('/')

    return render_template('editar_producto.html', producto=producto_a_editar)

if __name__ == '__main__':
    app.run(debug=True)

