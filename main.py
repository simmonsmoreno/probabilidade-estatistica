import math
import pandas as pd
import numpy as np

def tabela_de_frequencias(dados, tipo):
    dados.sort()
    n = len(dados)
    amplitude_amostra = max(dados) - min(dados)

    if tipo == 'continuo':
        k = int(1 + 3.32 * math.log10(n))
        amplitude_classe = amplitude_amostra / k
        classes = []
        inicio = min(dados)
        for i in range(k):
            fim = inicio + amplitude_classe
            classes.append((inicio, fim))
            inicio = fim
    else:
        classes = list(set(dados))

    tabela = pd.DataFrame(columns=['xi', 'fi', 'Fi', 'fr', 'Fr'])
    fi_acumulado = 0
    for classe in classes:
        if tipo == 'continuo':
            fi = len([x for x in dados if classe[0] <= x < classe[1]])
        else:
            fi = dados.count(classe)
        fi_acumulado += fi
        fr = fi / n
        Fr = fi_acumulado / n
        tabela = tabela.append({'xi': classe, 'fi': fi, 'Fi': fi_acumulado, 'fr': fr, 'Fr': Fr}, ignore_index=True)

    return tabela

# Exemplo de dados
dados = [1, 2, 3, 4, 2, 3, 4, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7]

# Chamando a função para criar a tabela de frequências
print(tabela_de_frequencias(dados, 'discreto'))
print(tabela_de_frequencias(dados, 'continuo'))