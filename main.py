from flask import Flask, request, render_template

app = Flask(__name__)

def calcular_promedio(nota1,nota2,nota3):
    return (nota1 + nota2 + nota3) / 3

@app.route('/')
def index():
    return render_template('index.html')
#Ejercicio 1:
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = calcular_promedio(nota1, nota2, nota3)

        if promedio < 40:
            estado = 'REPROBADO'
        elif asistencia < 75:
            estado = 'REPROBADO'
        else:
            estado = 'APROBADO'

        return render_template('ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')
#Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        if len(nombre1) > len(nombre2) and len(nombre1) > len(nombre3):
            nombre_mayor = nombre1
        elif len(nombre2) > len(nombre1) and len(nombre2) > len(nombre3):
            nombre_mayor = nombre2
        else:
            nombre_mayor = nombre3

        cantidad = len(nombre_mayor)

        return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, cantidad=cantidad)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)