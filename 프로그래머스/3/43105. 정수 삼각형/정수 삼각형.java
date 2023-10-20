class Solution {
    public int solution(int[][] triangle) {
        int[][] dp = new int[triangle.length][triangle.length];
        
        for (int i = 0; i < triangle.length; i++){
            int[] temp = new int[i+1];
            for (int j = 0; j < i+1; j++){
                int left = i >0 && j > 0 ? dp[i-1][j-1] : 0;
                int right = i > 0 && j < i ? dp[i-1][j] : 0;
                temp[j] = Math.max(left,right) + triangle[i][j];
            }
            dp[i]= temp;
        }
        
        int answer = 0;
        for (int i : dp[dp.length-1]) {
            answer = Math.max(answer, i);
        }
        return answer;
    }
}