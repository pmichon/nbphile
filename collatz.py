#!/usr/bin/env python3
import argparse

def generate_collatz_sequence(n):
    """
    Generuje ciąg Collatza dla zadanej liczby n.
    
    Zasady:
    - Jeśli n jest parzyste: n/2
    - Jeśli n jest nieparzyste: 3n+1
    - Kontynuuj aż dojdziesz do 1
    
    Zwraca krotkę: (sekwencja, długość, maksymalna wartość)
    """
    if n <= 0:
        raise ValueError("Liczba musi być większa od 0")
    
    sequence = [n]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence, len(sequence), max(sequence)

def main():
    parser = argparse.ArgumentParser(
        description='Generuj ciąg Collatza (hipoteza 3n+1) dla zadanej liczby.'
    )
    parser.add_argument('n', type=int, help='Liczba początkowa (dodatnia liczba całkowita)')
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='Pokaż pełną sekwencję')
    args = parser.parse_args()

    if args.n <= 0:
        print("Błąd: Liczba musi być większa od 0")
        return

    sequence, length, max_value = generate_collatz_sequence(args.n)
    
    print(f"Ciąg Collatza dla liczby {args.n}:")
    print(f"  Długość sekwencji: {length}")
    print(f"  Maksymalna wartość: {max_value}")
    
    if args.verbose:
        print(f"  Pełna sekwencja:")
        # Wyświetl sekwencję w wierszach po 10 liczb
        for i in range(0, len(sequence), 10):
            chunk = sequence[i:i+10]
            print(f"    {' → '.join(map(str, chunk))}")
    else:
        # Pokaż tylko początek i koniec dla długich sekwencji
        if length <= 10:
            print(f"  Sekwencja: {' → '.join(map(str, sequence))}")
        else:
            start = ' → '.join(map(str, sequence[:5]))
            end = ' → '.join(map(str, sequence[-3:]))
            print(f"  Sekwencja: {start} → ... → {end}")
            print(f"  (użyj --verbose aby zobaczyć pełną sekwencję)")

if __name__ == "__main__":
    main()
