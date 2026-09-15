nombre_estudiante = input("Ingresa tu nombre: ")
calificacion_1 = float(input(f"Hola, {nombre_estudiante}! Bienvenid@ a EduTech Solutions, vamos a calcular tu situación académica, por favor digita tu primer calificación entre 0 y 100: "))
calificacion_2 = float(input("Por favor digita tu segunda calificación: "))
calificacion_3 = float(input("Por favor digita tu tercera calificación: "))
calificacion_4 = float(input("Por favor digita tu cuarta calificación: "))
calificacion_5 = float(input("Por favor digita tu quinta calificación: "))
suma_calificaciones = calificacion_1 + calificacion_2 + calificacion_3 + calificacion_4 + calificacion_5
promedio = suma_calificaciones / 5
print(f"{nombre_estudiante}, tu promedio académico es: {promedio:.2f}")
if promedio >= 60:
    print("Aprobado")
elif promedio >= 40:
    print("En recuperación")
else:
    print("Reprobado")