# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add(self,temp,arr):
        while len(arr)!=0:
            node=ListNode(arr[0])
            arr=arr[1:]
            temp.next=node
            temp=temp.next
        return temp
    
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd,even,cnt=[],[],1
        while head!=None:
            if cnt%2==0:
                even.append(head.val)
            else:
                odd.append(head.val)
            cnt+=1
            head=head.next
        if len(even)==0 and len(odd)==0:
            return head
        elif len(even)==0:
            return ListNode(odd[0])
        elif len(odd)==0:
            return ListNode(even[0])
        temp = ListNode(odd[0])
        glob=temp
        odd=odd[1:]
        temp=self.add(temp,odd)
        temp=self.add(temp,even)
        return glob
