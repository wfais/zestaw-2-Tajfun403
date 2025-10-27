import os
import time
import threading
import sys

# Stałe konfiguracyjne
LICZBA_KROKOW = 80_000_000
LICZBA_WATKOW = sorted({1, 2, 4, os.cpu_count() or 4})


def policz_fragment_pi(pocz: int, kon: int, krok: float, wyniki: list[float], indeks: int) -> None:
    # Funkcja oblicza częściową sumę przybliżenia liczby pi metodą prostokątów.
    # Argumenty:
    #     pocz, kon - zakres iteracji (indeksy kroków całkowania),
    #     krok      - szerokość pojedynczego prostokąta (1.0 / LICZBA_KROKOW),
    #     wyniki    - lista, do której należy wpisać wynik dla danego wątku na pozycji indeks,
    #     indeks    - numer pozycji w liście 'wyniki' do zapisania rezultatu.

    # Każdy wątek powinien:
    #   - obliczyć lokalną sumę dla przydzielonego przedziału,
    #   - wpisać wynik do wyniki[indeks].

    sum = 0.0
    for i in range(pocz, kon):
        x = (i + 0.5) * krok
        sum += 4.0 / (1.0 + x * x)

    wyniki[indeks] = sum


def main():
    print(f"Python: {sys.version.split()[0]}  (tryb bez GIL? {getattr(sys, '_is_gil_enabled', lambda: None)() is False})")
    print(f"Liczba rdzeni logicznych CPU: {os.cpu_count()}")
    print(f"LICZBA_KROKOW: {LICZBA_KROKOW:,}\n")

    # Wstępne uruchomienie w celu stabilizacji środowiska wykonawczego
    krok = 1.0 / LICZBA_KROKOW
    wyniki = [0.0]
    w = threading.Thread(target=policz_fragment_pi, args=(0, LICZBA_KROKOW, krok, wyniki, 0))
    w.start()
    w.join()

    # ---------------------------------------------------------------
    # Tu zaimplementować:
    #   - utworzenie wielu wątków (zgodnie z LICZBY_WATKOW),
    #   - podział pracy na zakresy [pocz, kon) dla każdego wątku,
    #   - uruchomienie i dołączenie wątków (start/join),
    #   - obliczenie przybliżenia π jako sumy wyników z poszczególnych wątków,
    #   - pomiar czasu i wypisanie przyspieszenia.
    # ---------------------------------------------------------------

    for threads in LICZBA_WATKOW:
        wyniki = [0.0] * threads
        thread_list = []
        krok = 1.0 / LICZBA_KROKOW
        start_time = time.time()

        for i in range(threads):
            start = i * (LICZBA_KROKOW // threads)
            end = (i + 1) * (LICZBA_KROKOW // threads) if i != threads - 1 else LICZBA_KROKOW
            w = threading.Thread(target=policz_fragment_pi, args=(start, end, krok, wyniki, i))
            thread_list.append(w)
            w.start()

        for w in thread_list:
            w.join()

        pi_approx = sum(wyniki) * krok
        elapsed_time = time.time() - start_time
        print(f"Wątki: {threads:2d}, π ≈ {pi_approx:.15f}, czas: {elapsed_time:.4f} s")


if __name__ == "__main__":
    main()
