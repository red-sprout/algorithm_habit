import java.util.*;

class Solution {
    int findIdx(int n, String[] words) {
        int l = words.length;
        Set<String> set = new HashSet<>();
        String last = "";
        for(int i = 0; i < l; ++i) {
            if(set.contains(words[i])) {
                return i;
            }

            if(!last.equals("")
               && last.charAt(last.length() - 1) != words[i].charAt(0)) {
                return i;
            }

            set.add(words[i]);
            last = words[i];
        }
        return -1;
    }

    int[] convert(int n, int idx) {
        if(idx == -1) {
            return new int[] {0, 0};
        }

        return new int[] {
            idx % n + 1,
            idx / n + 1
        };
    }

    public int[] solution(int n, String[] words) {
        int idx = findIdx(n, words);
        return convert(n, idx);
    }
}
