#!/usr/bin/env python3
import argparse

# Global cache for Collatz sequences
_cache = {}
_cache_stats = {'hits': 0, 'misses': 0}

def generate_collatz_sequence(n, use_cache=True):
    """
    Generuje ciąg Collatza dla zadanej liczby n.
    
    Zasady:
    - Jeśli n jest parzyste: n/2
    - Jeśli n jest nieparzyste: 3n+1
    - Kontynuuj aż dojdziesz do 1
    
    Args:
        n: Liczba początkowa
        use_cache: Czy użyć cache (domyślnie True)
    
    Zwraca krotkę: (sekwencja, długość, maksymalna wartość)
    """
    if n <= 0:
        raise ValueError("Liczba musi być większa od 0")
    
    # Sprawdź czy wynik jest w cache
    if use_cache and n in _cache:
        _cache_stats['hits'] += 1
        return _cache[n]
    
    _cache_stats['misses'] += 1
    
    sequence = [n]
    original_n = n
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        
        # Jeśli napotkaliśmy liczbę w cache, użyj jej
        if use_cache and n in _cache:
            cached_seq, _, _ = _cache[n]
            sequence.extend(cached_seq)
            break
        else:
            sequence.append(n)
    
    result = (sequence, len(sequence), max(sequence))
    
    # Zapisz w cache
    if use_cache:
        _cache[original_n] = result
    
    return result

def main():
    parser = argparse.ArgumentParser(
        description='Generuj ciąg Collatza (hipoteza 3n+1) dla zadanej liczby.'
    )
    parser.add_argument('n', type=int, help='Liczba początkowa (dodatnia liczba całkowita)')
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='Pokaż pełną sekwencję')
    parser.add_argument('--cache-stats', action='store_true',
                       help='Pokaż statystyki cache')
    parser.add_argument('--no-cache', action='store_true',
                       help='Wyłącz cache (dla testów)')
    args = parser.parse_args()

    if args.n <= 0:
        print("Błąd: Liczba musi być większa od 0")
        return

    use_cache = not args.no_cache
    sequence, length, max_value = generate_collatz_sequence(args.n, use_cache=use_cache)
    
    print(f"Ciąg Collatza dla liczby {args.n}:")
    print(f"  Długość sekwencji: {length}")
    print(f"  Maksymalna wartość: {max_value}")
    
    if args.cache_stats:
        print(f"  Cache statystyki:")
        print(f"    Trafienia: {_cache_stats['hits']}")
        print(f"    Chybienia: {_cache_stats['misses']}")
        print(f"    Rozmiar cache: {len(_cache)}")
    
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
