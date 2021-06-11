import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Carreras(
 CarreraId INTEGER PRIMARY KEY AUTOINCREMENT,
 Carrera VARCHAR(255)
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS Clases(
 Id INTEGER PRIMARY KEY AUTOINCREMENT,
 ClaseId INTEGER,
 Clase VARCHAR(255),
 CarreraId INTEGER,
 FOREIGN KEY(CarreraId) REFERENCES Carreras(CarreraId)
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS Mentores(
 Id INTEGER PRIMARY KEY AUTOINCREMENT,
 MentorId INTEGER,
 Mentor VARCHAR(255),
 ClaseId INTEGER,
 FOREIGN KEY(ClaseId) REFERENCES Clases(ClaseId)
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS Estudiantes(
 Id INTEGER PRIMARY KEY AUTOINCREMENT,
 EstudianteId INTEGER,
 Estudiante VARCHAR(255),
 ClaseId INTEGER,
 MentorId INTEGER,
 FOREIGN KEY(ClaseId) REFERENCES Clases(ClaseIds)
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS EstudianteLista(
 Id INTEGER PRIMARY KEY AUTOINCREMENT,
 Estudiante VARCHAR(255)
);
''')
cur.execute("INSERT INTO Carreras(Carrera) VALUES ('Ingeniería')")
cur.execute("INSERT INTO Carreras(Carrera) VALUES ('Administración')")
cur.execute("INSERT INTO Clases(ClaseId,Clase,CarreraId) VALUES (1,'Matematicas',1)")
cur.execute("INSERT INTO Clases(ClaseId,Clase,CarreraId) VALUES (1,'Matematicas',2)")
cur.execute("INSERT INTO Clases(ClaseId,Clase,CarreraId) VALUES (2,'Finanzas',2)")
cur.execute("INSERT INTO Clases(ClaseId,Clase,CarreraId) VALUES (3,'Fisica',1)")
cur.execute("INSERT INTO Mentores(MentorId,Mentor,ClaseId) VALUES (1,'Jorge',1)")
cur.execute("INSERT INTO Mentores(MentorId,Mentor,ClaseId) VALUES (1,'Jorge',2)")
cur.execute("INSERT INTO Mentores(MentorId,Mentor,ClaseId) VALUES (2,'Pablo',1)")
cur.execute("INSERT INTO Mentores(MentorId,Mentor,ClaseId) VALUES (3,'Lucas',3)")
cur.execute("INSERT INTO EstudianteLista(Estudiante) VALUES ('Andrés')")
cur.execute("INSERT INTO EstudianteLista(Estudiante) VALUES ('Raúl')")
cur.execute("INSERT INTO EstudianteLista(Estudiante) VALUES ('Herrera')")
con.commit()
con.close()
