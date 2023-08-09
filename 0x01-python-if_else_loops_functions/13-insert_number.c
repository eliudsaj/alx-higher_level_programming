#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node into linked list
 * @head: head of the linked list
 * @number: number to inserted
 *
 * Return: pointer to new inserted node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	if (!head)
		return NULL;

	new_node = malloc(sizeof(*new_node));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

        current = *head;
	if (*head == NULL)
		*head = new_node;
	else if (number < current->n)
	{
		new_node->next = current;
		*head = new_node;
	}
	else
	{
		while (current->next)
		{
			if (number > current->next->n)
				current = current->next;
			else
				break;
		}
		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);
}
