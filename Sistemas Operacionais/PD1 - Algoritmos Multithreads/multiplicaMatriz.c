#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int **A, *V, *R;
int N;

typedef struct {
    int row;
} ThreadData;

void *multiplica_linha(void *arg) {
    ThreadData *data = (ThreadData *)arg;
    int i = data->row;
    R[i] = 0;
    for (int j = 0; j < N; j++) {
        R[i] += A[i][j] * V[j];
    }
    pthread_exit(NULL);
}

int main() {
    printf("Digite o valor de N (dimensão da matriz NxN): ");
    scanf("%d", &N);

    A = malloc(N * sizeof(int *));
    for (int i = 0; i < N; i++) {
        A[i] = malloc(N * sizeof(int));
    }
    V = malloc(N * sizeof(int));
    R = malloc(N * sizeof(int));

    printf("Digite os elementos da matriz A:\n");
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            scanf("%d", &A[i][j]);

    printf("Digite os elementos do vetor V:\n");
    for (int i = 0; i < N; i++)
        scanf("%d", &V[i]);

    pthread_t threads[N];
    ThreadData data[N];

    for (int i = 0; i < N; i++) {
        data[i].row = i;
        pthread_create(&threads[i], NULL, multiplica_linha, &data[i]);
    }

    for (int i = 0; i < N; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Resultado da multiplicação (vetor R):\n");
    for (int i = 0; i < N; i++) {
        printf("%d\n", R[i]);
    }

    return 0;
}
