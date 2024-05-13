#include <stdio.h>
#include <stdlib.h>
#include <time.h>
/**
 * @brief Estructura para representar un punto en un plano xy
 * @param x Coordenada x del punto.
 * @param y Coordenada y del punto.
 * @param next Puntero al siguiente punto en la lista.
 */
typedef struct point {
    int x;
    int y;
    struct point* next;
} point;

/**
 * @brief Agrega un nuevo punto a la cabeza de la lista.
 * @param head Puntero al primer punto de la lista.
 * @param x Coordenada x del nuevo punto.
 * @param y Coordenada y del nuevo punto.
 * @return Puntero al nuevo primer punto de la lista.
 */
point* add_point(point* head, int x, int y) {
    point* new_point = (point*)malloc(sizeof(point));
    new_point->x = x;
    new_point->y = y;
    new_point->next = head;
    return new_point;
}

/**
 * @brief Elimina un punto de la lista por su coordenada x.
 * @param head Puntero al primer punto de la lista.
 * @param x Coordenada x del punto a eliminar.
 * @return Puntero al primer punto de la lista después de la eliminación.
 */
point* delete_point(point* head, int x) {
    point* temp = head, *prev;

    if (temp != NULL && temp->x == x) {
        head = temp->next;
        free(temp);
        return head;
    }

    while (temp != NULL && temp->x != x) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) return head;

    prev->next = temp->next;
    free(temp);

    return head;
}

/**
 * @brief Elimina puntos duplicados basados en x y deja solo el de mayor y.
 * @param head Puntero al primer punto de la lista.
 * @return Puntero al primer punto de la lista después de eliminar duplicados.
 */
point* remove_duplicates(point* head) {
    point *ptr1, *ptr2, *dup;
    ptr1 = head;

    while (ptr1 != NULL && ptr1->next != NULL) {
        ptr2 = ptr1;

        while (ptr2->next != NULL) {
            if (ptr1->x == ptr2->next->x) {
                if (ptr1->y < ptr2->next->y)
                    ptr1->y = ptr2->next->y;

                dup = ptr2->next;
                ptr2->next = ptr2->next->next;
                free(dup);
            } else {
                ptr2 = ptr2->next;
            }
        }
        ptr1 = ptr1->next;
    }
    return head;
}

/**
 * @brief Agrega los puntos del contorno de un rectángulo a la lista.
 * @param head Puntero al primer punto de la lista.
 * @param x1 Coordenada x del primer punto del rectángulo.
 * @param y Coordenada y de los puntos del rectángulo.
 * @param x2 Coordenada x del último punto del rectángulo.
 * @return Puntero al primer punto de la lista después de agregar los puntos del rectángulo.
 */
point* add_rectangle_points(point* head, int x1, int y, int x2) {
    for (int x = x1; x <= x2; x++) {
        head = add_point(head, x, y);
    }
    return head;
}

/**
 * @brief Imprime los puntos de la lista.
 * @param head Puntero al primer punto de la lista.
 */
void print_points(point* head) {
    point* temp = head;
    while (temp != NULL) {
        printf("(%d, %d).", temp->x, temp->y);
        temp = temp->next;
    }
}

/**
 * @brief Función principal que agrega puntos de rectángulos a una lista, elimina duplicados y los imprime.
 * @return 0 si el programa se ejecuta correctamente.
 */

int main() {
    // Semilla para los aleatorios
    srand(time(NULL));

    // Lista ligada simple
    point* head = NULL;
    int n, max_x2 = 0;

    printf("Ingrese el número de rectángulos: ");
    scanf("%d", &n);

    // Crear una matriz para almacenar los valores de x1, y, x2
    int rectangulos[n][3];
    for (int i = 0; i < n; i++) {
        rectangulos[i][0] = rand() %10 +1; // x1
        rectangulos[i][2] = rectangulos[i][0] + (rand() % (20-rectangulos[i][0])); // x2
        rectangulos[i][1] = rand() %10 +1; // y
        if (rectangulos[i][2] > max_x2) {
            max_x2 = rectangulos[i][2];
        }
    }
    clock_t start = clock();
    // Recorrer la matriz para añadir los puntos del rectángulo
    for (int i = 0; i < n; i++) {
        head = add_rectangle_points(head, rectangulos[i][0], rectangulos[i][1], rectangulos[i][2]-1);
    }

    // Agregar un rectángulo que vaya desde 0 hasta el x2 mayor
    head = add_rectangle_points(head, 0, 0, max_x2);

    // Eliminar duplicados
    head = remove_duplicates(head);

    clock_t end = clock();

    // Calcular e imprimir el tiempo transcurrido en segundos
    double elapsed_time = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Tiempo transcurrido en segundos: %.15f\n", elapsed_time);

    // Imprimir los puntos de la lista
    print_points(head);

    return 0;
}

