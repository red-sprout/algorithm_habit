import java.util.*;

class Solution {
    int n;
    boolean[][] pillar;
    boolean[][] beam;

    int[] dx = {-1, 0, 1, 0, -1, 1, -1, 1, 0};
    int[] dy = {0, -1, 0, 1, 1, -1, -1, 1, 0};

    void init(int n) {
        this.n = n;
        this.pillar = new boolean[n + 1][n + 1];
        this.beam = new boolean[n + 1][n + 1];
    }

    boolean pillarCheck(int x, int y) {
        return y == 0
            || beam[x][y]
            || (x > 0 && beam[x - 1][y])
            || (y > 0 && pillar[x][y - 1]);
    }

    boolean beamCheck(int x, int y) {
        return (y > 0 && pillar[x][y - 1])
            || (x < n && y > 0 && pillar[x + 1][y - 1])
            || ((x > 0 && beam[x - 1][y]) && (x < n && beam[x + 1][y]));
    }

    void create(int x, int y, int a) {
        if(a == 0) {
            if(pillarCheck(x, y)) {
                pillar[x][y] = true;
            }
        } else {
            if(beamCheck(x, y)) {
                beam[x][y] = true;
            }
        }
    }

    void delete(int x, int y, int a) {
        if(a == 0) {
            if(!pillar[x][y]) return;

            boolean flag = false;
            pillar[x][y] = false;

            for(int i = 0; i < 9; ++i) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(0 <= nx && nx <= n && 0 <= ny && ny <= n) {
                    if(pillar[nx][ny] && !pillarCheck(nx, ny)) {
                        flag = true;
                        break;
                    }

                    if(beam[nx][ny] && !beamCheck(nx, ny)) {
                        flag = true;
                        break;
                    }
                }
            }

            pillar[x][y] = flag;
        } else {
            if(!beam[x][y]) return;

            boolean flag = false;
            beam[x][y] = false;

            for(int i = 0; i < 9; ++i) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(0 <= nx && nx <= n && 0 <= ny && ny <= n) {
                    if(pillar[nx][ny] && !pillarCheck(nx, ny)) {
                        flag = true;
                        break;
                    }

                    if(beam[nx][ny] && !beamCheck(nx, ny)) {
                        flag = true;
                        break;
                    }
                }
            }

            beam[x][y] = flag;
        }
    }

    int[][] getStructure() {
        List<int[]> list = new ArrayList<>();

        for(int i = 0; i < n + 1; ++i) {
            for(int j = 0; j < n + 1; ++j) {
                if(pillar[i][j]) {
                    list.add(new int[] {i, j, 0});
                }
                if(beam[i][j]) {
                    list.add(new int[] {i, j, 1});
                }
            }
        }

        int l = list.size();
        int[][] answer = new int[l][];

        for(int i = 0; i < l; ++i) {
            answer[i] = list.get(i);
        }

        return answer;
    }

    public int[][] solution(int n, int[][] build_frame) {
        init(n);

        for(int[] build : build_frame) {
            if(build[3] == 1) {
                create(build[0], build[1], build[2]);
            } else {
                delete(build[0], build[1], build[2]);
            }
        }

        return getStructure();
    }
}
