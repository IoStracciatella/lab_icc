import imageio.v3 as iio
import numpy as np

def luminance(img):
    if len(img.shape) == 3:
        R = img[:, :, 0]
        G = img[:, :, 1]
        B = img[:, :, 2]
        L = 0.2126 * R + 0.7152 * G + 0.0722 * B
        L = L.astype(np.uint8)
        return L
    else:
        return img

def downsampling(img, P):
    nova = img[::P, ::P]
    return nova

def quantization(img, B):
    shift = 8 - B
    img = img >> shift
    img = img << shift
    return img.astype(np.uint8)

def mirror(img, E):
    if E == "H":
        return img[:, ::-1]
    elif E == "V":
        return img[::-1, :]
    else:
        return img

def gamma(img, F):
    img = img / 255
    img = 255 * (img ** (1 / F))
    img = np.clip(img, 0, 255)
    return img.astype(np.uint8)

nome = input().strip()
N = int(input().strip())
img = iio.imread(nome)
img = luminance(img)

for i in range(N):
    partes = input().split()
    op = partes[0]

    if op == "LUMINANCE":
        img = luminance(img)
    elif op == "DOWNSAMPLING":
        P = int(partes[1])
        img = downsampling(img, P)
    elif op == "QUANTIZATION":
        B = int(partes[1])
        img = quantization(img, B)
    elif op == "MIRROR":
        E = partes[1]
        img = mirror(img, E)
    elif op == "GAMMA":
        F = float(partes[1])
        img = gamma(img, F)

media = np.mean(img)
desvio = np.std(img)
minimo = np.min(img)
maximo = np.max(img)
tons = len(np.unique(img))
h, w = img.shape

print(f"Intensidade média: {media:.2f} | Desvio: {desvio:.2f}")
print(f"Intensidade mínima: {minimo} | Intensidade máxima: {maximo}")
print(f"Tons únicos: {tons}")
print(f"Dimensão: {h} x {w}")
