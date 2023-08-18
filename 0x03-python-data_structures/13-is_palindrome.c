#include "lists.h"

/**
 * list_len - returns number of elements in list_t.
 * @h: head.
 * Return: number of elements.
 */
unsigned int list_len(listint_t **h)
{
	unsigned int store = 0;

	while (*h != NULL)
	{
		store = store + 1;
		*h = (*h)->next;
	}
	return (store);
}

/**
* is_palindrome - checks if a linked list is palindromic.
* @head: pointer to head node of linked list.
* Return: 1 if is palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	unsigned int len, i = 0;
	int store[1024];

	temp = *head;
	/* NO LIST FOUND */
	if (head == NULL)
		return (0);
	/* LIST EMPTY */
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	len = list_len(head);
	while (temp != NULL)
	{
		store[i] = temp->n;
		temp = temp->next;
		i = i + 1;
	}

	for (i = 0; i <= (len / 2); i++)
	{
		/* IS NOT PALINDROMIC */
		if (store[i] != store[len - i - 1])
			return (0);
	}
	/* IS PALINDROMIC */
	return (1);
}
