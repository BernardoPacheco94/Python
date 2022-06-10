class FormaGeometrica:
    cor_fundo = None
    cor_borda = None
    espessura_borda = None
    
class Triangulo(FormaGeometrica):
    base = None
    altura = None
    
    def calcular_area(self):
        return (self.base*self.altura) / 2
    
class Quadrilatero(FormaGeometrica):
    base = None
    altura = None
    
    def calcular_area(self):
        return self.base*self.altura

triangulo_a = Triangulo()
triangulo_a.cor_fundo = 'vermelho'
triangulo_a.cor_borda = 'preto'
triangulo_a.espessura_borda = 3
triangulo_a.base = 100
triangulo_a.altura = 150

print('Cor de fundo:',triangulo_a.cor_fundo)
print('Area triangulo:',round(triangulo_a.calcular_area()))


quadrado = Quadrilatero()
quadrado.cor_fundo = 'transparente'
quadrado.cor_borda = 'preto'
quadrado.espessura_borda = 2
quadrado.base = 8
quadrado.altura = 16
print('Area quadrado:', quadrado.calcular_area())
