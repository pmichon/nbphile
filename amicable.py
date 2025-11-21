#!/usr/bin/env python3
import argparse

def sum_proper_divisors(n):
    """
    Oblicza sumę dzielników właściwych liczby n.
    Dzielniki właściwe to dzielniki mniejsze od samej liczby.
    """
    if n <= 1:
        return 0
    
    total = 1  # 1 jest zawsze dzielnikiem dla n > 1
    
    # Sprawdzamy dzielniki do pierwiastka z n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Unikamy podwójnego liczenia dla kwadratów idealnych
                total += n // i
                
    return total

def are_amicable(a, b):
    """
    Sprawdza, czy liczby a i b są liczbami zaprzyjaźnionymi.
    """
    if a == b:
        return False  # Liczby muszą być różne
        
    sum_a = sum_proper_divisors(a)
    sum_b = sum_proper_divisors(b)
    
    return sum_a == b and sum_b == a

def main():
    parser = argparse.ArgumentParser(description='Sprawdź, czy podana para liczb to liczby zaprzyjaźnione.')
    parser.add_argument('a', type=int, help='Pierwsza liczba')
    parser.add_argument('b', type=int, help='Druga liczba')
    args = parser.parse_args()

    if are_amicable(args.a, args.b):
        print(f"TAK: Liczby {args.a} i {args.b} są zaprzyjaźnione.")
        print(f"Suma dzielników {args.a}: {sum_proper_divisors(args.a)}")
        print(f"Suma dzielników {args.b}: {sum_proper_divisors(args.b)}")
    else:
        print(f"NIE: Liczby {args.a} i {args.b} NIE są zaprzyjaźnione.")
        print(f"Suma dzielników {args.a}: {sum_proper_divisors(args.a)}")
        print(f"Suma dzielników {args.b}: {sum_proper_divisors(args.b)}")

if __name__ == "__main__":
    main()
