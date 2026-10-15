import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Locale;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer head = new StringTokenizer(in.readLine());
        head.nextToken();
        int n = Integer.parseInt(head.nextToken());
        int q = Integer.parseInt(head.nextToken());
        Set<String> taken = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String team = in.readLine().trim();
            // the university is everything before " #k"; names differing only
            // in letter case are the same university
            int hash = team.lastIndexOf('#');
            String university = hash >= 0 ? team.substring(0, hash).trim() : team;
            university = university.toLowerCase(Locale.ROOT);
            if (taken.contains(university)) {
                continue;
            }
            if (taken.size() == q) {
                System.out.println(team);
                return;
            }
            taken.add(university);
        }
    }
}
