
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
# Axel Guzman NC 0070
print("Axel Guzman NC 0070")
print("UIII Act 3 coloca puntos a una imagen en blanco y negro")
mi_imagen = cv2.imread('leon.png', cv2.IMREAD_GRAYSCALE)
plt.imshow(mi_imagen, cmap='gray')
plt.title('leon.png y Axel Guzman 0070')
plt.show()
print("+-+-+- puntos en la imagen +-+-+-")
plt.imshow(mi_imagen, cmap='gray')
x = [100, 100, 300, 340]
y = [100, 400, 500, 300]
plt.scatter(x, y, s=20, c='red')
plt.show()
print("+-+-+- cuadro en la imagen +-+-+-")
img_leon = cv2.imread('leon.png', cv2.IMREAD_GRAYSCALE)
plt.imshow(img_leon, cmap='gray')
# Nuevas coordenadas del cuadro
x = [150, 150, 450, 450, 150]
y = [400, 100, 100, 400, 400]
plt.plot(x, y, c='blue')
plt.show()
print("+-+-+- circulo verde en la imagen +-+-+-")
I = cv2.imread('leon.png', cv2.IMREAD_GRAYSCALE)
plt.imshow(I, cmap='gray')
N = 30 # lados del poligono
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc, yc) = (340, 320)
r = 150 # radio
for i in range(N+1):
    t = 2*np.pi/N*i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)
plt.plot(x, y, c='green')
plt.show()
