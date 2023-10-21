import java.util.*;

class Solution {
    ArrayList<Integer> queue = new ArrayList();
    
    void insert(int num){
        int idx = 0;
        for (int el:queue){
            if (el > num) break;
            idx++;
        }
        if (idx >= queue.size()){
            queue.add(num);
        }else{
            queue.add(idx, num);
        }
    }
    
    void delMin(){
        if (queue.size() > 0) queue.remove(0);
    }
    
    void delMax(){
        if (queue.size() > 0) queue.remove(queue.size()-1);
    }
    
    public int[] solution(String[] operations) {
        int[] answer = {};
        for (String op:operations){
            if (op.charAt(0) == 'I'){
                insert(Integer.parseInt(op.split(" ")[1]));
            }else if (op.split(" ")[1].equals("1")){
                delMax();
            }else{
                delMin();
            }
        }
        return queue.size()>0 ? new int[]{queue.get(queue.size()-1), queue.get(0)} : new int[]{0,0};
    }
}