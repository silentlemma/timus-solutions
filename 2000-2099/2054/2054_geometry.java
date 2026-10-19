import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
  static final int LONG_MONTH = 31;
  static final int SHORT_MONTH = 30;
  static final int FEBRUARY = 28;
  static final int SOLSTICE_DAY = 171;
  static final int HOURS_PER_DAY = 24;
  static final int HOURS_PER_YEAR = 8760;
  static final int NOON = 12;
  static final int HALF_TURN = 180;
  static final double TILT_DEGREES = 23.439281;

  public static void main(String[] args) throws Exception {
    Locale.setDefault(Locale.US);
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer fields = new StringTokenizer(reader.readLine());
    double radians = Math.PI / HALF_TURN;
    double latitude = Double.parseDouble(fields.nextToken()) * radians;
    int count = Integer.parseInt(fields.nextToken());
    String[] months = {
        "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"};
    int[] lengths = {LONG_MONTH, FEBRUARY, LONG_MONTH, SHORT_MONTH, LONG_MONTH, SHORT_MONTH,
        LONG_MONTH, LONG_MONTH, SHORT_MONTH, LONG_MONTH, SHORT_MONTH, LONG_MONTH};
    double equatorial = Math.cos(latitude) * Math.cos(TILT_DEGREES * radians);
    double transverse = Math.cos(latitude);
    double axial = Math.sin(latitude) * Math.sin(TILT_DEGREES * radians);
    DecimalFormat decimal = new DecimalFormat("0.0000000000", new DecimalFormatSymbols(Locale.US));
    StringBuilder output = new StringBuilder();
    for (int query = 0; query < count; query++) {
      fields = new StringTokenizer(reader.readLine());
      int dayIndex = Integer.parseInt(fields.nextToken()) - 1;
      String month = fields.nextToken();
      int hour = Integer.parseInt(fields.nextToken());
      for (int index = 0; !months[index].equals(month); index++) dayIndex += lengths[index];
      int elapsed = (dayIndex - SOLSTICE_DAY) * HOURS_PER_DAY + hour - NOON;
      double orbit = 2 * Math.PI * elapsed / HOURS_PER_YEAR;
      double spin = orbit + 2 * Math.PI * (hour - NOON) / HOURS_PER_DAY;
      double sine = equatorial * Math.cos(spin) * Math.cos(orbit)
          + transverse * Math.sin(spin) * Math.sin(orbit) + axial * Math.cos(orbit);
      double angle = Math.asin(Math.max(0, Math.min(1, sine))) / radians;
      output.append(decimal.format(angle)).append('\n');
    }
    System.out.print(output);
  }
}
