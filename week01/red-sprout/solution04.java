import java.util.*;

class Solution {
    int m, n;
    char[][] board;

    void init(int m, int n, String[] sArr) {
        this.m = m;
        this.n = n;
        this.board = new char[m][n];

        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < n; ++j) {
                this.board[i][j] = sArr[i].charAt(j);
            }
        }
    }

    int erase() {
        boolean[][] visited = new boolean[m][n];
        for(int i = 0; i < m - 1; ++i) {
            for(int j = 0; j < n - 1; ++j) {
                char c = board[i][j];
                if(c == '.') continue;
                if(c == board[i + 1][j]
                  && c == board[i][j + 1]
                  && c == board[i + 1][j + 1]) {
                    visited[i][j] = true;
                    visited[i + 1][j] = true;
                    visited[i][j + 1] = true;
                    visited[i + 1][j + 1] = true;
                }
            }
        }

        int cnt = 0;
        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < n; ++j) {
                if(visited[i][j]) {
                    ++cnt;
                    board[i][j] = '.';
                }
            }
        }

        return cnt;
    }

    void fall() {
        Queue<Character>[] queues = new Queue[n];
        for(int j = 0; j < n; ++j) {
            queues[j] = new ArrayDeque<>();
        }

        for(int i = m - 1; i >= 0; --i) {
            for(int j = 0; j < n; ++j) {
                if(board[i][j] != '.') queues[j].offer(board[i][j]);
            }
        }

        for(int i = m - 1; i >= 0; --i) {
            for(int j = 0; j < n; ++j) {
                if(!queues[j].isEmpty()) {
                    board[i][j] = queues[j].poll();
                } else {
                    board[i][j] = '.';
                }
            }
        }
    }

    public int solution(int m, int n, String[] board) {
        init(m, n, board);
        int answer = 0;
        while(true) {
            int cnt = erase();
            if(cnt == 0) break;
            answer += cnt;
            fall();
        }
        return answer;
    }
}
