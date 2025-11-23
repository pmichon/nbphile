# nbphile: Eksperymenty z ciągami liczbowymi

Repozytorium `nbphile` (Number Phile) służy do eksperymentowania z różnymi ciągami liczbowymi w języku Python. Projekt jest inspirowany repozytorium [primes](https://github.com/pmichon/primes) i ma na celu rozwijanie narzędzi matematycznych.

## 📋 Spis treści

- [Funkcjonalności](#funkcjonalności)
- [Instalacja](#instalacja)
- [Narzędzia](#narzędzia)
- [Wymagania](#wymagania)
- [Licencja](#licencja)

## ✨ Funkcjonalności

Obecnie projekt oferuje:
- 🔢 **Generator ciągu Fibonacciego** - prosty skrypt do generowania n pierwszych wyrazów ciągu.
- 🤝 **Sprawdzanie liczb zaprzyjaźnionych** - skrypt weryfikujący czy dwie liczby są liczbami zaprzyjaźnionymi.
- 🔄 **Ciąg Collatza (hipoteza 3n+1)** - generator ciągu Collatza z wizualizacją długości i maksymalnej wartości.

W przyszłości planowane są kolejne eksperymenty z ciągami liczbowymi.

## 🚀 Instalacja

### Wymagania

- Python 3.8+

### Klonowanie repozytorium

```bash
git clone https://github.com/pmichon/nbphile.git
cd nbphile
```

## 🛠️ Narzędzia

### 1. Generator Ciągu Fibonacciego (`fibonacci.py`)

Wypisuje zadaną liczbę pierwszych elementów ciągu Fibonacciego.

```bash
# Wypisz 10 pierwszych elementów
python3 fibonacci.py 10
```

**Wynik:**
```
Pierwsze 10 elementów ciągu Fibonacciego:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### 2. Sprawdzanie Liczb Zaprzyjaźnionych (`amicable.py`)

Sprawdza, czy podana para liczb to liczby zaprzyjaźnione (suma dzielników właściwych jednej liczby równa się drugiej i odwrotnie).

```bash
# Sprawdź parę liczb 220 i 284
python3 amicable.py 220 284
```

**Wynik:**
```
TAK: Liczby 220 i 284 są zaprzyjaźnione.
Suma dzielników 220: 284
Suma dzielników 284: 220
```

### 3. Generator Ciągu Collatza (`collatz.py`)

Generuje ciąg Collatza (hipoteza 3n+1) dla zadanej liczby. Ciąg powstaje według zasad:
- Jeśli n parzyste: n/2
- Jeśli n nieparzyste: 3n+1
- Kontynuuj aż dojdziesz do 1

```bash
# Podstawowe użycie
python3 collatz.py 13

# Tryb verbose - pełna sekwencja
python3 collatz.py 27 --verbose

# Statystyki cache
python3 collatz.py 27 --cache-stats

# Wyłącz cache (dla testów)
python3 collatz.py 27 --no-cache

# Generuj sekwencje dla zakresu liczb
python3 collatz.py --range 10 15

# Tylko statystyki (bez pełnej sekwencji)
python3 collatz.py 27 --stats-only
python3 collatz.py --range 10 13 --stats-only

# Eksport do CSV (jedna sekwencja)
python3 collatz.py 13 --csv sekwencja.csv

# Eksport zakresu do CSV (wiele sekwencji, każda w nowej linii)
python3 collatz.py --range 5 20 --csv sekwencje.csv
```

**Wynik:**
```
Ciąg Collatza dla liczby 13:
  Długość sekwencji: 10
  Maksymalna wartość: 40
  Sekwencja: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

**Wynik dla zakresu:**
```
Wygenerowano sekwencje dla zakresu [10, 15]:
  Liczba sekwencji: 6
  Średnia długość: 13.00
  Najdłuższa sekwencja: 18 (dla n=14)
```

**Wynik dla --stats-only:**
```
n=27: first: 27, len: 112, max: 9232, mean: 905.71, median: 357.00, stdev: 1491.24
```

**Cache:** Skrypt automatycznie cache'uje obliczone sekwencje, aby przyspieszyć kolejne obliczenia dla liczb o wspólnych podsekwencjach.

**Format CSV:** Każda linia w pliku CSV zawiera jedną sekwencję jako wartości oddzielone przecinkami.

## 🤝 Współpraca

Zapraszamy do zgłaszania pomysłów na nowe ciągi liczbowe i ulepszenia!

## 📄 Licencja

Projekt udostępniony na licencji MIT. Zobacz plik [LICENSE](LICENSE) dla szczegółów.

Copyright (c) 2025 pmichon
