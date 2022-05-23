# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
altura_da_tela = 500
largura_da_tela = 600
window = pygame.display.set_mode((largura_da_tela, altura_da_tela))
pygame.display.set_caption('Jogo')


# ----- definição tamanhos das estruturas
altura_inicial_do_carro_da_fgv = 50
largura_inicial_do_carro_da_fgv = 70

carro_da_fgv_img = pygame.image.load('recursos/imagem_do_carro_da_fgv.png').convert_alpha()
carro_da_fgv_img_small = pygame.transform.scale(carro_da_fgv_img, (largura_inicial_do_carro_da_fgv, altura_inicial_do_carro_da_fgv))



# ----- Inicia estruturas de dados
game = True

# ----- Posição do obstáculo

posição_x_carro_da_fgv = 200
posição_y_carro_da_fgv = -altura_inicial_do_carro_da_fgv

velocidade_x_do_carro_da_fgv = -0.015
velocidade_y_do_carro_da_fgv = 0.05

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    posição_x_carro_da_fgv += velocidade_x_do_carro_da_fgv
    posição_y_carro_da_fgv += velocidade_y_do_carro_da_fgv
    # Se o obstaculo passar do final da tela, volta para cima
    if posição_y_carro_da_fgv > altura_da_tela or posição_x_carro_da_fgv + largura_inicial_do_carro_da_fgv < 0 or posição_x_carro_da_fgv > largura_da_tela:
        posição_x_carro_da_fgv = 200
        posição_y_carro_da_fgv = -altura_inicial_do_carro_da_fgv

    # ----- Gera saídas
    window.fill((255, 255, 0))  # Preenche com a cor branca
    window.blit(carro_da_fgv_img_small, (posição_x_carro_da_fgv, posição_y_carro_da_fgv))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados