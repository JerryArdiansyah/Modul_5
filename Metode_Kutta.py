# Jerry Ardiansyah
# 202010225316

#Metode Runge-Kutta Orde 4

# Definisikan fungsi f(x)
def f(x,y):
    return x+y

# RK orde 4
def RK4(x0,y0,xn,n):

    # Menghitung ukuran langkah xi 
    h = (xn-x0)/n

    print('---------------------------')
    print('x0\ty\tfxy\tyn')
    print('---------------------------')
    for i in range(n): 
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h/2), (y0+k1/2))) 
        k3 = h * (f((x0+h/2), (y0+k2/2)))
        k4 = h * (f((x0+h), (y0+k3))) 
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f'% (x0,y0,yn) )
        print('---------------------------')
        y0 = yn
        x0 = x0+h

    print('\nJadi x=%.4f, y=%.4f' %(xn,yn))

# Input
print('\nMasukan Kondisi Awal: ')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('\nMasukan Titik yang akan Dihitung: ') 
xn = float(input('xn = '))

print('\nMasukan Jumlah Iterasi: ') 
step = int(input('Jumlah Iterasi = '))

#Memanggil Metode Heun 
RK4(x0, y0, xn, step)