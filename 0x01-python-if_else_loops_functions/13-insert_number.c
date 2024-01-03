#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * insert_node - Inserts a node in a sorted singly linked list
 * @head: Pointer to pointer to the first node in the linked list
 * @number: Integer value for the new node
 *
 * Return: pointer to the new node, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur, *prev, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!head)
	{
		return (NULL);
	}

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	cur = *head;
	while (cur)
	{
		if (cur->n > new->n)
		{
			prev->next = new;
			new->next = cur;
			break;
		}
		prev = cur;
		cur = cur->next;
	}

	return (new);
}
