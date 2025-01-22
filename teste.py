def intervalos_personalizados():
    intervalos = ['Sem duração']
    total_minutos = 23 * 60 + 30  # Total de minutos até 23h30
    minutos = 15

    while minutos <= total_minutos:
        horas = minutos // 60
        minutos_restantes = minutos % 60

        if horas > 0 and minutos_restantes > 0:
            intervalos.append(f"{horas}h{minutos_restantes}m")
        elif horas > 0:
            intervalos.append(f"{horas}h")
        else:
            intervalos.append(f"{minutos_restantes}m")
        
        # Após a primeira hora, os intervalos passam a ser de 30 minutos
        if minutos < 60:
            minutos += 15
        else:
            minutos += 30

    return intervalos

# Testando a função
print(intervalos_personalizados())

