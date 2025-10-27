import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

# Funkcja rysująca wykres na podstawie eval()
def rysuj_wielomian(wejscie):
    # Generowanie wartości x i y przy użyciu eval()
    # Rysowanie wykresu ale bez show()
    func = wejscie.split(',')[0].strip()
    zakres = wejscie.split(',')[1].strip().split()
    start, end = float(zakres[0]), float(zakres[1])
    x_val = np.linspace(start, end, 400)
    y_val = [eval(func) for x in x_val]

    plt.plot(x_val, y_val, color = 'blueviolet')

    # Zwracanie wartości na granicach przedziału
    return y_val[0], y_val[-1]

# Funkcja rysująca wykres na podstawie SymPy i lambdify()
def rysuj_wielomian_sympy(wejscie):
    # Definicja symbolu i konwersja do funkcji numerycznej za pomocą SymPy
    # Generowanie wartości x i y przy użyciu funkcji numerycznej
    # Rysowanie wykresu ale bez show()

    x = symbols('x')
    func = wejscie.split(',')[0].strip()
    zakres = wejscie.split(',')[1].strip().split()
    start, end = float(zakres[0]), float(zakres[1])
    expr = sympify(func)
    func_num = lambdify(x, expr, modules=['numpy'])

    x_val_sympy = np.linspace(start, end, 400)
    y_val_sympy = func_num(x_val_sympy)

    plt.plot(x_val_sympy, y_val_sympy, color='red')

    # Zwracanie wartości na granicach przedziału
    return y_val_sympy[0], y_val_sympy[-1]

if __name__ == '__main__':
    # Przykładowe wywołanie pierwszej funkcji
    wejscie1 = "x**3 + 3*x + 1, -10 10"
    
    # Pierwszy wykres z eval5
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)
    
    # Drugie wejście dla funkcji SymPy - bardziej złożona funkcja 
    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"  
    
    # Drugi wykres z SymPy
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)
    
    # Wyświetlanie obu wykresów
    plt.show()
