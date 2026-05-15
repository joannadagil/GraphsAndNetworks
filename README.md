# Grafy i sieci - projekt zaliczeniowy

Zadaniem jest stworzenie algorytu znajdowania trójkątów w grafie spójnym.

## Założenia

**GRAF SPÓJNY** - graf nieskierowany, w którym istnieje ścieżka między każdymi dwoma wierzchołkami

**TRÓJKĄT** - cykl (podgraf pełny K_3 - klika), składający się z trzech wierzchołków, z których każdy jest połączony krawędzią z pozostałymi dwoma

Zakładamy zatem, że graf może nie być **prosty** - a więc mogą występować **pętle** i **krawędzie wielokrotne**. Krawęzie wielokrote będą liczone jako wielokrotne trójkąty.

Natomiast - jak w powyższej definicji spójności - zakładamy, że graf **nie jest skierowany**.

## Wejście

$v$ - numer krawędzi grafu

$e$ - macierz sąsiedztwa grafu

## Wyjście

lista wszystkich trójkątów znajdujących się w grafie

## Złożoność

$$
O\left(|v|^3\right)
$$

Metoda jest optymalna dla gęstszych grafów.
