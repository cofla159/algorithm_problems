import java.util.*;

class Solution {
    HashMap<Integer, ArrayList<Integer>> graph = new HashMap();

    int dfs(int start, int[] discon_wire, boolean[] visited, int count){
        visited[start] = true;
        ArrayList<Integer> nextList = graph.get(start);
        
        for (int next:nextList){
            if (Arrays.equals(discon_wire, new int[]{start, next}) || Arrays.equals(discon_wire,new int[]{next, start})) {
                continue;
            }
            if (!visited[next]){
                count = dfs(next, discon_wire, visited, count+1);
            }
        }
        return count;
    }
    
    public int solution(int n, int[][] wires) {
        int answer = n-2;
        
        for (int i = 0; i <n; i++){
            graph.put(i+1, new ArrayList<Integer>());
        }
        
        for (int[] wire:wires){
            ArrayList list1 = graph.get(wire[0]);
            list1.add(wire[1]);
            ArrayList list2 = graph.get(wire[1]);
            list2.add(wire[0]);
        }
        
        for (int[] wire:wires){
            boolean visited[] = new boolean[n+1];
            int result = dfs(1, wire, visited,1);
            answer = Math.min(answer, Math.abs(result-(n-result)));
        }
        return answer;
    }
}