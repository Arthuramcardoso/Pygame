# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
altura_da_tela = 720
largura_da_tela = 1270
window = pygame.display.set_mode((largura_da_tela, altura_da_tela))
pygame.display.set_caption('Jogo')


# ----- definição tamanhos das estruturas

altura_inicial_dos_obstaculos = 160
largura_inicial_dos_obstaculos = 240

carro_da_fgv_img = pygame.image.load('recursos/imagem_do_carro_da_fgv.png').convert_alpha()
carro_da_fgv_img = pygame.transform.scale(carro_da_fgv_img, (largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

carro_do_marcão_img = pygame.image.load('recursos/imagem_do_carro_do_marcão.png').convert_alpha()
carro_do_marcão_img = pygame.transform.scale(carro_do_marcão_img,(largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

# ----- Posições e velocidades iniciais
esquerda = [175, -altura_inicial_dos_obstaculos, 0, 8]


# ----- Inicia estruturas de dados
# definindo os novos tipos de estruturas
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, img, posição):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.posição = posição
        self.rect.x = posição[0]
        self.rect.y = posição[1]
        self.speedx = posição[2]
        self.speedy = posição[3]

    def update (self):
        #atualizando posição do obstaculo
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #atualizando o tamanho
        #self.image = pygame.transform.scale(self.image, (abs(180+self.rect.y*0.375), abs(120+self.rect.y*0.25)))

        #reiniciando posição
        if self.rect.top > altura_da_tela:
            #self.image = pygame.transform.scale(self.image,(largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))
            self.rect.x = self.posição[0]
            self.rect.y = self.posição[1]

game = True


# ----- Ajuste de velocidade

clock = pygame.time.Clock()
FPS = 20

# ----- Criando obstaculos

carro_da_fgv = Obstaculo(carro_da_fgv_img,esquerda)

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo

    carro_da_fgv.update()

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca

    window.blit(carro_da_fgv.image, (carro_da_fgv.rect.x, carro_da_fgv.rect.y))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados