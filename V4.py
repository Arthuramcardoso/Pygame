# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
altura_da_tela = 500
largura_da_tela = 1000
window = pygame.display.set_mode((largura_da_tela, altura_da_tela))
pygame.display.set_caption('Jogo')


# ----- definição tamanhos e propriedades das estruturas

altura_inicial_dos_obstaculos = 120
largura_inicial_dos_obstaculos = 180

velocidade_x_dos_obstaculos = 0
velocidade_y_dos_obstaculos = 8

tela_de_fundo_img = pygame.image.load('recursos/fundo.png').convert()
tela_de_fundo_img = pygame.transform.scale(tela_de_fundo_img,(largura_da_tela, altura_da_tela))

carro_da_fgv_img = pygame.image.load('recursos/imagem_do_carro_da_fgv.png').convert_alpha()
carro_da_fgv_img = pygame.transform.scale(carro_da_fgv_img, (largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

carro_do_marcao_img = pygame.image.load('recursos/imagem_do_carro_do_marcão.png').convert_alpha()
carro_do_marcao_img = pygame.transform.scale(carro_do_marcao_img,(largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

carro_da_espm_img = pygame.image.load('recursos/imagem_do_carro_da_espm.png').convert_alpha()
carro_da_espm_img = pygame.transform.scale(carro_da_espm_img,(largura_inicial_dos_obstaculos, altura_inicial_dos_obstaculos))

# ----- Posições e velocidades iniciais
muito_esquerda = [0, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]
esquerda = [200, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]
meio = [400, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]
direita = [600, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]
muito_direita = [800, -altura_inicial_dos_obstaculos, velocidade_x_dos_obstaculos, velocidade_y_dos_obstaculos]



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

carro_da_fgv = Obstaculo(carro_da_fgv_img, muito_esquerda)
carro_do_marcao = Obstaculo(carro_do_marcao_img, meio)
carro_da_espm = Obstaculo(carro_da_espm_img, muito_direita)

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
    carro_do_marcao.update()
    carro_da_espm.update()


    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(tela_de_fundo_img,(0,0))

    window.blit(carro_da_fgv.image, carro_da_fgv.rect)
    window.blit(carro_da_espm.image, carro_da_espm.rect)
    window.blit(carro_do_marcao.image, carro_do_marcao.rect)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados