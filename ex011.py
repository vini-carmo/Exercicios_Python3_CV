largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
print('Sua parede tem a dimensão de {:.1f}m de largura X {:.1f}m de altura e sua área é de {:.1f}m²!'.format(largura, altura, area))
print('Para pintar essa parede, você precisa de {:.1f}L de tinta!'.format(area / 2))
