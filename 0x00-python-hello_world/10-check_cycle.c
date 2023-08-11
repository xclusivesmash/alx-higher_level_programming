#include "lists.h"

/**
 * check_cycle - checks for a loop in a
 * singly linked list.
 * @list: head node of the list.
 * Return: 0 if no cycle exists, otherwise 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *store, *move;

	if (list == NULL)
		return (0);
	store = list;
	move = list;
	while (move != NULL && move->next != NULL)
	{
		store = store->next;
		move = move->next->next;
		/* CHECK FOR CYCLE EXISTENCE */
		if (store == move)
			return (1);
	}
	/* RETURN 0 BY DEFAULT */
	return (0);
}
