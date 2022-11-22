from PIL import Image

# CARREGAR A IMAGEM
imagem = Image.open(r"C:\Users\KAL-EL\Downloads\Imagens\Clark_Kent.jpeg")

# CONVERTER PARA PRETO E BRANCO
imagem = imagem.convert("L")

# SALVANDO A IMAGEM
imagem.save(r"C:\Users\KAL-EL\Downloads\Imagens\Clark_Kent_PB.jpeg")
