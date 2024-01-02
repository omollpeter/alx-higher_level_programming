#include "lists.h"
#include <unistd.h>
#include <stdio.h>

/**
 * check_cycle - Checks if linked list contains a cycle
 * @list: Pointer to the first node in the linked list
 *
 * Return: 1 if there is cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);

	slow = list;
	fast = list;
	
	while (slow != NULL || fast != NULL)
	{
		if (fast->next == NULL)
			return (0);

		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
