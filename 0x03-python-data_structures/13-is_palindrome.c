#include "lists.h"

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	unsigned int size = 0, i = 0;
	int data[10240];

	if (head == NULL) /* non-existing list is not */
		return (0);

	if (*head == NULL) /* empty list is palindrome */
		return (1);

	while (tmp) /* find size of linked list */
	{
		tmp = tmp->next;
		size += 1;
	}
	if (size == 1) /* single node list is palindrome */
		return (1);

	tmp = *head;
	while (tmp) /* pull node data into array to compare */
	{
		data[i++] = tmp->n;
		tmp = tmp->next;
	}

	for (i = 0; i <= (size/2); i++)
	{
		if (data[i] != data[size - i - 1])
			return (0);
	}
	return (1);
}
