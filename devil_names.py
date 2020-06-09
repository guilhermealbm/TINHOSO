import random

devil_names = ['Anhangão', 'Aquele', 'Arrenegado', 'Austero', 'Azarape',
    'Barzabu', 'Beuzebu', 'Bode-Preto' 'Canho', 'Cão', 'Cão-Extremo', 
    'Cão-miúdo', 'Cão-Tinhoso', 'Capeta', 'Capiroto', 'Caracães', 'Careca', 
    'Carmulhão', 'Carocho', 'Carujo', 'Coisa-Má', 'Coisa-Ruim', 'Coxo', 'Crespo', 'Cujo', 
    'Dado', 'Danador', 'Das-Trevas', 'Dê', 'Debo', 'Demo', 'Demonião', 'Demônio', 'Diá', 
    'Diabo', 'Diabinho', 'Diacho', 'Dianho', 'Dião', 'Diogo', 'Dioguim', 'Dos-Fins',
    'Drão', 'Duba-Dubá', 'Ele', 'Figura', 'Galhardo', 'Grão-Tinhoso', 'Homem', 'Hermógenes',
    'Individuo', 'Lúcifer', 'Mafarro', 'Mal-Encarado', 'Maligno', 'Manfarro', 'Morcegão', 
    'Não-Sei-Que-Diga', 'Oculto', 'O-Muito-Sério', 'O-Que-Não-Existe', 'O-Que-Não-Ri', 
    'O-Que-Nunca-Fala', 'O-Que-Nunca-Se-Ri', 'Outro', 'Pai-do-Mal', 'Pai-da-Mentira',
    'Pé-de-Pato', 'Pé-Preto', 'Que-Diga', 'Que-Não-Há', 'Quem-Não-Existe', 'Rapaz',
    'Romãozinho', 'Roncôlho', 'Satanão', 'Sem-Gracejo', 'Sem-Olho', 'Sempre-Sério', 'Satanás',
    'Sôuto-Eu', 'Severo-Mor', 'Sujo', 'Tal', 'Temba', 'Tendeiro', 'Tentador', 'Tibes',
    'Tinhoso', 'Tisnado', 'Tralha', 'Tranjão', 'Tristoho', 'Tunes', 'Xu']

def get_random_devil_name():
    return random.choice(devil_names)
    

def get_devil_name(index):
    if (index < 0 or index >= len(devil_names)):
        return('Demônio out of bounds')
    else:
        return(devil_names[index])

def get_all_devil_names():
    return devil_names

if __name__ == '__main__':
    print(get_random_devil_name())