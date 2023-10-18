import java.util.*;

class Solution {
    HashSet<Integer> primeNum = new HashSet<>();
    
    boolean isPrimeNumber(int num){
        boolean result = true;
        if (num == 0 || num == 1) return false;
        
        for (int i = 2;i <= Math.sqrt(num); i++){
            if (num % i == 0) {
                result = false;
                break;
            }
        }
        return result;
    }
    
    void addPrimeNumber(String now, ArrayList list){
        if (!"".equals(now) && isPrimeNumber(Integer.parseInt(now))){
            primeNum.add(Integer.parseInt(now));
        }
        for (int i = 0; i < list.size(); i++){
            ArrayList list1 = new ArrayList<>(list.subList(0, i));
            ArrayList list2 = new ArrayList<>(list.subList(i+1, list.size()));
            list1.addAll(list2);
            addPrimeNumber(now+list.get(i), list1);
        }
    }
    
    public int solution(String numbers) {
        ArrayList<Character> charNums = new ArrayList();
        for (char c:numbers.toCharArray()){
            charNums.add(c);
        }
        addPrimeNumber("", charNums);
        return primeNum.size();
    }
}