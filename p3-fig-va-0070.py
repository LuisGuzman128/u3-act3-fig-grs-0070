import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Axel Guzman NC 0070
print("Axel Guzman NC 0070")
print("UIII Act 3 coloca puntos a un imagen en blanco y negro")
mi_imagen = cv2.imread('leon.png')
plt.imshow(mi_imagen)
plt.title('leon.png y Axel Guzman 0070')
plt.show()
print("+-+-+- puntos en la imagen +-+-+-")
plt.imshow(mi_imagen)
x = [100,100,300,340]
y = [100,400,500,300]
plt.scatter(x, y, s=20,c='red')
plt.show()