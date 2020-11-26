def prestamo(informacion: dict) -> dict:
    '''Determinar si el prestamo es aprobado'''
    if informacion['historia_credito'] == 1:
        if (informacion['ingreso_codeudor'] > 0) and ((informacion['ingreso_deudor'] / 9) > informacion['cantidad_prestamo']):
            informacion['aprobado'] = True
        else:
            if (informacion['dependientes'] == '3+') and (informacion['independiente'] == 'Si'):
                if (informacion['ingreso_codeudor'] / 12) > informacion['cantidad_prestamo']:
                    informacion['aprobado'] = True
                else:
                    informacion['aprobado'] = False                
            else:
                if informacion['cantidad_prestamo'] < 200:
                    informacion['aprobado'] = True
                else:
                    informacion['aprobado'] = False
    else:
        if (informacion['independiente'] == 'Si'):
            if not ((informacion['casado'] == 'Si') and ((informacion['dependientes'] == 2) or (informacion['dependientes'] == '3+'))):
                if (((informacion['ingreso_deudor'] / 10) > informacion['cantidad_prestamo']) or
                    ((informacion['ingreso_codeudor'] / 10) > informacion['cantidad_prestamo'])):
                    if informacion['cantidad_prestamo'] < 180:
                        informacion['aprobado'] = True
                    else:
                        informacion['aprobado'] = False                    
                else:
                    informacion['aprobado'] = False
            else:
                informacion['aprobado'] = False
        else:
            if ((informacion['tipo_propiedad'] != 'Semiurbano') and ((informacion['dependientes'] == 0) or
                                                                     (informacion['dependientes'] == 1))):
                if (informacion['educacion'] == 'Graduado'):
                    if ((informacion['ingreso_deudor'] / 11) > informacion['cantidad_prestamo']) and ((informacion['ingreso_codeudor'] / 11) > informacion['cantidad_prestamo']):
                        informacion['aprobado'] = True
                    else:
                        informacion['aprobado'] = False                    
                else:
                    informacion['aprobado'] = False
            else:
                informacion['aprobado'] = False
    return {'id_prestamo':informacion['id_prestamo'], 'aprobado':informacion['aprobado']}

print(prestamo({'id_prestamo':'RETOS2_001', 'casado':'No', 'dependientes':1, 'educacion':'Graduado', 'independiente':'Si',
                'ingreso_deudor':4692, 'ingreso_codeudor':0, 'cantidad_prestamo':106, 'plazo_prestamo':360,
                'historia_credito':1, 'tipo_propiedad':'Rural'}))

print(prestamo({'id_prestamo':'RETOS2_002', 'casado':'No', 'dependientes':'3+', 'educacion':'No Graduado', 'independiente':'No',
                'ingreso_deudor':1830, 'ingreso_codeudor':0, 'cantidad_prestamo':100, 'plazo_prestamo':360,
                'historia_credito':0, 'tipo_propiedad':'Urbano'}))

print(prestamo({'id_prestamo':'RETOS2_003', 'casado':'No', 'dependientes':0, 'educacion':'No Graduado', 'independiente':'No',
                'ingreso_deudor':3748, 'ingreso_codeudor':1668, 'cantidad_prestamo':110, 'plazo_prestamo':360,
                'historia_credito':1, 'tipo_propiedad':'Semiurbano'}))