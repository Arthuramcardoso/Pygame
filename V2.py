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
altura_inicial_do_obstaculo = 50
largura_inicial_do_obstaculo = 50

obstaculo_img = pygame.image.load('recursos/imagem_do_meteoro.png')
obstaculo_img_small = pygame.transform.scale(obstaculo_img, (largura_inicial_do_obstaculo, altura_inicial_do_obstaculo))



# ----- Inicia estruturas de dados
game = True

# ----- Posição do obstáculo

posição_x_obstaculo = 200
posição_y_obstaculo = -altura_inicial_do_obstaculo

velocidade_x_do_obstaculo = -0.015
velocidade_y_do_obstaculo = 0.05

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    posição_x_obstaculo += velocidade_x_do_obstaculo
    posição_y_obstaculo += velocidade_y_do_obstaculo
    # Se o obstaculo passar do final da tela, volta para cima
    if posição_y_obstaculo > altura_da_tela or posição_x_obstaculo + largura_inicial_do_obstaculo < 0 or posição_x_obstaculo > largura_da_tela:
        posição_x_obstaculo = 200
        posição_y_obstaculo = -altura_inicial_do_obstaculo

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(obstaculo_img_small, (posição_x_obstaculo, posição_y_obstaculo))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados