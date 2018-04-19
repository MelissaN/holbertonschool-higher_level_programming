#include "lists.h"

/**
 * is_pal - recursively moves pointer to linked list node and match
 * @start: pointer to head (** gives different address so not same as end)
 * @end: pointer to last node
 * Return: 0 if not, 1 if palindrome
 */
int is_pal(listint_t **start, listint_t *end)
{
	int flag = 1;

	if (*start == NULL)
		return (0);

	/* hold ptr to start and recursively move ptr to end */
	if (end->next != NULL)
		flag = is_pal(start, end->next);

	if (flag == 0)
		return (0);

	/* if no match, change flag so next recursive call returns no */
	if ((*start)->n != end->n)
        	return (0);

	/* if start and end match, move starting ptr down, end ptr is popped */
	*start = (*start)->next;

	return (flag);
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

	return (is_pal(&start, end));
}
