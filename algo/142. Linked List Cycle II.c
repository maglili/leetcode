/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head)
{
    // L1 = head to entry point
    // L2 = entry point to meeting point
    // x = meeting point to entry point
    // The distance of slow pointer walk to meeting point:
    //      L1 + L2
    // The distance of fast pointer walk to meeting point:
    //      L1 + L2 + x + L2
    // Solve the formula:
    //      2(L1 + L2) = L1 + L2 + x + L2
    //              L1 = x
    //  key point: (head to entry point) == (meeting point to entry point)
    if (head == NULL)
    {
        return NULL;
    }

    struct ListNode *p1 = head;
    struct ListNode *p2 = head;

    while (p2->next != NULL && p2->next->next != NULL)
    {
        p1 = p1->next;
        p2 = p2->next->next;

        // 2 point meet each other
        if (p1 == p2)
        {
            while (head != p1)
            {
                head = head->next;
                p1 = p1->next;
            }
            return p1;
        }
    }

    return NULL;
}