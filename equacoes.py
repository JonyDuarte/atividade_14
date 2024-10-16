from math import sqrt
# Esquação do primeiro grau

def calcular_x(a, b):
     x = -b / a
     return x

primeiro_grau = lambda a, b: -b/a

# Equação do segundo grau
def segundo_grau(a, b, c):
     D = (b**2 - 4*a*c)
     if D > 0:
          x1 = ((-b)+ sqrt(D))/(2*a)
          x2 = ((-b)- sqrt(D))/(2*a)
          yield f"Valor de x': {x1}."
          yield f'Valor de x": {x2}.'
     elif D == 0:
        x = -b/(2*a)
        yield f"Valor real de x: {x}."
     else:
          yield f"Não existem raízes reais para essa equação."

        
          
    
