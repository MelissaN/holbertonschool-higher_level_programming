#include "lists.h"

/**
 * insert_node - malloc and insert node into sorted singly linked list
 * @head: pointer to head of linked list
 * @number: data for new node
 * Return: address of new node, or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL;
	listint_t *new = NULL;

	if (!head)
		return (NULL);

	/* malloc new node */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	/* if no linked list, insert node as the only member */
	if (*head == NULL)
	{
		*head = new;
		(*head)->next = NULL;
		return (new);
	}
	/* if only one node in linked list, do comparision and insert */
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

	/* if lots of nodes in linked list, do comparision and insert */
	tmp = *head;
	while (tmp->next != NULL)
	{
		/* if new node num is smaller than first node, insert */
		if (new->n < tmp->n)
		{
			new->next = tmp;
			*head = new;
			return (new);
		}
		/* if new node num is the same as an existing node, insert */
		/* compare previous node and next node, insert in between */
		if (((new->n > tmp->n) && (new->n < (tmp->next)->n)) ||
		    (new->n == tmp->n))
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	/* if new node is greatest and never inserted, insert now */
	tmp->next = new;
	return (new);
}
