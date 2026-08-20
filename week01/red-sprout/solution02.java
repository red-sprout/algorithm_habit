import java.util.*;

class Solution {
    int zeros;

    String binary(int num) {
        String s = "";
        while(num > 0) {
            s = (num & 1) + s;
            num = num >> 1;
        }
        return s;
    }

    String convert(String s) {
        int l = s.length();
        int cnt = 0;
        for(int i = 0; i < l; ++i) {
            char c = s.charAt(i);
            if(c == '1') {
                ++cnt;
            } else {
                ++zeros;
            }
        }
        return binary(cnt);
    }

    int[] loop(String s) {
        int cnt = 0;
        while(!s.equals("1")) {
            s = convert(s);
            ++cnt;
        }
        return new int[] {cnt, zeros};
    }

    public int[] solution(String s) {
        zeros = 0;
        return loop(s);
    }
}
