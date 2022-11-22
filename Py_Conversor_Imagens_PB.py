from PIL import Image

# CARREGAR A IMAGEM
imagem = Image.open(r"imagem_colorida.jpg")

# CONVERTER PARA PRETO E BRANCO
imagem = imagem.convert("L")

# SALVANDO A IMAGEM
imagem.save(r"imagem_preto_branco.jpg")
