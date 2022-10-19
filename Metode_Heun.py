# Jerry Ardiansyah
# 202010225316

#Definisikan Fungsi f(x)
def f(x,y):
    return x+y

# Euler method 
def heun(x0,y0,xn,n):

    #Menghitung ukuran langkah xi 
    h = (xn-x0)/n

    print('-------------------------')
    print('x0\ty0\tfxy\tyn') 
    print('-------------------------')
    for i in range(n):
        k1 =h * f(x0,y0) 
        k2 = h * (f((x0+h), (y0+k1)))
        k = (k1+ k2)/2 
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f'% (x0,y0,yn) )
        print('-------------------------')
        y0 = yn
        x0 = x0+h

    print('\nJadi x=%.4f, y=%.4f' %(xn,yn))

# Input
print('\nMasukan Titik yang akan Dihitung: ')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('\nMasukan Titik yang akan Dihitung: ') 
xn = float(input('xn = '))

print('\nMasukan Jumlah Iterasi: ') 
step= int(input('Jumlah Iterasi = '))


# Memanggil Metode Heun
heun (x0,y0,xn,step)
