#include "vector.h"

void vector_object(Vector *v)
{
    v->free = vector_free;
    v->init = vector_init;
    v->push_back = vector_push_back;
    v->pop_back = vector_pop_back;
    v->get = vector_get;
    v->get_capacity = get_vector_capacity;
    v->get_total = get_vector_total;
    v->replace = vector_replace;
    v->isEmpty = vector_empty;
    v->get_items = vector_get_items;
}

void vector_init(Vector *v)
{
    v->total = 0;
    v->capacity = CAPACITY;
    v->items = malloc(sizeof(void *) * v->capacity);
}

void vector_free(Vector *v)
{
    free(v->items);
}


int vector_replace(Vector *v,int index,void *value)
{
    if (index < 0 || index >= v->total){
        return (0);
    }

    v->items[index] = value;
    return (1);
}

void vector_push_back(Vector *v,void *value)
{
    int x = v->total;
    if (x == v->capacity)
        vector_realloc(v,v->capacity * (CAPACITY / 2));
    
    if (x != 0)
        v->items[x++] = value;
    else
        v->items[x] = value;
    
    v->total++;
}

void vector_pop_back(Vector *v)
{
    int i = 1;

    for (i;i<v->total - 1;i++)
    {
        if (i != 1)
            v->items[i] = v->items[i - 1];
    }

    v->items[i + 1] = NULL;

    v->total--;

    if (v->total > 0 && v->total == v->capacity / (CAPACITY / 2))
        vector_realloc(v,v->capacity / (CAPACITY / 2));
}

void vector_realloc(Vector *v,int capacity)
{
    void **newitems = realloc(v->items,sizeof(void *) * capacity);

    if (newitems){
        v->items = newitems;
        v->capacity = capacity;
    }
}

void *vector_get(Vector *v,int index)
{
    if (index >= 0 && index < v->total)
        return (v->items[index]);
    
    return (NULL);
}

int get_vector_capacity(Vector *v)
{
    return (v->capacity);
}

int get_vector_total(Vector *v)
{
    return (v->total);
}

bool vector_empty(Vector *v)
{
    if (v->total != 0)
        return (false);
    
    return (true);
}

void * vector_get_items(Vector *v)
{
    return (v->items);
}