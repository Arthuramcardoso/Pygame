# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import time
from pygame.locals import *
from pygame import mixer

pygame.init()

# ----- Gera tela principal
altura_da_tela = 500
largura_da_tela = 1000
window = pygame.display.set_mode((largura_da_tela, altura_da_tela))
pygame.display.set_caption('Jogo')


# ----- Musica
mixer.init()
mixer.music.load('Recursos/zap zap.ogg')
mixer.music.play()

# ----- funções utilizadas no jogo

camadas = []
def cria_camadas(n_camada_final):
    for i in range(1, n_camada_final*5, 5):
        camadas.append(-i*altura_inicial_dos_obstaculos)
    return camadas


# ----- definição tamanhos e propriedades das estruturas

largura_do_personagem = 180
altura_do_personagem = 120

altura_inicial_dos_obstaculos = 120
largura_inicial_dos_obstaculos = 180

velocidade_x_dos_obstaculos = 0
velocidade_y_dos_obstaculos = 2

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

lista_das_imagens = [carro_da_fgv_img, carro_do_marcao_img, carro_da_espm_img, carro_da_puc_img, carro_do_mackenzie_img]

# ----- Posições e velocidades iniciais
muito_esquerda = [0, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]
esquerda = [200, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]
meio = [400, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]
direita = [600, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]
muito_direita = [800, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]

cria_camadas(20)

# ----- Inicia estruturas de dados
# definindo os novos tipos de estruturas
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, img, posição,camada):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.posição = posição
        self.rect.x = posição[0]
        self.rect.y = camada
        self.speedx = posição[2]
        self.speedy = posição[3]

    def update (self):
        #atualizando posição do obstaculo
        self.rect.x += self.speedx
        self.rect.y += self.speedy*((tempo_final-tempo_inicial))

        #atualizando o tamanho
        #self.image = pygame.transform.scale(self.image, (abs(180+self.rect.y*0.375), abs(120+self.rect.y*0.25)))

        #reiniciando posição
        if self.rect.top > altura_da_tela:
            #self.image = pygame.transform.scale(self.image,(largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))
            self.rect.x = self.posição[0]
            self.rect.y = self.posição[1]

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

carro_da_fgv = Obstaculo(carro_da_fgv_img, muito_esquerda, camadas[0])
carro_do_marcao = Obstaculo(carro_do_marcao_img, esquerda, camadas[1])
carro_da_espm = Obstaculo(carro_da_espm_img, meio, camadas[2])
carro_da_puc = Obstaculo(carro_da_puc_img, direita, camadas[3])
carro_do_mackenzie = Obstaculo(carro_do_mackenzie_img, muito_direita, camadas[4])

listaobstaculos = [carro_da_fgv,carro_do_marcao,carro_da_espm,carro_da_puc,carro_do_mackenzie]

for obstaculo in listaobstaculos:
    todosobstaculos.add(obstaculo)
    sprites.add(obstaculo)


# ===== Loop principal =====
while game:
    clock.tick(FPS)
    tempo_final = time.time()

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if personagem.indice == 0:
                    personagem.indice = 0
                else:
                    personagem.indice -= 1
                    personagem.speedx = -20
                

            if event.key == pygame.K_RIGHT:
                if personagem.indice == 4:
                    personagem.indice = 4
                else:
                    personagem.indice += 1
                    personagem.speedx = 20
            
  
    # ----- Atualiza estado do jogo

    # carro_da_fgv.update()
    # carro_do_marcao.update()
    # carro_da_espm.update()
    # carro_da_puc.update()
    # carro_do_mackenzie.update()

    # personagem.update()
    sprites.update()

    # ----- Verifica Colisão
    hits = pygame.sprite.spritecollide(personagem, todosobstaculos, True)
    if len(hits) > 0:
        game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(tela_de_fundo_img,(0,0))

    # window.blit(carro_da_fgv.image, carro_da_fgv.rect)
    # window.blit(carro_da_espm.image, carro_da_espm.rect)
    # window.blit(carro_do_marcao.image, carro_do_marcao.rect)
    # window.blit(carro_da_puc.image, carro_da_puc.rect)
    # window.blit(carro_do_mackenzie.image, carro_do_mackenzie.rect)
    # window.blit(personagem.image, personagem.rect)
    sprites.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados