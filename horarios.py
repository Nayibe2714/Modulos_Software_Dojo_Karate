import pyomo.environ as pyo
dias = [ "lunes", "Martes", "Miercoles", "Jueves", "Viernes","Sabado", "Domingo"]
horas = [f"h_{i}" for i in range (10, 20)]
clase = [f"SB_{i}" for i in range (2)]

modelo= pyo.ConcreteModel()
modelo.sDias=pyo.Set(initialize=dias)
modelo.sHoras= pyo.Set(initialize=horas)
modelo.sClase=pyo.Set(initialize=clase)

modelo.vbClaseHorario = pyo.Var(modelo.sDias, modelo.sHoras, modelo.SClase, domain=pyo.Binary)

