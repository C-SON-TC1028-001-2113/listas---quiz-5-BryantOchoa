def diagonal1(matriz):
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
    return diagonal

def matriz_hecha(N,M):
    matriz = []
    if N == M:
        for i in range(N):
            matriz.append([])
            for j in range (M):
                matriz[i].append(int(input()))
    return matriz

def main():
    N = int(input())
    M = int(input())
    if N != M:
        print("La matriz no es cuadrada")
    else:
        Mat = matriz_hecha(N, M)
        print(diagonal1(Mat))
if __name__=='__main__':
    main()
