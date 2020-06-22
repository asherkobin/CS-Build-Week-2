class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1str = ""
        num2str = ""
        
        cur = l1
        
        while cur != None:
            num1str += str(cur.val)
            cur = cur.next
        
        cur = l2
        
        while cur != None:
            num2str += str(cur.val)
            cur = cur.next
            
        print(num1str)
        print(num2str)
        
        num1 = int(num1str[::-1])
        num2 = int(num2str[::-1])
        
        print(num1)
        print(num2)
        
        sum = str(num1 + num2)
        
        print(sum)
        sum_str = str(sum)
        sum_str = sum_str[::-1]
        
        head = None
        cur = None
        
        for digit in sum_str:
            if head is None:
                head = ListNode(int(digit))
                cur = head
            else:
                cur.next = ListNode(int(digit))
                cur = cur.next
                
        return head