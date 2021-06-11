from flask import Flask, render_template, jsonify, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nombre')
def nombre():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    data = []
    for row in cur.execute("SELECT * FROM EstudianteLista"):
        data.append({'nombre':row[1]})
    con.close()
    return jsonify(data)

@app.route('/carreras')
def carreras():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    data = []
    for row in cur.execute("SELECT * FROM Carreras"):
        data.append({'carrera':row[1]})
    con.close()
    return jsonify(data)

@app.route('/clases',methods=['POST'])
def clases():
    carrera = request.form.getlist('carrera')[0]
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM Carreras WHERE Carrera ='"+carrera+"'"):
        pass
    idCarrera = row[0]
    data = []
    for row in cur.execute("SELECT * FROM Clases WHERE CarreraId ="+str(idCarrera)):
        data.append({'clase':row[2]})
    con.close()
    return jsonify(data)

@app.route('/mentores',methods=['POST'])
def mentores():
    clase = request.form.getlist('clase')[0]
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM Clases WHERE Clase ='"+clase+"'"):
        pass
    idClase = row[1]
    data = []
    for row in cur.execute("SELECT * FROM Mentores WHERE ClaseId ="+str(idClase)):
        data.append({'mentor':row[2]})
    con.close()
    return jsonify(data)

@app.route('/registro',methods=['POST'])
def registro():
    if request.method == "POST":
        nombre = request.form.getlist('nombre')[0]
        carrera = request.form.getlist('carrera')[0]
        clase = request.form.getlist('clase')[0]
        mentor = request.form.getlist('mentor')[0]
        clase = request.form.getlist('clase')[0]
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        exist = False
        for row in cur.execute("SELECT * FROM EstudianteLista WHERE Estudiante ='"+nombre+"'"):
            pass
        idEst = row[0]
        for row in cur.execute("SELECT * FROM Clases WHERE Clase ='"+clase+"'"):
            pass
        idClase = row[1]
        for row in cur.execute("SELECT * FROM Mentores WHERE Mentor ='"+mentor+"'"):
            pass
        idMentor = row[1]
        exist = True
        for row in cur.execute("SELECT * FROM Estudiantes WHERE ClaseId = "+str(idClase)+" and EstudianteId = "+str(idEst)):
            exist = False
        if exist:
            cur.execute("INSERT INTO Estudiantes(EstudianteId,Estudiante,ClaseId,MentorId) VALUES ("+str(idEst)+",'"+nombre+"',"+str(idClase)+","+str(idMentor)+")")
            con.commit()
            con.close()
            return jsonify({"existe":False})
        else:
            con.close()
            return jsonify({"existe":True})

@app.route("/lista")
def lista():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    carreras = []
    carrerasId = []
    for row in cur.execute("SELECT * FROM Carreras"):
        carrerasId.append(row[0])
        carreras.append(row[1])
    clase = []
    for i in carrerasId:
        aux = []
        for j in cur.execute("SELECT * FROM Clases WHERE CarreraId = "+str(i)):
            aux.append(j[2])
        clase.append(aux)
    con.close()
    return render_template('clases.html',clase=clase,carreras=carreras,leng=len(carreras))

@app.route("/cursos/<string:clase>")
def cursos(clase):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    mentores = []
    alumnos=[]
    for row in cur.execute("SELECT * FROM Clases WHERE clase = '"+clase+"'"):
        pass
    claseId = row[1]
    for row in cur.execute("SELECT * FROM Mentores WHERE claseId = "+str(claseId)):
        mentores.append(row[2])
    for row in cur.execute("SELECT * FROM Estudiantes WHERE claseId = "+str(claseId)):
        alumnos.append([row[0],row[2]])
    con.close()
    return render_template('clase.html',clase=clase,mentores=mentores,alumnos=alumnos),200

@app.route("/borrar/<string:clase>/<string:idu>")
def borrar(clase,idu):
    print(idu)
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("DELETE FROM Estudiantes WHERE id="+idu)
    con.commit()
    con.close()
    return redirect(url_for('cursos',clase=clase))
app.run(debug=True,host='0.0.0.0',port=80)

