import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static final String[] NAMES = {"trochee", "iamb", "dactyl", "amphibrach", "anapaest"};
    // syllables in a foot and place of the stressed syllable, from 1
    static final int[] FOOT = {2, 2, 3, 3, 3};
    static final int[] PLACE = {1, 2, 1, 2, 3};

    static List<Boolean> stresses(String line) {
        List<Boolean> out = new ArrayList<>();
        for (String word : line.trim().split("\\s+")) {
            for (String syllable : word.split("-")) {
                if (!syllable.isEmpty()) {
                    out.add(syllable.indexOf('[') >= 0);
                }
            }
        }
        return out;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        List<List<Boolean>> poem = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            poem.add(stresses(in.readLine()));
        }
        for (int m = 0; m < NAMES.length; m++) {
            // the last foot may be cut short, so only the place within a foot
            // matters, and every syllable must agree with it
            boolean fits = true;
            for (List<Boolean> verse : poem) {
                for (int i = 0; i < verse.size(); i++) {
                    if (verse.get(i) != (i % FOOT[m] == PLACE[m] - 1)) {
                        fits = false;
                    }
                }
            }
            if (fits) {
                System.out.println(NAMES[m]);
                return;
            }
        }
        System.out.println("not a poem");
    }
}
