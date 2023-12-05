#include "lists.h"

/**
 * check_cycle -checks if singly linked list has cycle
 * @list: pointer to head of linked list
 *
 * Return 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise =list;
	listint_t *hare = list;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise ==hare)
			return (1);
	}
	return (0);
}
