# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKList(self, lists):
        if lists == []:
            return ListNode("")

        # base case
        if len(lists) == 1:
            return lists[0]

        # recursive case
        else:
            n = len(lists) // 2
            left = self.mergeKLists(lists[:n])
            right = self.mergeKLists(lists[n:])
            result = self.merge([left, right])

            return result

    def merge(self, lists):
        ans = []
        while lists != [None, None]:
            if lists[0] == None:
                ans.append(lists[1].val)
                if lists[1].val != None:
                    lists[1] = lists[1].next
            elif lists[1] == None:
                ans.append(lists[0].val)
                if lists[0].val != None:
                    lists[0] = lists[0].next
            elif lists[0].val <= lists[1].val:
                ans.append(lists[0].val)
                if lists[0].val != None:
                    lists[0] = lists[0].next
            else:
                ans.append(lists[1].val)
                if lists[1].val != None:
                    lists[1] = lists[1].next

        if ans == []:
            return None

        last_val = None
        result = ListNode()
        for i in ans[::-1]:
            result.val = i
            result.next = last_val
            last_val = ListNode(i, last_val)

        return result

    def mergeKLists2(self, lists):
        """
        O(n^2)
        """

        idx = None
        ans = []
        count = 0

        while lists != [None] * len(lists):
            count += 1
            min_val = float("inf")
            for i in range(len(lists)):
                if lists[i] == None:
                    continue
                elif lists[i].val < min_val:
                    min_val = lists[i].val
                    idx = i

            ans.append(min_val)
            if lists[idx] != None:
                lists[idx] = lists[idx].next

        if ans == []:
            return ListNode("", None)

        # result
        return_ans = ListNode()
        next_val = None
        for i in ans[::-1]:
            return_ans.val = i
            return_ans.next = next_val
            next_val = ListNode(i, next_val)

        return return_ans


if __name__ == "__main__":
    # lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    # print(Solution().mergeKLists(lists))
    print(5 or None)
