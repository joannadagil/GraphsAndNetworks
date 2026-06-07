# Grafy i sieci - projekt zaliczeniowy

Zadaniem jest stworzenie algorytmu znajdowania trójkątów w grafie spójnym.

## Założenia

**GRAF SPÓJNY** - graf nieskierowany, w którym istnieje ścieżka między każdymi dwoma wierzchołkami

**TRÓJKĄT** - cykl (podgraf pełny K_3 - klika), składający się z trzech wierzchołków, z których każdy jest połączony krawędzią z pozostałymi dwoma

Zakładamy zatem, że graf może nie być **prosty** - a więc mogą występować **pętle** i **krawędzie wielokrotne**. Krawęzie wielokrote będą liczone jako wielokrotne trójkąty.

Natomiast - jak w powyższej definicji spójności - zakładamy, że graf **nie jest skierowany**.

## Wejście

`v` - liczba wierzchołków grafu

`e` - macierz sąsiedztwa grafu, gdzie `e[i][j]` oznacza liczbę krawędzi między wierzchołkami `i` oraz `j`.

Program umożliwia użytkownikowi wprowadzenie grafu na dwa sposoby: przez listę sąsiadów albo przez listę krawędzi. Dostępny jest także przykład testowy. Niezależnie od wybranego sposobu wprowadzenia danych graf jest ostatecznie zapisywany w postaci macierzy sąsiedztwa, na której działa algorytm wyszukiwania trójkątów.

## Wyjście

Program wypisuje:

- listę krawędzi grafu,
- macierz sąsiedztwa,
- listę wszystkich trójkątów znajdujących się w grafie,
- liczbę znalezionych trójkątów.

Jeżeli między daną parą wierzchołków występuje więcej niż jedna krawędź, program wypisuje również liczbę krawędzi między tymi wierzchołkami.

## Złożoność

`O ( | V | ^3 )`

Algorytm sprawdza wszystkie możliwe trójki różnych wierzchołków. Dla każdej trójki wierzchołków sprawdzane jest, czy istnieją między nimi trzy wymagane krawędzie. Jeżeli tak, trójka zostaje dodana do listy znalezionych trójkątów.

Zastosowanie macierzy sąsiedztwa jest optymalne dla grafów gęstszych, ponieważ sprawdzenie liczby krawędzi między dwoma wierzchołkami odbywa się w czasie stałym.

## Opis działania algorytmu

Algorytm przechodzi po wszystkich trójkach wierzchołków `a`, `b`, `c` takich, że `a < b < c`. Dzięki temu każda trójka sprawdzana jest tylko raz.

Następnie dla danej trójki obliczana jest wartość:

`n = e[a][b] * e[b][c] * e[c][a]`

Jeżeli wartość `n` jest większa od zera, oznacza to, że pomiędzy wszystkimi trzema parami wierzchołków istnieją krawędzie, więc wierzchołki tworzą trójkąt.

W przypadku krawędzi wielokrotnych wartość `n` może być większa niż `1`. Wtedy trójkąt zostaje dodany do wyniku odpowiednią liczbę razy.

Przykład:

Jeżeli:

`e[0][1] = 1`  
`e[1][2] = 1`  
`e[2][0] = 2`

to trójka wierzchołków `0`, `1`, `2` zostanie policzona jako dwa trójkąty, ponieważ między wierzchołkami `2` oraz `0` istnieją dwie krawędzie.

## Instrukcja użytkownika

Program został przygotowany jako plik wykonywalny `.exe`.

Aby uruchomić program, należy otworzyć folder z plikiem programu i uruchomić plik `main.exe`.

Program działa w konsoli. Po uruchomieniu wyświetla menu:

`1 - lista sąsiadów`  
`2 - lista krawędzi`  
`3 - przykład testowy`

Po wybraniu opcji `1` użytkownik podaje liczbę wierzchołków, a następnie dla każdego wierzchołka wpisuje listę jego sąsiadów. Numery sąsiadów należy oddzielać spacją. Jeżeli wierzchołek nie ma sąsiadów, należy zostawić pustą linię.

W przypadku listy sąsiadów graf jest traktowany jako nieskierowany, więc połączenie `0-1` oraz `1-0` oznacza tę samą krawędź. Jeżeli użytkownik wpisze ten sam numer kilka razy, program traktuje to jako krawędzie wielokrotne. Jeśli liczba powtórzeń różni się po obu stronach, program przyjmuje większą liczbę.

Po wybraniu opcji `2` użytkownik podaje liczbę wierzchołków, liczbę krawędzi, a następnie wpisuje kolejne krawędzie w formacie `początek koniec`. Jeżeli w grafie występują krawędzie wielokrotne, tę samą krawędź należy wpisać kilka razy.

Po wybraniu opcji `3` program uruchamia przykład testowy. Program pokazuje graf bez dodatkowej krawędzi wielokrotnej oraz graf z dodatkową krawędzią wielokrotną.

Dla każdego przypadku program wypisuje krawędzie grafu, macierz sąsiedztwa, znalezione trójkąty oraz ich liczbę.

Po zakończeniu działania programu należy nacisnąć Enter, aby zamknąć okno konsoli.