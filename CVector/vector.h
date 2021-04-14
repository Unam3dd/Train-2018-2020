#include <stdlib.h>
#include <stdbool.h>

#define CAPACITY 4
#define VECTOR_VERSION "0.1"
#define VECTOR_AUTHOR "unam3dd"

typedef struct Vector
{
    void **items;
    int capacity;
    int total;
    void (*init)(struct Vector *v);
    void (*free)(struct Vector *v);
    void (*push_back)(struct Vector *v,void *value);
    void (*pop_back)(struct Vector *v);
    void *(*get)(struct Vector *v,int index);
    int (*get_capacity)(struct Vector *v);
    int (*get_total)(struct Vector *v);
    int (*replace)(struct Vector *v,int index,void *value);
    bool (*isEmpty)(struct Vector *v);
    void *(*get_items)(struct Vector *v);
} Vector;

void vector_object(Vector *v);
void vector_init(Vector *v);
void vector_free(Vector *v);
static void vector_realloc(Vector *v,int capacity);
void vector_push_back(Vector *v,void *value);
void vector_pop_back(Vector *v);
void *vector_get(Vector *v,int index);
int get_vector_capacity(Vector *v);
int get_vector_total(Vector *v);
int vector_replace(Vector *v,int index,void *value);
bool vector_empty(Vector *v);
void * vector_get_items(Vector *v);