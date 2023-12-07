#include "lists.h"

/**
 * check_cycle - checks cycle and cyclic redundancies
 * @list: linked list head
 * Return: 0on error, 1 on success
 */
int check_cycle(listint_t *list)
{
	listint_t *top, *bottom;

	if (!list || !list->next)
		return (0);

	top = list;
	bottom = list->next;
	while (bottom && bottom->next)

		if (top == bottom)
			return (1);

	top = top->next;
	bottom = bottom->next->next;
	return (0);
}
