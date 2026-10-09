import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main {
    static class Folder {
        // the tree map keeps the subfolders sorted by name
        final TreeMap<String, Folder> sub = new TreeMap<>();
    }

    static void print(Folder f, int depth, StringBuilder out) {
        for (Map.Entry<String, Folder> e : f.sub.entrySet()) {
            for (int i = 0; i < depth; i++) {
                out.append(' ');
            }
            out.append(e.getKey()).append('\n');
            print(e.getValue(), depth + 1, out);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            text.append(line).append('\n');
        }
        StringTokenizer tok = new StringTokenizer(text.toString());
        int n = Integer.parseInt(tok.nextToken());
        Folder root = new Folder();
        for (int i = 0; i < n; i++) {
            Folder cur = root;
            for (String name : tok.nextToken().split("\\\\")) {
                Folder next = cur.sub.get(name);
                if (next == null) {
                    next = new Folder();
                    cur.sub.put(name, next);
                }
                cur = next;
            }
        }
        StringBuilder out = new StringBuilder();
        print(root, 0, out);
        System.out.print(out);
    }
}
