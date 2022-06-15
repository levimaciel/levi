import pygame

def tamanho_imagem(img, fator):
    tamanho = round(img.get_width() * fator), round(img.get_height() * fator)
    return pygame.transform.scale(img, tamanho)

def centro_rotação(janela, imagem, top_left, angulo):
    rotated_image = pygame.transform.rotate(imagem, angulo)
    new_rect = rotated_image.get_rect(center=imagem.get_rect(topleft = top_left).center)
    janela.blit(rotated_image, new_rect.topleft)

def texto_centro(janela, fonte, texto):
    render = fonte.render(texto, 1, (200, 200, 200))
    janela.blit(render, (janela.get_width()/2 - render.get_width() /
                      2, janela.get_height()/2 - render.get_height()/2))