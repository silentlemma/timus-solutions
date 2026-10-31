import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static final BufferedReader INPUT = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer words = new StringTokenizer("");
    static final Map<String, Integer> IDS = new HashMap<>();
    static final ArrayList<String> NAMES = new ArrayList<>();
    static final ArrayList<Long> TOTALS = new ArrayList<>();
    static long[] best;
    static int[] where;
    static int size = 1;
    static class Person {
        int city;
        long wealth;
        Person(int c, long w) {
            city = c;
            wealth = w;
        }
    }
    static String next() throws IOException {
        while (!words.hasMoreTokens())
            words = new StringTokenizer(INPUT.readLine());
        return words.nextToken();
    }
    static int cityId(String city) {
        Integer found = IDS.get(city);
        if (found != null)
            return found;
        int id = NAMES.size();
        IDS.put(city, id);
        NAMES.add(city);
        TOTALS.add(0L);
        return id;
    }
    // a max tree over cities: the best total and the one city that reaches it,
    // or minus one when several cities do
    static void pull(int i) {
        int a = 2 * i, b = a + 1;
        best[i] = Math.max(best[a], best[b]);
        // minus one denotes a tie, replacing a full multiplicity array.
        where[i] = best[a] == best[b] ? -1 : where[best[a] > best[b] ? a : b];
    }
    static void add(int city, long amount) {
        int i = size + city;
        best[i] += amount;
        for (i /= 2; i > 0; i /= 2) {
            long value = best[i];
            int winner = where[i];
            pull(i);
            // unchanged maxima and tie status cannot affect an ancestor.
            if (value == best[i] && winner == where[i])
                break;
        }
    }
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(next());
        Map<String, Person> people = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            String who = next();
            int city = cityId(next());
            long wealth = Long.parseLong(next());
            people.put(who, new Person(city, wealth));
            TOTALS.set(city, TOTALS.get(city) + wealth);
        }
        int m = Integer.parseInt(next()), k = Integer.parseInt(next());
        // each move introduces at most one city; no move records need to be stored.
        while (size < NAMES.size() + k)
            size *= 2;
        best = new long[2 * size];
        where = new int[2 * size];
        int[] days = new int[size];
        for (int i = 0; i < size; ++i)
            where[size + i] = i;
        for (int i = 0; i < TOTALS.size(); ++i)
            best[size + i] = TOTALS.get(i);
        TOTALS.clear();
        for (int i = size - 1; i > 0; --i)
            pull(i);
        int today = 1;
        for (int i = 0; i < k; ++i) {
            int day = Integer.parseInt(next());
            Person person = people.get(next());
            int to = cityId(next());
            // a strict leader only; the moves of a day count from the next morning
            if (where[1] >= 0)
                days[where[1]] += day + 1 - today;
            today = day + 1;
            if (person.city != to) {
                add(person.city, -person.wealth);
                add(to, person.wealth);
                person.city = to;
            }
        }
        if (where[1] >= 0)
            days[where[1]] += m + 1 - today;
        Collections.sort(NAMES);
        StringBuilder out = new StringBuilder();
        for (String name : NAMES) {
            int d = days[IDS.get(name)];
            if (d > 0)
                out.append(name).append(' ').append(d).append('\n');
        }
        System.out.print(out);
    }
}
