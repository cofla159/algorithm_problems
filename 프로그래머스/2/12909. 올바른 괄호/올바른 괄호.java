import java.util.*;

class Solution {
    boolean solution(String s) {
        if (s.length() == 0) return false;
        
        ArrayList<Character> stack = new ArrayList();
        for(char c:s.toCharArray()){
            if(!stack.isEmpty() && stack.get(stack.size()-1) == '(' && c == ')') stack.remove(stack.size()-1);
            else stack.add(c);
        }

        return stack.size() == 0;
    }
}