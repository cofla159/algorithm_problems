#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#define min(a,b)  (((a) > (b)) ? (b) : (a))
#define max(a,b)  (((a) > (b)) ? (a) : (b))

int dfs(int cur, int n, int* visited, int** graph, int count){
    visited[cur] = 1;
    for (int i = 0; i < n; i++){
        if (graph[cur][i] && !visited[i]){
             int result = dfs(i, n, visited, graph, count+1);
             count = max(count, result);
        }
    }
    return count;
}

// wires_rows는 2차원 배열 wires의 행 길이, wires_cols는 2차원 배열 wires의 열 길이입니다.
int solution(int n, int** wires, size_t wires_rows, size_t wires_cols) {
    int answer = n-2;
    int **graph = (int**) calloc (n,sizeof(int*) );
    for(int i=0; i<n; i++){
        graph[i] = (int*) calloc (n, sizeof(int) );
    }
    for (int i = 0; i < wires_rows; i++){
        graph[wires[i][0]-1][wires[i][1]-1] = 1;
        graph[wires[i][1]-1][wires[i][0]-1] = 1;
    }

    for (int i = 0; i < wires_rows; i++){
        graph[wires[i][0]-1][wires[i][1]-1] = 0;
        graph[wires[i][1]-1][wires[i][0]-1] = 0;
        
        int* visited = (int*) calloc (n, sizeof(int));
        int con_num = dfs(0, n, visited, graph, 1);        
        answer = min(answer, abs(con_num-(n-con_num)));

        graph[wires[i][0]-1][wires[i][1]-1] = 1;
        graph[wires[i][1]-1][wires[i][0]-1] = 1;
    }

    for (int i = 0; i < n; i++) {
      free(graph[i]);
    }
    free(graph);
    
    return answer;
}