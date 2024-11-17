from experta import *

class Sintomas(Fact):
    """Clase para hechos de síntomas del paciente."""
    pass

class CaracteristicasPaciente(Fact):
    """Clase para hechos relacionados con características del paciente."""
    pass

class Diagnostico(Fact):
    """Clase para hechos de diagnóstico."""
    pass

class Tratamiento(Fact):
    """Clase para hechos de tratamiento."""
    pass

class Consideracion(Fact):
    """Clase para hechos de consideraciones sobre el tratamiento."""
    pass

class DiagnosticoSistema(KnowledgeEngine):
    """Sistema experto para diagnosticar y recomendar tratamiento."""

    @DefFacts()
    def hechos_iniciales(self):
        yield Fact(diagnostico_iniciado=True)

    # Reglas

    @Rule(Sintomas(pus=True, dolor_pulpa=True, fiebre=True))
    def regla_R1(self):
        print("Regla R1 activada: Infección Bacteriana")
        self.declare(Diagnostico(diagnostico="Infección Bacteriana"))
        self.declare(Tratamiento(tratamiento="Aplicar Antibióticos"))


    # R2: Infección fúngica por manchas blancas y defensas bajas
    @Rule(Sintomas(manchas_blancas_removibles=True, defensas_bajas=True))
    def regla_R2(self):
        print("Regla R2 activada: Infección Fúngica")
        self.declare(Diagnostico(diagnostico="Infección Fúngica"))
        self.declare(Tratamiento(tratamiento="Aplicar Antimicóticos"))

    # R3: Infección vírica por llagas persistentes
    @Rule(Sintomas(llagas_persistentes=True))
    def regla_R3(self):
        print("Regla R3 activada: Infección Vírica")
        self.declare(Diagnostico(diagnostico="Infección Vírica"))
        self.declare(Tratamiento(tratamiento="Aplicar Antivirales"))
        self.declare(Tratamiento(tratamiento="Realizar Biopsia"))

    # R4: Infección parasitaria por problemas neurológicos y dificultad para cerrar la boca
    @Rule(Sintomas(problemas_neurologicos=True, dificultad_cerrar_boca=True))
    def regla_R4(self):
        print("Regla R4 activada: Infección Parasitaria")
        self.declare(Diagnostico(diagnostico="Infección Parasitaria"))
        self.declare(Tratamiento(tratamiento="Realizar extracción de larvas"))

    # R5: Infección periodontal por inflamación, pérdida de estructura dental y sangrado
    @Rule(Sintomas(inflamacion=True, perdida_estructura_dental=True, sangrado=True))
    def regla_R5(self):
        print("Regla R5 activada: Infección Periodontal")
        self.declare(Diagnostico(diagnostico="Infección Periodontal"))
        self.declare(Tratamiento(tratamiento="Aplicar tratamiento periodontal específico"))

    # R6: Medicación infantil
    @Rule(CaracteristicasPaciente(edad=P(lambda x: x < 15)), Tratamiento(tratamiento="Aplicar Antibióticos"))
    def regla_R6(self):
        print("Regla R6 activada: Consideraciones para niños")
        self.declare(Tratamiento(tratamiento="Administrar medicamento en suspensión"))
        self.declare(Consideracion(consideracion="Evitar aminoglucósidos y tetraciclinas"))
        self.declare(Consideracion(consideracion="Ajustar dosis según peso"))

    # R7: Medicación ajustada para adolescentes con peso superior al promedio
    @Rule(CaracteristicasPaciente(edad=P(lambda x: 12 <= x <= 13), peso_superior_promedio=True))
    def regla_R7(self):
        print("Regla R7 activada: Ajuste de medicación para adolescentes")
        self.declare(Consideracion(consideracion="Considerar comprimidos"))
        self.declare(Consideracion(consideracion="Ajustar dosis según peso"))

    # R8: Alergia a penicilina
    @Rule(
        CaracteristicasPaciente(alergia_penicilina=True),
        Tratamiento(tratamiento="Aplicar Antibióticos")
    )
    def regla_R8(self):
        print("Regla R8 activada: Sustituir antibióticos por clindamicina o azitromicina")
        self.declare(Consideracion(consideracion="Aplicar clindamicina o azitromicina"))


    # R9: Patología grave
    @Rule(Sintomas(patologia_grave=True))
    def regla_R9(self):
        print("Regla R9 activada: Tratamiento para patología grave")
        self.declare(Consideracion(consideracion="Administrar dosis de ataque"))
        self.declare(Consideracion(consideracion="Aumentar frecuencia de administración"))

    # R10: Tratamiento para dolor en pulpa dental e inflamación
    @Rule(Sintomas(dolor_pulpa=True, inflamacion=True))
    def regla_R10(self):
        print("Regla R10 activada: Infección Bacteriana con tratamiento dental")
        self.declare(Diagnostico(diagnostico="Infección Bacteriana"))
        self.declare(Tratamiento(tratamiento="Aplicar Antibióticos"))
        self.declare(Tratamiento(tratamiento="Realizar tratamiento de conducto"))


    # R12: Flemón grave
    @Rule(Sintomas(flemon=True, patologia_grave=True))
    def regla_R12(self):
        print("Regla R12 activada: Tratamiento para flemón grave")
        self.declare(Tratamiento(tratamiento="Aplicar penicilina + gentamicina + metronidazol"))
        self.declare(Tratamiento(tratamiento="Administrar dexametasona"))

    # R13: Infección extendida a cuello/tórax
    @Rule(Sintomas(infeccion_cuello_torax=True))
    def regla_R13(self):
        print("Regla R13 activada: Tratamiento urgente para infección grave")
        self.declare(Tratamiento(tratamiento="Hospitalización urgente"))
        self.declare(Tratamiento(tratamiento="Antibióticos intravenosos"))
        self.declare(Tratamiento(tratamiento="Cirugía con anestesia general"))

    # R14: Heridas sucias
    @Rule(Sintomas(heridas_sucias=True))
    def regla_R14(self):
        print("Regla R14 activada: Limpieza de heridas")
        self.declare(Tratamiento(tratamiento="Limpiar y desinfectar herida"))

    # R15: Infección resistente a antibióticos
    @Rule(Sintomas(infeccion_resistente=True))
    def regla_R15(self):
        print("Regla R15 activada: Cefalosporinas para infección resistente")
        self.declare(Tratamiento(tratamiento="Aplicar cefalosporinas de tercera generación"))

   # R16: Muela del juicio retenida
    @Rule(Sintomas(muela_juicio_retenida=True))
    def regla_R16(self):
        print("Regla R16 activada: Muela del juicio retenida")
        self.declare(Diagnostico(diagnostico="Muela del juicio retenida"))
        self.declare(Tratamiento(tratamiento="Evaluación de quiste"))
        self.declare(Tratamiento(tratamiento="Extracción quirúrgica"))
        self.declare(Consideracion(consideracion="Seguimiento periódico"))

    # R17: Bruxismo y estrés o mala oclusión
    @Rule(Sintomas(bruxismo=True, estres_mala_oclusion=True))
    def regla_R17(self):
        print("Regla R17 activada: Bruxismo con estrés o mala oclusión")
        self.declare(Diagnostico(diagnostico="Bruxismo"))
        self.declare(Tratamiento(tratamiento="Evaluación de ATM"))
        self.declare(Tratamiento(tratamiento="Tratamiento de ATM"))
        self.declare(Consideracion(consideracion="Seguimiento periódico"))

    # R18: Lesiones crónicas en lengua/mucosas
    @Rule(Sintomas(lesiones_cronicas=True))
    def regla_R18(self):
        print("Regla R18 activada: Lesiones crónicas en lengua o mucosas")
        self.declare(Diagnostico(diagnostico="Lesiones crónicas en lengua/mucosas"))
        self.declare(Tratamiento(tratamiento="Evaluación de cáncer oral"))
        self.declare(Consideracion(consideracion="Seguimiento periódico"))

    # R19: Caries profunda
    @Rule(Sintomas(caries_profunda=True))
    def regla_R19(self):
        print("Regla R19 activada: Caries profunda")
        self.declare(Diagnostico(diagnostico="Caries profunda"))
        self.declare(Tratamiento(tratamiento="Tratamiento de conducto"))
        self.declare(Consideracion(consideracion="Seguimiento periódico"))

    # R20: Presencia de quiste
    @Rule(Sintomas(presencia_quiste=True))
    def regla_R20(self):
        print("Regla R20 activada: Presencia de quiste")
        self.declare(Diagnostico(diagnostico="Presencia de quiste"))
        self.declare(Tratamiento(tratamiento="Evaluación de quiste"))
        self.declare(Tratamiento(tratamiento="Remoción de quiste"))
        self.declare(Consideracion(consideracion="Seguimiento periódico"))

    # R21
    @Rule(Sintomas(flemon=True))
    def regla_R21(self):
        self.declare(Diagnostico(diagnostico="Infección Bacteriana"))
        self.declare(Tratamiento(tratamiento="Aplicar Antibióticos"))
        self.declare(Tratamiento(tratamiento="Extraer Pus"))

    # Método para obtener la receta generada
    def obtener_receta(self):
        receta = {
            "diagnosticos": [],
            "tratamientos": [],
            "consideraciones": []
        }
        for hecho in self.facts.values():
            if isinstance(hecho, Diagnostico):
                receta["diagnosticos"].append(hecho["diagnostico"])
            if isinstance(hecho, Tratamiento):
                receta["tratamientos"].append(hecho["tratamiento"])
            if isinstance(hecho, Consideracion):
                receta["consideraciones"].append(hecho["consideracion"])
        return receta
