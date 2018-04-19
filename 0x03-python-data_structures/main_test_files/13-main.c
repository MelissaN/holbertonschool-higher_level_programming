#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 1);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	print_listint(head);
	free_listint(head);

	head = NULL;
	add_nodeint_end(&head, 1);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);

	head = NULL;
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 500000);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 1);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 2);
	add_nodeint_end(&head, 3);
	add_nodeint_end(&head, 2);
	add_nodeint_end(&head, 1);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 2);
	add_nodeint_end(&head, 2);
	add_nodeint_end(&head, 1);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 500000);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	free_listint(head);

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 500);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 1);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");
	print_listint(head);
	free_listint(head);

	return (0);
}
