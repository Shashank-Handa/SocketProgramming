from PIL import Image

def compress(filepath):
    img=Image.open(filepath)
    size=img.size
    img=img.resize((int(size[0]*0.8),int(size[1]*0.8)),Image.ANTIALIAS)
    img.save("2"+filepath,optimize=True,quality=80)

    return "2"+filepath