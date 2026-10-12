import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

public class Main {
    static final String OPEN = "<friend>", CLOSE = "</friend>", END = "</blog>";
    static final int BUFFER = 1 << 16;

    // the name inside a friend tag, without other tags or spaces
    static String clean(String inside) {
        StringBuilder name = new StringBuilder();
        boolean tag = false;
        for (char c : inside.toCharArray()) {
            if (c == '<')
                tag = true;
            else if (c == '>')
                tag = false;
            else if (!tag)
                name.append(c);
        }
        return name.toString().trim();
    }

    public static void main(String[] args) throws IOException {
        InputStream in = System.in;
        ByteArrayOutputStream raw = new ByteArrayOutputStream();
        byte[] chunk = new byte[BUFFER];
        for (int r = in.read(chunk); r > 0; r = in.read(chunk))
            raw.write(chunk, 0, r);
        String[] lines = raw.toString("ISO-8859-1").split("\n", -1);
        int n = Integer.parseInt(lines[0].trim());
        int pos = 1;
        List<String> names = new ArrayList<>();
        List<TreeSet<String>> friendSets = new ArrayList<>();
        for (int b = 0; b < n; b++) {
            while (lines[pos].trim().isEmpty())
                pos++;
            String name = lines[pos].trim();
            StringBuilder text = new StringBuilder();
            for (pos++;; pos++) {
                text.append(lines[pos]).append('\n');
                if (lines[pos].contains(END))
                    break;
            }
            pos++;
            TreeSet<String> friends = new TreeSet<>();
            String body = text.toString();
            for (int at = body.indexOf(OPEN); at >= 0; at = body.indexOf(OPEN, at)) {
                int stop = body.indexOf(CLOSE, at + OPEN.length());
                String friend = clean(body.substring(at + OPEN.length(), stop));
                if (!friend.isEmpty() && !friend.equals(name))
                    friends.add(friend);
                at = stop + CLOSE.length();
            }
            names.add(name);
            friendSets.add(friends);
        }
        StringBuilder out = new StringBuilder();
        for (int b = 0; b < n; b++) {
            String name = names.get(b);
            TreeSet<String> friends = friendSets.get(b), readers = new TreeSet<>(),
                            both = new TreeSet<>();
            for (int o = 0; o < n; o++) {
                if (o != b && friendSets.get(o).contains(name))
                    readers.add(names.get(o));
            }
            for (String s : friends) {
                if (readers.contains(s))
                    both.add(s);
            }
            if (b > 0)
                out.append('\n');
            out.append(name).append('\n');
            List<TreeSet<String>> groups = new ArrayList<>();
            groups.add(friends);
            groups.add(readers);
            groups.add(both);
            for (int g = 0; g < groups.size(); g++)
                out.append(g + 1)
                    .append(": ")
                    .append(String.join(", ", groups.get(g)))
                    .append('\n');
        }
        System.out.print(out);
    }
}
