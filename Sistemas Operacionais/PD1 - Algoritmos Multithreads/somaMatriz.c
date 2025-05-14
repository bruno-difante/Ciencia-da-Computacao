#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int **A, **B, **C;
int N, M;

typedef struct {
    int row;
} ThreadData;

void *soma_linha(void *arg) {
    ThreadData *data = (ThreadData *)arg;
    int i = data->row;
    for (int j = 0; j < M; j++) {
        C[i][j] = A[i][j] + B[i][j];
    }
    pthread_exit(NULL);
}

int main() {
    printf("Digite as dimensões da matriz (N linhas, M colunas): ");
    scanf("%d %d", &N, &M);

    A = malloc(N * sizeof(int *));
    B = malloc(N * sizeof(int *));
    C = malloc(N * sizeof(int *));
    for (int i = 0; i < N; i++) {
        A[i] = malloc(M * sizeof(int));
        B[i] = malloc(M * sizeof(int));
        C[i] = malloc(M * sizeof(int));
    }

    printf("Digite os elementos da matriz A:\n");
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            scanf("%d", &A[i][j]);

    printf("Digite os elementos da matriz B:\n");
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            scanf("%d", &B[i][j]);

    pthread_t threads[N];
    ThreadData data[N];

    for (int i = 0; i < N; i++) {
        data[i].row = i;
        pthread_create(&threads[i], NULL, soma_linha, &data[i]);
    }

    for (int i = 0; i < N; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Resultado da soma:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    return 0;
}
