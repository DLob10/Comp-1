# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# int -> int
def absoluto(num):
    """Retorna o modulo do numero"""
    if num > 0:
        return num
    else:
        return -num



# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# int, int, int -> int
import math

def delta(a, b, c):
    return (b**2) - 4*a*c

def calcular_raiz(a, b, c):
    """Dados os valores dos coeficientes retorna as raizes ou valor nulo."""
    if delta(a, b, c) > 0 :
        return "2"
    else :
        if delta(a, b, c)< 0 :
            return "0"
        else :
            return "1"




# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# float -> float
def calcular_f(x):
    if x < 0 :
        return None
    else :
        if x >= 0 and x <= 2 :
            return x
        else :
            if x > 2 and x <= 3.5 :
                return 2
            else :
                if x > 3.5 and x <= 5 :
                    return 3
                else :
                    if x > 5 and x <= 6 :
                        return (x**2) - (10 * x) + 28


# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# int , bool -> bool
def meia_entrada(idade, estudante):
    if idade <=21 or idade >=65 :
        return True
    else:
        if idade >21 and idade <65 and estudante == True:
            return True
        else :
            return False
