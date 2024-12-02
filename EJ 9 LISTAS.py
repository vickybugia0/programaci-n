planificacion_vuelos = [
    [["08:00", "AeroAir"], ["12:00", "SkyLine"]], 
    [["09:00", "AirConnect"], ["14:00", "SwiftJet"]],  
    [["07:30", "JetSet"], ["16:00", "GlobalWings"]],  
    [["10:00", "FlyDirect"]],  
    [["11:00", "SwiftJet"], ["18:00", "AeroAir"]],  
    [["07:00", "GlobalWings"]],  
    [["20:00", "JetSet"]]  
]

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for i, dia in enumerate(dias):
    print(f"\n{dia}:")
    for vuelo in planificacion_vuelos[i]:
        print(f"  Hora: {vuelo[0]} | Compañía: {vuelo[1]}")