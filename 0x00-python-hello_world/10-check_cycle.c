#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * Return: 0 if no cycle, 1 is yes
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp_fast = NULL;
	listint_t *fast = NULL;
	listint_t *slow = NULL;

	if (!list)
		return (0);

	tmp_fast = list;
	fast = list;
	slow = list;

	while (1) /* if match is found, cycle is found */
	{
		tmp_fast = fast;
		if (tmp_fast->next->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;

			if (fast->n == slow->n)
				return (1);
		}
		else
			return (0);
	}

}
