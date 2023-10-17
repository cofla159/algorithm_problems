import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList();
        int beforeNum = -1;
        for (int num: arr){
            if (num != beforeNum){
                beforeNum = num;
                answer.add(num);
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}