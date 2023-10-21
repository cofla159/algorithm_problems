import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[] visited = new int[n];
        
        for (int i = 0; i < computers.length; i++){
                if (visited[i] == 0){
                    answer += 1;
                    ArrayList<List<Integer>> willVisit = new ArrayList();
                    willVisit.add(List.of(i,i));
                    visited[i] = 1;
                    
                    while (willVisit.size() > 0){
                        List<Integer> now = willVisit.remove(0);
                        int x = now.get(0);
                        int y = now.get(1);
                       
                        for (int j = 0; j < computers.length; j++){
                            if (computers[x][j] == 1 && visited[j] == 0){
                                willVisit.add(List.of(x,j));
                                visited[j] = 1;
                            }else if (computers[y][j] == 1 && visited[j] == 0){
                                willVisit.add(List.of(y,j));
                                visited[j] = 1;
                            }
                        }
                    }
                }
        }
        return answer;
    }
}