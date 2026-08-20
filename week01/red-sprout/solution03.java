import java.util.*;

class Solution {
    int maxSize;
    Map<String, Integer> cache;

    String getOld() {
        int val = 1_000_000_007;
        String old = "";

        for(String key : cache.keySet()) {
            if(val > cache.get(key)) {
                val = cache.get(key);
                old = key;
            }
        }

        return old;
    }

    int update(String city, int idx) {
        if(maxSize == 0) return 5;
        String key = city.toLowerCase();
        int t = cache.containsKey(key) ? 1 : 5;

        if(cache.containsKey(key)
           || cache.size() < maxSize) {
            cache.put(key, idx);
        } else {
            cache.remove(getOld());
            cache.put(key, idx);
        }

        return t;
    }

    public int solution(int cacheSize, String[] cities) {
        int t = 0;
        int l = cities.length;
        maxSize = cacheSize;
        cache = new HashMap<>();

        for(int i = 0; i < l; ++i) {
            t += update(cities[i], i);
        }

        return t;
    }
}
