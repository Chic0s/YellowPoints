from PIL import Image

blue = Image.open("nomdufichier.png").split() [2]
blue.point(lambda x: (256-x)**2).show()