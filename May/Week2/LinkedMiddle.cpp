/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* temp;
        for(temp=head;temp->next!=NULL&&temp->next->next!=NULL;temp=temp->next->next,head=head->next);
        if(temp->next==NULL)
            return head;
        return head->next;
    }
};
