class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = []

        curr = head
        while curr:
            ans.append(curr.val)
            curr = curr.next

        return ans == ans[::-1]