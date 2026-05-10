# GraphsAndNetworks
Project from graphs and networks course.

- co to znaczy "znajdowanie trójkątów" - chcemy je wypisać czy policzyć ile istnieje?
- czy graf musi być prosty? (pętle, krawędzie wielokrotne)

## Algorytm znajdowania trójkątów w grafie spójnym

**GRAF SPÓJNY** - graf nieskierowany, w którym istnieje ścieżka między każdymi dwoma wierzchołkami

**TRÓJKĄT** - cykl (podgraf pełny K_3 - klika), składający się z trzech wierzchołków, z których każdy jest połączony krawędzią z pozostałymi dwoma

## Podejście 1

Dla każdego wierzchołka sprawdzamy parami wszystkie wierzchołki, do których ma krawędź, czy mają krawędź między sobą.

$$
O\left(|V| \cdot \sum{\deg{(v_i)}!}\right) 
$$

(+ złożoność sprawdzenia istnienia krawędzi między wierzchołkami)


## Podejście 2

Mnożenie macierzy sąsiedztwa trzykrotnie. Dla każdego wierzchołka $i$ w macierzy na pozycji $(i,i)$ otrzymamy ilość ścieżek o długości 3 zaczynających i kończących się w tym wierzchołku.

O grafie wiadomo tylko, że jest spójny, a więc nie możemy weliminować możliwości, że nie jest prosty. Możemy jednak wyzerować krawędzie będące pętlami. W tym celu podmieniamy wartości na przekątnej grafu sąsiedztwa na 0.

Po wykonaniu potrójnego mnożenia takiej zmodyfikowanej macierzy otrzymujemy na przekątnej dla każdego wierzchołka liczbę trójkątów w których jest ten wierzchołek. Obliczamy sumę wartości na przekątnej i następnie dzielimy ją przez 3 - gdyż dla każdego trójkąta dokonaliśmy trzykrotnego zliczenia go - po jednym dla każdego wierzchołka.

Dla wielokrotnych krawędzi przyjmujemy interpretację, że wybór innej krawędzi między tymi samymi wierzchołkami liczy się oddzielnie.

$$
O\left(|V|^3\right)
$$

Metoda jest optymalniejsza dla gęstszych grafów.
