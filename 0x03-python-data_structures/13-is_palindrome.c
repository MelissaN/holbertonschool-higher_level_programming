#include "lists.h"

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *beg = *head;
	listint_t *end = *head;

	if (head == NULL) /* non-existing list is not */
		return (0);

	if (*head == NULL) /* empty list is palindrome */
		return (1);

	while (end->next != NULL)
		end = end->next;

	while (beg->n == end->n)
	{
		if (beg->next == end || beg == end)
			return (1);
		beg = beg->next;
		end = beg;
		while (end->next->next != NULL)
			end = end->next;
		end->next = NULL;
	}
	return (0);
}
