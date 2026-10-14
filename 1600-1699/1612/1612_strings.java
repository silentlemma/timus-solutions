import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StringBuilder text = new StringBuilder();
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        for (int c; (c = in.read()) != -1;)
            text.append((char)c);
        int trams = 0, trolleys = 0;
        // a word is a run of letters; anything else ends it
        for (String word : text.toString().split("[^a-z]+")) {
            if (word.equals("tram"))
                trams++;
            else if (word.equals("trolleybus"))
                trolleys++;
        }
        if (trams > trolleys)
            System.out.println("Tram driver");
        else if (trolleys > trams)
            System.out.println("Trolleybus driver");
        else
            System.out.println("Bus driver");
    }
}
