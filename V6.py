#teste pull request

# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import time
from pygame.locals import *
from pygame import mixer

pygame.init()

# ----- Gera tela
altura_da_tela = 500
largura_da_tela = 1000
window = pygame.display.set_mode((largura_da_tela, altura_da_tela))
pygame.display.set_caption('Jogo')

# ----- Musica
mixer.init()
mixer.music.load('Recursos/zap zap.ogg')

# ----- funções utilizadas no jogo
def cria_camadas(n_camada_final):
    camadas = []
    for i in range(1, n_camada_final*5, 5):
        camadas.append(-i*altura_inicial_dos_obstaculos)
    return camadas

def cria_obstaculos(n_buracos, camada):
    lista_obstaculos = []
    lista_indices = [0,1,2,3,4]
    for buraco in range(n_buracos):
        indice_sorteado = random.choice(lista_indices)
        lista_indices.remove(indice_sorteado)
    for indice in lista_indices:
        imagem_sorteada = random.choice(lista_das_imagens)
        posicao = lista_posições[indice]
        oobstaculo = Obstaculo(imagem_sorteada, posicao, camada)
        lista_obstaculos.append(oobstaculo)
    return lista_obstaculos

def cria_todos_obstaculos(camadas):
    lista = []
    numeros_de_buracos = [1,2,3,4]
    for i in camadas:
        lista.append(cria_obstaculos(random.choice(numeros_de_buracos), i))
    return lista

# ----- definição tamanhos e propriedades das estruturas
pontos = 0

largura_do_personagem = 180
altura_do_personagem = 120

largura_inicial_dos_obstaculos = 180
altura_inicial_dos_obstaculos = 120

velocidade_x_dos_obstaculos = 0
velocidade_y_dos_obstaculos = 2

acelerador = 0.1

tela_de_fundo_img = pygame.image.load('recursos/fundo.png').convert()
tela_de_fundo_img = pygame.transform.scale(tela_de_fundo_img,(largura_da_tela, altura_da_tela))

personagem_img = pygame.image.load('recursos/imagem_do_personagem.png').convert_alpha()
personagem_img = pygame.transform.scale(personagem_img,(largura_do_personagem, altura_do_personagem))

