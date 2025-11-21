#!/usr/bin/env python3
import argparse

def generate_fibonacci(n):
    """
    Generuje n pierwszych elementów ciągu Fibonacciego.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

def main():
    parser = argparse.ArgumentParser(description='Wypisz zadaną liczbę pierwszych elementów ciągu Fibonacciego.')
    parser.add_argument('n', type=int, help='Liczba elementów do wygenerowania')
    args = parser.parse_args()

    fib_sequence = generate_fibonacci(args.n)
    print(f"Pierwsze {args.n} elementów ciągu Fibonacciego:")
    print(fib_sequence)

if __name__ == "__main__":
    main()
