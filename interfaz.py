import tkinter as tk
from tkinter import messagebox
from reglas import DiagnosticoSistema, Sintomas, CaracteristicasPaciente

# Crear ventana principal
root = tk.Tk()
root.title("Diagnóstico Odontológico")
root.geometry("800x700")

# Crear Frame principal
main_frame = tk.Frame(root)
main_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Frame para los síntomas a la izquierda
sintomas_frame = tk.LabelFrame(main_frame, text="Síntomas del Paciente", padx=10, pady=10)
sintomas_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

# Frame para las características a la derecha de los síntomas
caracteristicas_frame = tk.LabelFrame(main_frame, text="Características del Paciente", padx=10, pady=10)
caracteristicas_frame.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

# Variables de interfaz para los síntomas
sintomas_vars = {
    "pus": tk.BooleanVar(),
    "dolor_pulpa_dental": tk.BooleanVar(),
    "fiebre": tk.BooleanVar(),
    "manchas_blancas_removibles": tk.BooleanVar(),
    "defensas_bajas": tk.BooleanVar(),
    "llagas_persistentes": tk.BooleanVar(),
    "problemas_neurologicos": tk.BooleanVar(),
    "dificultad_cerrar_boca": tk.BooleanVar(),
    "inflamacion": tk.BooleanVar(),
    "perdida_estructura_dental": tk.BooleanVar(),
    "sangrado": tk.BooleanVar(),
    "patologia_grave": tk.BooleanVar(),
    "flemon": tk.BooleanVar(),
    "infeccion_cuello_torax": tk.BooleanVar(),
    "heridas_sucias": tk.BooleanVar(),
    "infeccion_resistente_a_antibioticos": tk.BooleanVar(),
    "muela_juicio_retenida": tk.BooleanVar(),
    "bruxismo": tk.BooleanVar(),
    "estres_mala_oclusion": tk.BooleanVar(),
    "lesiones_cronicas": tk.BooleanVar(),
    "caries_profunda": tk.BooleanVar(),
    "presencia_quiste": tk.BooleanVar(),
}

# Crear checkboxes para los síntomas en el Frame de síntomas
for sintoma, var in sintomas_vars.items():
    tk.Checkbutton(sintomas_frame, text=sintoma.replace("_", " ").capitalize(), variable=var).pack(anchor='w')

# Variables para las características del paciente
alergia_var = tk.BooleanVar()
peso_superior_promedio_var = tk.BooleanVar()  # Nueva variable

# Entrada para características (alergia y peso) en el Frame de características
tk.Checkbutton(caracteristicas_frame, text="Alergia a la penicilina", variable=alergia_var).pack(anchor='w')
tk.Checkbutton(caracteristicas_frame, text="Peso superior al promedio", variable=peso_superior_promedio_var).pack(anchor='w')  # Nuevo checkbox

tk.Label(caracteristicas_frame, text="Edad del paciente:").pack(anchor='w')
edad_var = tk.IntVar()
tk.Entry(caracteristicas_frame, textvariable=edad_var).pack(anchor='w')

# Frame para los resultados
resultados_frame = tk.Frame(main_frame)
resultados_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ns")

# Área de texto para mostrar el diagnóstico
diagnostico_text = tk.Text(resultados_frame, height=11, width=35, wrap="word", state="disabled")
diagnostico_text.pack(pady=5)

# Área de texto para mostrar el tratamiento
tratamiento_text = tk.Text(resultados_frame, height=11, width=35, wrap="word", state="disabled")
tratamiento_text.pack(pady=5)

# Área de texto para mostrar consideraciones
consideraciones_text = tk.Text(resultados_frame, height=11, width=35, wrap="word", state="disabled")
consideraciones_text.pack(pady=5)

# Función para generar el diagnóstico y tratamiento
def generar_receta():
    # Verificar si el campo de edad está lleno
    if edad_var.get() <= 0:
        messagebox.showwarning("Advertencia", "Por favor, ingrese la edad del paciente.")
        return

    # Crear una nueva instancia del sistema experto y reiniciar
    engine = DiagnosticoSistema()
    engine.reset()  # Reinicia el motor para eliminar hechos previos

    # Recopilar y declarar los síntomas seleccionados
    sintomas_seleccionados = {sintoma: var.get() for sintoma, var in sintomas_vars.items() if var.get()}
    if sintomas_seleccionados:
        
        engine.declare(Sintomas(**sintomas_seleccionados))

    # Declarar la característica de alergia si está marcada
    if alergia_var.get():
        
        engine.declare(CaracteristicasPaciente(alergia_penicilina=True))
    
    # Declarar la característica de peso superior al promedio si está marcada
    if peso_superior_promedio_var.get():
        
        engine.declare(CaracteristicasPaciente(peso_superior_promedio=True))
    
    # Declarar la edad del paciente
    engine.declare(CaracteristicasPaciente(edad=edad_var.get()))

    # Ejecutar el sistema experto
    engine.run()

    # Obtener y mostrar diagnóstico, tratamiento y consideraciones
    receta = engine.obtener_receta()

    # Mostrar diagnóstico
    diagnostico_text.config(state="normal")
    diagnostico_text.delete(1.0, tk.END)
    diagnostico_text.insert(tk.END, "Diagnósticos:\n" + "\n".join(f"- {d}" for d in receta["diagnosticos"]))
    diagnostico_text.config(state="disabled")

    # Mostrar tratamiento
    tratamiento_text.config(state="normal")
    tratamiento_text.delete(1.0, tk.END)
    tratamiento_text.insert(tk.END, "Tratamientos:\n" + "\n".join(f"- {t}" for t in receta["tratamientos"]))
    tratamiento_text.config(state="disabled")

    # Mostrar consideraciones
    consideraciones_text.config(state="normal")
    consideraciones_text.delete(1.0, tk.END)
    consideraciones_text.insert(tk.END, "Consideraciones:\n" + "\n".join(f"- {c}" for c in receta["consideraciones"]))
    consideraciones_text.config(state="disabled")

# Botón para generar la guía
tk.Button(main_frame, text="Generar Guía", command=generar_receta).grid(row=2, column=2, sticky="ew")

# Ejecutar la aplicación
root.mainloop()
