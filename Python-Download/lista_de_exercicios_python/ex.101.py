def voto(i):
    from datetime import date
    idd = date.today().year - i
    if idd < 16:
        return f'Com {idd} anos: NÃO VOTA!'
    elif idd >= 16 and idd < 18 or idd >= 70:
        return f'Com {idd} anos: VOTO OPCIONAL!'
    elif idd >= 18 or idd < 70:
        return f'Com {idd} anos: VOTO OBRIGATÓRIO!'


idade = int(input('Ano de nascimento: '))
print(voto(idade))
