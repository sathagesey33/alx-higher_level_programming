#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>

/**
* struct lisintager_t - singly link lists
* @s: intager
* @next: points to the next node
*/
typedef struct lisintager_t
{
	int s;
	struct lisintager_t *next;
} lisintager_s;

size_t print_lisintager(const lisintager_t *h);
lisintager_t *add_nodeint(lisintager_t **head, const int n);
void free_lisintager(lisintager_t *head);
int check_cycle(lisintager_t *list);

#endif /* LISTS_H */


 

