#include "lists.h"

/**
 * is_pal - matches and returns if palindrome
 * @head: ptr to head of list
 * @reversed: ptr to head of reversed list
 * Return: 0 if not, 1 if yes
 */
int is_pal(listint_t **head, listint_t *reversed)
{
	while (reversed != NULL)
	{
		if (reversed->n != (*head)->n)
			return (0);
		reversed = reversed->next;
		*head = (*head)->next;
	}
	return (1);
}

/**
 * reverse - reverses linked list starting at ptr given
 * @midway_head: ptr to the middle of the linked list
 * Return: return head of reversed list (tail of original list)
 */
listint_t *reverse(listint_t **midway_head)
{
	listint_t *prev = NULL;
	listint_t *curr = *midway_head;
	listint_t *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (prev);
}

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int result = 1;
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *mid = NULL;
	listint_t *reversed = NULL;

	if (head == NULL) /* non-existing list is not */
		return (0);
	if (*head == NULL) /* empty list is palindrome */
		return (1);

	if ((*head)->next == NULL) /* one node list returns true */
		return (result);
	else
	{
		while (fast != NULL && fast->next != NULL) /*find midpoint */
		{
			slow = slow->next;
			fast = fast->next->next;
		}
		if (fast != NULL)
			slow = slow->next;
		mid = slow;

		reversed = reverse(&mid); /* reverse midpt to compare */
		result = is_pal(head, reversed);

		return (result);
	}
}
