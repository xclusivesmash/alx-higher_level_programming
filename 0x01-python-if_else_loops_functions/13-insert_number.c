#include "lists.h"

/**
 * insert_node - adds a node to a sorted
 * linked list.
 * @head: head node of the list.
 * @number: input integer.
 * Return: pointer to new node or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		(*head)->next = NULL;
		return (new);
	}
	if ((*head)->next == NULL)
	{
		if ((*head)->n < new->n)
			(*head)->next = new;
		else
		{
			new->next = *head;
			*head = new;
		}
		return (new);
	}
	tmp = *head;
	while (tmp->next != NULL)
	{
		if (new->n < tmp->n)
		{
			new->next = tmp;
			*head = new;
			return (new);
		}
		if (((new->n > tmp->n) && (new->n < (tmp->next)->n)) ||
		    (new->n == tmp->n))
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	tmp->next = new;
	return (new);
}
