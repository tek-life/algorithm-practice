# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        #Find the last head.
        _1st=head
        _2nd=head
        while _2nd!=None:
            _1st=_1st.next
            if _2nd.next!=None:
                _2nd=_2nd.next.next
            else:
                break
        #Reverse the bottom half.
        bottom=ListNode(None)
        nex=_1st
        while nex!=None:
            nex_temp=nex.next
            nex.next=bottom.next
            bottom.next=nex
            nex=nex_temp
        #
        _2nd=bottom.next
        _1st=head
        mark=_2nd
        while _2nd!=None:
            _1st_tmp=_1st.next
            if _1st_tmp == mark:
                _1st.next=None
                _1st_tmp=None
                
            _2nd_tmp=_2nd.next
            _2nd.next=_1st.next
            _1st.next=_2nd
            _2nd=_2nd_tmp
            _1st=_1st_tmp
        if _1st !=None:
            _1st.next=None
