import java.io.*;
import java.util.*;

public class Main {
    // a max tree over cities: the best total, how many leaves reach it, and
    // one of them
    static int size = 1;
    static long[] best;
    static int[] count, where;

    static void add(int city, long amount) {
        int i = city + size;
        best[i] += amount;
        for (i /= 2; i > 0; i /= 2) {
            int a = 2 * i, b = 2 * i + 1;
            if (best[a] != best[b]) {
                int w = best[a] > best[b] ? a : b;
                best[i] = best[w];
                count[i] = count[w];
                where[i] = where[w];
            } else {
                best[i] = best[a];
                count[i] = count[a] + count[b];
                where[i] = where[a];
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null)
            text.append(line).append(' ');
        StringTokenizer in = new StringTokenizer(text.toString());
        int n = Integer.parseInt(in.nextToken());
        String[] name = new String[n], city = new String[n];
        long[] money = new long[n];
        for (int i = 0; i < n; i++) {
            name[i] = in.nextToken();
            city[i] = in.nextToken();
            money[i] = Long.parseLong(in.nextToken());
        }
        int m = Integer.parseInt(in.nextToken()), k = Integer.parseInt(in.nextToken());
        int[] day = new int[k];
        String[] who = new String[k], to = new String[k];
        for (int i = 0; i < k; i++) {
            day[i] = Integer.parseInt(in.nextToken());
            who[i] = in.nextToken();
            to[i] = in.nextToken();
        }
        Map<String, Integer> cityId = new HashMap<>();
        List<String> cityName = new ArrayList<>();
        for (String[] group : new String[][] {city, to})
            for (String c : group)
                if (!cityId.containsKey(c)) {
                    cityId.put(c, cityName.size());
                    cityName.add(c);
                }
        while (size < cityName.size())
            size *= 2;
        best = new long[2 * size];
        count = new int[2 * size];
        where = new int[2 * size];
        for (int c = 0; c < size; c++) {
            count[size + c] = 1;
            where[size + c] = c;
        }
        for (int i = size - 1; i > 0; i--) {
            count[i] = count[2 * i] + count[2 * i + 1];
            where[i] = where[2 * i];
        }
        Map<String, Integer> home = new HashMap<>();
        Map<String, Long> wealth = new HashMap<>();
        for (int i = 0; i < n; i++) {
            home.put(name[i], cityId.get(city[i]));
            wealth.put(name[i], money[i]);
            add(cityId.get(city[i]), money[i]);
        }
        long[] days = new long[cityName.size()];
        int today = 1;
        for (int i = 0; i <= k; i++) {
            // the moves of a day count from the next morning
            int until = i < k ? day[i] + 1 : m + 1;
            if (until > today && count[1] == 1) // a strict leader only
                days[where[1]] += until - today;
            today = Math.max(today, until);
            if (i == k)
                break;
            long w = wealth.get(who[i]);
            add(home.get(who[i]), -w);
            home.put(who[i], cityId.get(to[i]));
            add(cityId.get(to[i]), w);
        }
        TreeMap<String, Long> answer = new TreeMap<>();
        for (int c = 0; c < cityName.size(); c++)
            if (days[c] > 0)
                answer.put(cityName.get(c), days[c]);
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Long> e : answer.entrySet())
            sb.append(e.getKey()).append(' ').append(e.getValue()).append('\n');
        System.out.print(sb);
    }
}
