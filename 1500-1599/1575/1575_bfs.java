import java.io.*;
import java.util.*;

public class Main {
    // the lines of the map in the order of their stations; the circle line
    // closes on itself
    static final String[] LINES = {
        "Pobedy I_Pyatiletki_square Zvezda Uralskaya Shevchenko Teatralnaya Kuybyshevskaya "
            + "Oborony_square Mayakovskaya Parkovaya Botanicheskaya Samolyotnaya Vtorchermet "
            + "Keramicheskaya",
        "Bakinskih_Komissarov Prospekt_Kosmonavtov Uralmash Mashinostroiteley Uralskaya Dinamo "
            + "1905_year_square Geologicheskaya Bazhovskaya Chkalovskaya Botanicheskaya "
            + "Shcherbakovskaya Uktusskie_Gory Nizhne_Isetskaya Himmash",
        "Taganskaya Elmash Turbinnaya Pionerskaya Shevchenko 1905_year_square Moskovskaya "
            + "Central_stadium Kraulya Metallurgov MEGA",
        "7_klyuchey Sortirovochnaya China_town Zarechny City 1905_year_square Kuybyshevskaya "
            + "Sibirskaya Siniye_kamni Lechebnaya Varshavskaya Kompressornaya Koltsovo",
        "Kalinovskaya Italyanskaya Ozyornaya Shefskaya Komsomolskaya Gagarinskaya Teatralnaya "
            + "Geologicheskaya Posadskaya Volgogradskaya Yugo_zapadnaya Akademicheskaya",
        "Zelyony_ostrov Tatishchevskaya Verh_Isetskaya Kommunarov_square 1905_year_square "
            + "Teatralnaya Vostochnaya Vtuzgorodok Kamennye_palatki University",
        "Vilonovskaya Gagarinskaya Vostochnaya Kuybyshevskaya Geologicheskaya Dvorets_sporta "
            + "Aviatsionnaya Voennaya Sovhoznaya",
    };
    static final String CIRCLE =
        "Uralskaya Pionerskaya Gagarinskaya Vtuzgorodok Sibirskaya Oborony_square Bazhovskaya "
        + "Dvorets_sporta Posadskaya Moskovskaya Kommunarov_square City";

    static Map<String, List<String>> adj = new HashMap<>();

    static void join(String a, String b) {
        adj.computeIfAbsent(a, k -> new ArrayList<>()).add(b);
        adj.computeIfAbsent(b, k -> new ArrayList<>()).add(a);
    }

    public static void main(String[] args) throws IOException {
        for (String line : LINES) {
            String[] stops = line.split(" ");
            for (int i = 0; i + 1 < stops.length; i++)
                join(stops[i], stops[i + 1]);
        }
        String[] ring = CIRCLE.split(" ");
        for (int i = 0; i < ring.length; i++)
            join(ring[i], ring[(i + 1) % ring.length]);
        // every run between neighbouring stations takes a minute and changes are
        // free, so the answer is the number of runs on a shortest path
        Map<String, Map<String, Integer>> dist = new HashMap<>();
        for (String start : adj.keySet()) {
            Map<String, Integer> seen = new HashMap<>();
            seen.put(start, 0);
            ArrayDeque<String> queue = new ArrayDeque<>();
            queue.add(start);
            while (!queue.isEmpty()) {
                String v = queue.poll();
                for (String u : adj.get(v))
                    if (!seen.containsKey(u)) {
                        seen.put(u, seen.get(v) + 1);
                        queue.add(u);
                    }
            }
            dist.put(start, seen);
        }
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null)
            all.append(line).append(' ');
        StringTokenizer words = new StringTokenizer(all.toString());
        int n = Integer.parseInt(words.nextToken());
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            String a = words.nextToken(), b = words.nextToken();
            out.append(dist.get(a).get(b)).append('\n');
        }
        System.out.print(out);
    }
}
