#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * len_list - Computes the length of a linked list
 * @head: Pointer to pointer to the first node in the list
 *
 * Return: Number of nodes in the list
 */
int len_list(listint_t **head)
{
	listint_t *temp;
	int count = 0;

	if (*head == NULL)
		return (count);

	temp = *head;
	while (temp)
	{
		count += 1;
		temp = temp->next;
	}

	return (count);
}

/**
 * is_palindrome - Checks whether a singly linked list is a palindrome
 * @head: Pointer to pointer to the first node in the list
 *
 * Return: 1 if list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len, start, end;

	len = len_list(head);

	if (len == 0)
		return (1);

	start = 0;
	end = len - 1;

	while (start <= end)
	{
		if (get_nodeint_at_index(*head, start) != get_nodeint_at_index(*head, end))
			return (0);
		start++;
		end--;
	}

	return (1);
}

/**
 * get_nodeint_at_index - Retrieves a node at a spec. index in the linked list
 * @head: Pointer to the first node in the linked list
 * @index: Position of the node in the list
 *
 * Return: pointer to the retrieved node, NULL otherwise
 */
int get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *temp;
	unsigned int i = 0;
	int node;

	temp = head;
	while (i < index)
	{
		temp = temp->next;
		i++;
	}

	node = temp->n;
	return (node);
}

