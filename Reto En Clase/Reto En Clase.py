def inicio_reaccion(codigo: str, hora_terminacion: int, minuto_terminacion: int,
                    duracion_horas:int, duracion_minutos:int, duracion_segundos:int):
    horaseg = hora_terminacion*3600
    minseg = minuto_terminacion*60
    seg1 = horaseg+minseg
    horaseg2 = duracion_horas*3600
    minseg2 = duracion_minutos*60
    seg2 = horaseg2+minseg2+duracion_segundos
    totalseg = seg1-seg2
    hh = totalseg // 3600
    mm = (totalseg - (hh*3600)) // 60
    mms = str(mm).zfill(2)
    ss = totalseg-((mm*60)+(hh*3600))
    sss = str(ss).zfill(2)
    return f"La reacción {codigo} debe iniciarse a las {hh} horas, {mms} minutos con {sss} segundos para que esté lista en en el momento requerido"

reac1 = inicio_reaccion('HHA01', 16, 30, 4, 11, 23)
print(reac1)

reac2 = inicio_reaccion('IQ200', 16, 30, 7, 24, 58)
print(reac2)
