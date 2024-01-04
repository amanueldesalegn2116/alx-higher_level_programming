#include "lists.h"
/**
 * insert_node - Inserts a node with a given number into a sorted linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The value to be inserted into the linked list.
 *
 * Return: A pointer to the newly inserted node, or NULL on failure.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	/* Allocate memory for the new node. */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	return (NULL);

	/* Set the value of the new node. */
	new->n = number;

	/* If the list is empty or the first node has a greater value, insert at the beginning. */
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	/* Traverse the list to find the correct position for the new node. */
	while (node && node->next && node->next->n < number)
	node = node->next;

	/* Insert the new node into the sorted position. */
	new->next = node->next;
	node->next = new;

return (new);
}
