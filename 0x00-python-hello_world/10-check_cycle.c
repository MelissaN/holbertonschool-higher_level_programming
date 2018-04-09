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

	fast = list;
	slow = list;

	while (1)
	{
		/*traverse through nodes as long as linked list node exists*/
		tmp_fast = fast;
		if (tmp_fast->next != NULL && tmp_fast->next->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;

			if (fast->n == slow->n) /*if nodes match, cycle found*/
				return (1);
		}
		else
			return (0);
	}

}
