#include "lists.h"
/**
 * check_cycle - Checks if a linked list has a cycle using Floyd's algorithm.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if a cycle is found, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
/* Initialize two pointers, slow and fast, both starting at the head. */
listint_t *slow = list;
listint_t *fast = list;

	/* Check if the linked list is empty. */
	if (!list)
	return (0);

	/* Traverse the linked list using Floyd's algorithm. */
	while (slow && fast && fast->next)
	{
	/* Move slow pointer one step at a time. */
	slow = slow->next;

	/* Move fast pointer two steps at a time. */
	fast = fast->next->next;

	/* If there's a cycle, slow and fast pointers will meet. */
	if (slow == fast)
	return (1);
	}

/* If the loop completes, there is no cycle in the linked list. */
return (0);
}
