def nota(* n, sit=False):
    """
    :param n: Adicionar as notas dos alunos
    :param sit: Se for True vai mostrar a situação da turma
    :return: Dicionario com varias informações da turma
    """

    dicio = dict()
    mai = men = med = 0

    dicio['total'] = len(n)

    for v, c in enumerate(n):
        if v == 0:
            mai = c
            men = c
        else:
            if c > mai:
                mai = c
            if c < men:
                men = c
    dicio['Maior'] = mai
    dicio['Menor'] = men

    for m in n:
        med += m
    dicio['Media'] = med / len(n)

    if sit:
        if dicio['Media'] >= 7:
            dicio['Situacao'] = 'Boa'
        elif dicio['Media'] > 5:
            dicio['Situacao'] = 'Razoavel'
        else:
            dicio['Situacao'] = 'Ruim'

    return dicio


print(nota(10, 5.5, 2.1, sit=True))
