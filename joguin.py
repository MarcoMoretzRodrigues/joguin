import pygame
import random
import sys

# Inicializa o Pygame e imprime uma mensagem de depuração
pygame.init()
print("Pygame foi iniciado com sucesso!")

# Definições da tela
LARGURA_TELA = 800
ALTURA_TELA = 400
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo Odonto")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Relógio para controlar a taxa de quadros (FPS)
clock = pygame.time.Clock()
FPS = 30

# Variáveis do personagem
largura_personagem = 50
altura_personagem = 50
x_personagem = 50
y_personagem = ALTURA_TELA - altura_personagem - 10
velocidade_personagem = 5

# Tenta carregar a imagem do personagem e exibe mensagem de erro, se falhar
try:
    imagem_personalizada = pygame.image.load("img/homem.png")  # Substitua com o caminho correto
    print("Imagem do personagem carregada com sucesso!")
except pygame.error as e:
    print(f"Erro ao carregar a imagem do personagem: {e}")
    sys.exit()

# Variáveis do obstáculo (cáries)
largura_obstaculo = 40
altura_obstaculo = 40
x_obstaculo = LARGURA_TELA
y_obstaculo = ALTURA_TELA - altura_obstaculo - 10
velocidade_obstaculo = 7

# Tenta carregar a imagem do obstáculo e exibe mensagem de erro, se falhar
try:
    imagem_carie = pygame.image.load("img/desenho-animado.png")  # Substitua com o caminho correto
    print("Imagem da cárie carregada com sucesso!")
except pygame.error as e:
    print(f"Erro ao carregar a imagem da cárie: {e}")
    sys.exit()

# Fonte
fonte = pygame.font.SysFont(None, 55)

# Função para desenhar o personagem
def personagem(x, y):
    tela.blit(imagem_personalizada, (x, y))

# Função para desenhar o obstáculo (cárie)
def obstaculo(x, y):
    tela.blit(imagem_carie, (x, y))

# Função para exibir o nome do jogador
def mostrar_nome(nome):
    texto = fonte.render(f"Nome: {nome}", True, PRETO)
    tela.blit(texto, [10, 10])

# Loop principal do jogo
nome = "AAA"  # Nome fixo por enquanto
rodando = True

print("Entrando no loop principal do jogo.")
while rodando:
    try:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Controle de teclas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            x_personagem -= velocidade_personagem
        if teclas[pygame.K_RIGHT]:
            x_personagem += velocidade_personagem
        if teclas[pygame.K_UP]:
            y_personagem -= velocidade_personagem
        if teclas[pygame.K_DOWN]:
            y_personagem += velocidade_personagem

        # Movimenta o obstáculo
        x_obstaculo -= velocidade_obstaculo
        if x_obstaculo < -largura_obstaculo:
            x_obstaculo = LARGURA_TELA
            y_obstaculo = ALTURA_TELA - altura_obstaculo - 10

        # Atualiza a tela
        tela.fill(BRANCO)
        personagem(x_personagem, y_personagem)
        obstaculo(x_obstaculo, y_obstaculo)
        mostrar_nome(nome)

        # Atualiza a janela
        pygame.display.update()

        # Define a taxa de quadros
        clock.tick(FPS)

    except Exception as e:
        print(f"Ocorreu um erro no loop principal: {e}")
        rodando = False

# Encerra o Pygame
pygame.quit()

# Adiciona um input para impedir que o terminal feche imediatamente
input("Pressione Enter para sair...")
