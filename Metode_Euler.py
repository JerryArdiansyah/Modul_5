# Jerry Ardiansyah
# 202010225316

# Definisikan fungsi f(x) 
def f(x,y):
    return x+y

# Euler method
def euler(x0,y0,xn,n):

    #Menghitung ukuran langkah xi 
    h = (xn-x0)/n

    print('-------------------------------')
    print('x0\ty0\tfxy\tyn')
    print('-------------------------------')
    for i in range(n):
        fxy = f(x0, y0)
        yn = y0 + h * fxy
        print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0, y0, fxy, yn) ) 
        print('-------------------------------')
        y0 = yn
        x0 = x0+h

    print('\nJadi x=%. 4f, y=%.4f' %(xn, yn))

# Inputs
print('\nMasukan Kondisi Awal: ')
x0 = float(input('x0 = ')) 
y0 = float(input('y0 = '))

print('\nMasukan Titik yang akan Dihitung: ') 
xn = float(input('xn = '))

print('\nMasukan Jumlah Iterasi:') 
step = int(input('Jumlah Iterasi = '))

# Euler method call
euler (x0,y0,xn,step)