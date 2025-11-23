#!/usr/bin/env python3
import argparse
import csv

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

def save_sequences_to_csv(sequences, filename):
    """
    Zapisuje sekwencje do pliku CSV.
    Każda linia zawiera jedną sekwencję oddzieloną przecinkami.
    
    Args:
        sequences: Lista krotek (n, sequence, length, max_value)
        filename: Nazwa pliku wyjściowego
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for n, seq, _, _ in sequences:
            writer.writerow(seq)
    print(f"Zapisano {len(sequences)} sekwencji do {filename}")

def main():
    parser = argparse.ArgumentParser(
        description='Generuj ciąg Collatza (hipoteza 3n+1) dla zadanej liczby lub zakresu.'
    )
    parser.add_argument('n', type=int, nargs='?', help='Liczba początkowa (dodatnia liczba całkowita)')
    parser.add_argument('--range', nargs=2, type=int, metavar=('START', 'END'),
                       help='Generuj sekwencje dla zakresu [START, END]')
    parser.add_argument('--csv', type=str, metavar='FILE',
                       help='Zapisz sekwencje do pliku CSV')
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='Pokaż pełną sekwencję')
    parser.add_argument('--cache-stats', action='store_true',
                       help='Pokaż statystyki cache')
    parser.add_argument('--no-cache', action='store_true',
                       help='Wyłącz cache (dla testów)')
    args = parser.parse_args()

    # Walidacja argumentów
    if args.range is None and args.n is None:
        parser.error("Musisz podać liczbę lub użyć --range")
    
    if args.range and args.n:
        parser.error("Nie możesz używać jednocześnie liczby i --range")

    use_cache = not args.no_cache
    
    # Tryb zakresu
    if args.range:
        start, end = args.range
        if start <= 0 or end <= 0:
            print("Błąd: Liczby w zakresie muszą być większe od 0")
            return
        if start > end:
            print("Błąd: START musi być mniejsze lub równe END")
            return
        
        sequences = []
        total_length = 0
        max_length = 0
        max_length_n = 0
        
        total_count = end - start + 1
        show_progress = args.csv and total_count > 1
        
        for i, n in enumerate(range(start, end + 1), 1):
            seq, length, max_val = generate_collatz_sequence(n, use_cache=use_cache)
            sequences.append((n, seq, length, max_val))
            total_length += length
            if length > max_length:
                max_length = length
                max_length_n = n
            
            # Pokazuj postęp dla CSV z wieloma sekwencjami
            if show_progress:
                percent = (i / total_count) * 100
                print(f"\rGenerowanie sekwencji: {i}/{total_count} ({percent:.1f}%)", end='', flush=True)
        
        if show_progress:
            print()  # Nowa linia po zakończeniu
        
        # Zapis do CSV jeśli podano
        if args.csv:
            save_sequences_to_csv(sequences, args.csv)
        else:
            # Wyświetl podsumowanie
            print(f"Wygenerowano sekwencje dla zakresu [{start}, {end}]:")
            print(f"  Liczba sekwencji: {len(sequences)}")
            print(f"  Średnia długość: {total_length / len(sequences):.2f}")
            print(f"  Najdłuższa sekwencja: {max_length} (dla n={max_length_n})")
            
            if args.cache_stats:
                print(f"  Cache statystyki:")
                print(f"    Trafienia: {_cache_stats['hits']}")
                print(f"    Chybienia: {_cache_stats['misses']}")
                print(f"    Rozmiar cache: {len(_cache)}")
            
            if args.verbose:
                print(f"\nSzczegóły sekwencji:")
                for n, seq, length, max_val in sequences:
                    print(f"  n={n}: długość={length}, max={max_val}")
                    print(f"    {','.join(map(str, seq))}")
    
    # Tryb pojedynczej liczby
    else:
        if args.n <= 0:
            print("Błąd: Liczba musi być większa od 0")
            return

        sequence, length, max_value = generate_collatz_sequence(args.n, use_cache=use_cache)
        
        # Zapis do CSV jeśli podano
        if args.csv:
            save_sequences_to_csv([(args.n, sequence, length, max_value)], args.csv)
        else:
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
                    start_seq = ' → '.join(map(str, sequence[:5]))
                    end_seq = ' → '.join(map(str, sequence[-3:]))
                    print(f"  Sekwencja: {start_seq} → ... → {end_seq}")
                    print(f"  (użyj --verbose aby zobaczyć pełną sekwencję)")

if __name__ == "__main__":
    main()
