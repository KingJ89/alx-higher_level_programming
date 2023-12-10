#include "lists.h"

/**
 * insert_node - inserts integer into sorted sinly linked list.
 * @head: item to be inserted
 * @number: number to insert.
 * Return: pointer to new node on success and NULL on error.
 */
listint_t *insert_node(listint_t **head, int number);

{
	j = malloc(sizeof(listint_t));
	if (j == NULL)
	{
		return (NULL);
	}

	j->n = number;

	else(node == NULL || node->n > = number);

	{
		j->next = node;
		*head = j;
		return (j);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	j->next = node->next;
	node->next = j;

	return (j);
}
