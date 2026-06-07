def find_triangles(v, e):
    '''
    v - number of vertices
    e - adjacency matrix
    returns a list of triangles in the graph
    multiple edges are counted as multiple triangles
    '''
    triangles = []
    for a in range(v):
        for b in range(a+1, v):
            for c in range(b+1, v):
                n = e[a][b] * e[b][c] * e[c][a]
                #if n > 0: print("(", a," ", b , " ", c, ") = ", n)
                for _ in range(n): triangles.append((a,b,c))
                #print(triangles)
    return triangles


def read_graph_by_neighbours():
    v = int(input("Podaj liczbę wierzchołków: "))

    temp = [[0 for _ in range(v)] for _ in range(v)]

    print()
    print("Podaj sąsiadów każdego wierzchołka.")
    print("Numery oddzielaj spacją.")
    print("Jeśli wierzchołek nie ma sąsiadów, zostaw pustą linię.")
    print("Graf jest nieskierowany, więc 0-1 i 1-0 oznacza tę samą krawędź.")
    print("Jeśli wpiszesz ten sam numer kilka razy, oznacza to krawędzie wielokrotne.")
    print("Przykład: dla dwóch krawędzi między 0 i 1 wpisz przy 0: 1 1")
    print("Jeśli liczba powtórzeń różni się po obu stronach, program przyjmie większą liczbę.")
    print()

    for a in range(v):
        line = input(f"Sąsiedzi wierzchołka {a}: ")

        if line.strip() == "":
            continue

        neighbours = list(map(int, line.split()))

        for b in neighbours:
            if b < 0 or b >= v:
                print("Błąd: podano wierzchołek spoza zakresu.")
                exit()

            if a == b:
                print("Pętla została zapisana, ale nie będzie brana pod uwagę przy szukaniu trójkątów.")
                continue

            temp[a][b] += 1

    e = [[0 for _ in range(v)] for _ in range(v)]

    for i in range(v):
        for j in range(i + 1, v):
            edges_count = max(temp[i][j], temp[j][i])
            e[i][j] = edges_count
            e[j][i] = edges_count

    return v, e


def read_graph_by_edges():
    v = int(input("Podaj liczbę wierzchołków: "))
    m = int(input("Podaj liczbę krawędzi: "))

    e = [[0 for _ in range(v)] for _ in range(v)]

    print()
    print("Podawaj krawędzie w formacie: początek koniec")
    print("Przykład: 0 2")
    print("Graf jest nieskierowany, więc krawędź 0 2 oznacza też połączenie 2 0.")
    print("Jeśli istnieją krawędzie wielokrotne, wpisz tę samą krawędź kilka razy.")
    print()

    for i in range(m):
        a, b = map(int, input(f"Krawędź {i + 1}: ").split())

        if a < 0 or a >= v or b < 0 or b >= v:
            print("Błąd: podano wierzchołek spoza zakresu.")
            exit()

        if a == b:
            print("Pętla została zapisana, ale nie będzie brana pod uwagę przy szukaniu trójkątów.")
            continue

        e[a][b] += 1
        e[b][a] += 1

    return v, e


def example_graph():
    v = 5
    e = [[0 for _ in range(v)] for _ in range(v)]

    e[0][1] += 1
    e[1][0] += 1

    e[0][3] += 1
    e[3][0] += 1

    e[1][3] += 1
    e[3][1] += 1

    e[1][2] += 1
    e[2][1] += 1

    e[2][3] += 1
    e[3][2] += 1

    e[0][2] += 1
    e[2][0] += 1

    e[3][4] += 1
    e[4][3] += 1

    return v, e

def print_edges(v, e):
    print("Krawędzie grafu:")

    for i in range(v):
        for j in range(i + 1, v):
            if e[i][j] > 0:
                if e[i][j] == 1:
                    print(f"{i} -- {j}")
                else:
                    print(f"{i} -- {j}, liczba krawędzi: {e[i][j]}")

def print_results(v, e):
    triangles = find_triangles(v, e)

    print()
    print_edges(v, e)

    print()
    print("Macierz sąsiedztwa:")
    for row in e:
        print(row)

    print()
    print("Znalezione trójkąty:")
    for triangle in triangles:
        print(triangle)

    print()
    print("Liczba trójkątów:", len(triangles))


def main():
    print("Wybierz sposób wprowadzenia grafu:")
    print("1 - lista sąsiadów")
    print("2 - lista krawędzi")
    print("3 - przykład testowy")

    choice = input("Twój wybór: ")

    if choice == "1":
        v, e = read_graph_by_neighbours()
        print_results(v, e)

    elif choice == "2":
        v, e = read_graph_by_edges()
        print_results(v, e)

    elif choice == "3":
        v, e = example_graph()

        print()
        print("Przykład podstawowy:")
        print_results(v, e)

        e[0][2] += 1
        e[2][0] += 1

        print()
        print("Przykład z krawędzią wielokrotną między 0 i 2:")
        print_results(v, e)

    else:
        print("Niepoprawny wybór.")


main()
input("\nNaciśnij Enter, aby zakończyć program...")