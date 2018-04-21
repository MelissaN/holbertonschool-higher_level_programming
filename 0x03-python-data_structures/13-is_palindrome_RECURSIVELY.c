#include "lists.h"

/**
 * is_pal - recursively moves pointer to linked list node and match
 * @start: pointer to head (** gives different address so not same as end)
 * @end: pointer to last node
 * Return: 0 if not, 1 if palindrome
 */
int is_pal(listint_t **start, listint_t *end)
{
	if (end == NULL) /* pop off stack once ptr hits null; ptr is at end */
		return (1);

	/* recursively move end ptr to end; match; move ptrs inwards */
	if (is_pal(start, end->next) && ((*start)->n == end->n))
	{
		*start = (*start)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = *head;
	listint_t *end = *head;

	if (head == NULL) /* non-existing list is not */
		return (0);
	if (*head == NULL) /* one node list is palindrome */
		return (1);
	return (is_pal(&start, end));
}
