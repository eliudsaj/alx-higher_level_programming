#include "lists.h"

/**
 * check_cycle - checks if a linked list is circular
 * @list: linked list to check
 * Return: Circle(1) or Not(0)
 */
int check_cycle(listint_t *list)
{
	listint_t *runner = list;
	listint_t *slow = list;

	if (!list)
		return (0);
	while (slow && runner && runner->next)
	{
		slow = slow->next;
		runner = runner->next->next;
		if (slow == runner)
			return (1);
	}
	return (0);
}