carro_da_fgv_img = pygame.image.load('recursos/imagem_do_carro_da_fgv.png').convert_alpha()
carro_da_fgv_img = pygame.transform.scale(carro_da_fgv_img, (largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

carro_do_marcao_img = pygame.image.load('recursos/imagem_do_carro_do_marcão.png').convert_alpha()
carro_do_marcao_img = pygame.transform.scale(carro_do_marcao_img,(largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

carro_da_espm_img = pygame.image.load('recursos/imagem_do_carro_da_espm.png').convert_alpha()
carro_da_espm_img = pygame.transform.scale(carro_da_espm_img,(largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

carro_da_puc_img = pygame.image.load('recursos/imagem_do_carro_da_puc.png').convert_alpha()
carro_da_puc_img = pygame.transform.scale(carro_da_puc_img, (largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

carro_do_mackenzie_img = pygame.image.load('recursos/imagem_do_carro_do_mackenzie.png').convert_alpha()
carro_do_mackenzie_img = pygame.transform.scale(carro_do_mackenzie_img, (largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

tela_de_fundo_menu_img = pygame.image.load('Recursos/capamenu2.jpeg').convert()
tela_de_fundo_menu_img = pygame.transform.scale(tela_de_fundo_menu_img,(largura_da_tela, altura_da_tela))

ganhou_img = pygame.image.load('Recursos/imagem_ganhou.jpeg').convert()
ganhou_img = pygame.transform.scale(ganhou_img,(largura_da_tela, altura_da_tela))

perdeu_img = pygame.image.load('Recursos/imagem_perdeu.jpeg').convert()
perdeu_img = pygame.transform.scale(perdeu_img,(largura_da_tela, altura_da_tela))

lista_das_imagens = [carro_da_fgv_img, carro_do_marcao_img, carro_da_espm_img, carro_da_puc_img, carro_do_mackenzie_img]

lista_indices = [0,1,2,3,4]
indice_esquerda = lista_indices[0]
indice_direita = lista_indices[-1]

vx = 20

# ----- Posições
lista_posições = [0, 200, 400, 600, 800] # referentes respectivamente a posição muito a esquerda, a esquerda, no meio, a direita e muito a direita

camadas = cria_camadas(60)

# ----- Inicia estruturas de dados
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, img, posicao, camada):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = posicao
        self.rect.y = camada
        self.speedx = velocidade_x_dos_obstaculos
        self.speedy = velocidade_y_dos_obstaculos

    def update (self):
        #atualizando posição do obstaculo
        self.rect.x += self.speedx
        acelaracao = int(self.speedy*((tempo_passado))*acelerador)
        self.rect.y += 2 + acelaracao

        #reiniciando posição
        if self.rect.top > altura_da_tela:
            todosobstaculos.remove(self)
            sprites.remove(self)

class Personagem(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.xlist = [0,200,400,600,800]
        self.indice = 2
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = self.xlist[self.indice]
        self.rect.y = altura_da_tela - altura_do_personagem
        self.speedx = 0
        self.speedy = 0

    def update (self):
        #self.rect.x = self.xlist[self.indice]
        self.rect.x +=self.speedx
        self.rect.y +=self.speedy

        if self.speedx != 0 and self.rect.x in self.xlist:
            self.speedx = 0

#escreve pontuação na tela
tamanho_da_font = 48
font = pygame.font.SysFont(None, tamanho_da_font)

#inicia
game = True

# ----- Ajuste de velocidade
tempo_inicial = time.time()

clock = pygame.time.Clock()
FPS = 60

# ----- Criando obstaculos
todosobstaculos = pygame.sprite.Group()
sprites = pygame.sprite.Group()

personagem = Personagem(personagem_img)
sprites.add(personagem)

lista_lista_obstaculos = cria_todos_obstaculos(camadas)

for lista in lista_lista_obstaculos:
    for obstaculo in lista:
        todosobstaculos.add(obstaculo)
        sprites.add(obstaculo)

estado = 'inicio'

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    tempo_final = time.time()
    tempo_passado = tempo_final - tempo_inicial
    pontos = tempo_final - tempo_inicial

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False


        if estado == 'inicio':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    estado = 'jogo'
                    tempo_inicial = time.time()
                    mixer.music.play()
                    FPS = FPS
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and personagem.speedx <= 2 and estado == 'jogo':
                if personagem.indice == indice_esquerda:
                    personagem.indice = indice_esquerda
                else:
                    personagem.indice -= 1
                    personagem.speedx = -vx
                

            if event.key == pygame.K_RIGHT and personagem.speedx == 0 and estado == 'jogo':
                if personagem.indice == indice_direita:
                    personagem.indice = indice_direita
                else:
                    personagem.indice += 1
                    personagem.speedx = vx
            
    if pontos >= 61:
        estado = 'ganhou'
    # ----- Atualiza estado do jogo
    sprites.update()

    # ----- Verifica Colisão
    hits = pygame.sprite.spritecollide(personagem, todosobstaculos, True)
    if len(hits) > 0:
        estado = 'perdeu'

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    if estado == 'inicio':
        window.blit(tela_de_fundo_menu_img , (0,0))

    elif estado == 'jogo':
        window.blit(tela_de_fundo_img,(0,0))
        text = font.render('{0:.0f}'.format(pontos), True, (0, 0, 0))
        window.blit(text, (490, 0))
        sprites.draw(window)

    elif estado == 'ganhou':
        window.blit(ganhou_img, (0,0))

    elif estado == 'perdeu':
        window.blit(perdeu_img, (0,0))
        mixer.music.stop()

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados