import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Main {
    static final double RADIUS = 6875.0 / 2, DANGER = 100, MINUTES = 60, SECONDS = 3600;
    static final double HUNDREDTHS = 100;
    static final int PARTS = 3, BUFFER = 1 << 12;

    static String readAll(InputStream in) throws IOException {
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        byte[] buffer = new byte[BUFFER];
        for (int n; (n = in.read(buffer)) > 0;) {
            bytes.write(buffer, 0, n);
        }
        return bytes.toString("ISO-8859-1");
    }

    public static void main(String[] args) throws IOException {
        String text = readAll(System.in).replace('^', ' ').replace('\'', ' ').replace('"', ' ');
        String[] tokens = text.trim().split("\\s+");
        // every coordinate is "degrees minutes seconds" followed by NL, SL, EL or WL
        List<Double> angle = new ArrayList<>();
        for (int i = PARTS; i < tokens.length; i++) {
            String t = tokens[i];
            if (t.length() < 2 || t.charAt(1) != 'L' || "NSEW".indexOf(t.charAt(0)) < 0) {
                continue;
            }
            double degrees = Double.parseDouble(tokens[i - PARTS]) +
                             Double.parseDouble(tokens[i - 2]) / MINUTES +
                             Double.parseDouble(tokens[i - 1]) / SECONDS;
            boolean negative = t.charAt(0) == 'S' || t.charAt(0) == 'W';
            angle.add(Math.toRadians(negative ? -degrees : degrees));
        }
        double lat1 = angle.get(0), lon1 = angle.get(1), lat2 = angle.get(2);
        double lon2 = angle.get(angle.size() - 1);
        // the haversine formula keeps its precision for small distances
        double h = Math.pow(Math.sin((lat2 - lat1) / 2), 2) +
                   Math.cos(lat1) * Math.cos(lat2) * Math.pow(Math.sin((lon2 - lon1) / 2), 2);
        double distance = 2 * RADIUS * Math.asin(Math.min(1, Math.sqrt(h)));
        StringBuilder out = new StringBuilder();
        out.append(
            String.format(Locale.US, "The distance to the iceberg: %.2f miles.\n", distance));
        // the comparison uses the printed value: 99.996 is printed as 100.00
        if (Math.round(distance * HUNDREDTHS) < DANGER * HUNDREDTHS) {
            out.append("DANGER!\n");
        }
        System.out.print(out);
    }
}
