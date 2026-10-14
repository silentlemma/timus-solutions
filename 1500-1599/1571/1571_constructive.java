import java.util.*;

public class Main {
    static final int SMALL = 2;

    // english, or else the first name of one or two letters that no team
    // speaks: at most 100 teams cannot take all 702 of them
    static String freeLanguage(Set<String> spoken) {
        if (!spoken.contains("english"))
            return "english";
        List<String> names = new ArrayList<>();
        for (char a = 'a'; a <= 'z'; a++)
            names.add(String.valueOf(a));
        for (char a = 'a'; a <= 'z'; a++)
            for (char b = 'a'; b <= 'z'; b++)
                names.add("" + a + b);
        for (String name : names)
            if (!spoken.contains(name))
                return name;
        return "";
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] langs = new String[n];
        for (int i = 0; i < n; i++)
            langs[i] = in.next();
        Set<String> distinct = new HashSet<>(Arrays.asList(langs));
        StringBuilder out = new StringBuilder();
        if (distinct.size() < n) {
            // a third team would overhear two teams of one language
            out.append(n == SMALL ? "0" : "Impossible").append('\n');
        } else if (n == 1) {
            out.append("0\n");
        } else if (n == SMALL) {
            out.append("1\n").append(langs[0]).append('-').append(langs[1]).append('\n');
        } else {
            // a talk through another team's language is overheard, so every talk
            // goes through a language no team speaks
            String hub = freeLanguage(distinct);
            out.append(n).append('\n');
            for (String lang : langs)
                out.append(lang).append('-').append(hub).append('\n');
        }
        System.out.print(out);
    }
}
