/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
      Map<Integer, Integer> dict = new HashMap<>();
      boolean result = false;
      ListNode curr = head;
      int index = 0;
      while (curr!= null && result == false) {
        if (dict.containsKey(curr.val)) {
            dict.get(curr.val);
            result = true;
        }
        dict.put(curr.val,index);
        curr = curr.next;
        index++;
      }
      return result;
    }
}
