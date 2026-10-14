use std::collections::{HashMap, VecDeque};
use std::io::{self, Read};

/// The lines of the map in the order of their stations; the circle line
/// closes on itself.
const LINES: [&str; 7] = [
    "Pobedy I_Pyatiletki_square Zvezda Uralskaya Shevchenko Teatralnaya Kuybyshevskaya \
     Oborony_square Mayakovskaya Parkovaya Botanicheskaya Samolyotnaya Vtorchermet \
     Keramicheskaya",
    "Bakinskih_Komissarov Prospekt_Kosmonavtov Uralmash Mashinostroiteley Uralskaya Dinamo \
     1905_year_square Geologicheskaya Bazhovskaya Chkalovskaya Botanicheskaya \
     Shcherbakovskaya Uktusskie_Gory Nizhne_Isetskaya Himmash",
    "Taganskaya Elmash Turbinnaya Pionerskaya Shevchenko 1905_year_square Moskovskaya \
     Central_stadium Kraulya Metallurgov MEGA",
    "7_klyuchey Sortirovochnaya China_town Zarechny City 1905_year_square Kuybyshevskaya \
     Sibirskaya Siniye_kamni Lechebnaya Varshavskaya Kompressornaya Koltsovo",
    "Kalinovskaya Italyanskaya Ozyornaya Shefskaya Komsomolskaya Gagarinskaya Teatralnaya \
     Geologicheskaya Posadskaya Volgogradskaya Yugo_zapadnaya Akademicheskaya",
    "Zelyony_ostrov Tatishchevskaya Verh_Isetskaya Kommunarov_square 1905_year_square \
     Teatralnaya Vostochnaya Vtuzgorodok Kamennye_palatki University",
    "Vilonovskaya Gagarinskaya Vostochnaya Kuybyshevskaya Geologicheskaya Dvorets_sporta \
     Aviatsionnaya Voennaya Sovhoznaya",
];
const CIRCLE: &str = "Uralskaya Pionerskaya Gagarinskaya Vtuzgorodok Sibirskaya Oborony_square \
     Bazhovskaya Dvorets_sporta Posadskaya Moskovskaya Kommunarov_square City";

fn main() {
    let mut adj: HashMap<&str, Vec<&str>> = HashMap::new();
    let mut join = |a: &'static str, b: &'static str| {
        adj.entry(a).or_default().push(b);
        adj.entry(b).or_default().push(a);
    };
    for line in LINES {
        let stops: Vec<&str> = line.split_whitespace().collect();
        for pair in stops.windows(2) {
            join(pair[0], pair[1]);
        }
    }
    let ring: Vec<&str> = CIRCLE.split_whitespace().collect();
    for i in 0..ring.len() {
        join(ring[i], ring[(i + 1) % ring.len()]);
    }
    // every run between neighbouring stations takes a minute and changes are
    // free, so the answer is the number of runs on a shortest path
    let mut dist: HashMap<&str, HashMap<&str, u32>> = HashMap::new();
    for &start in adj.keys() {
        let mut seen: HashMap<&str, u32> = HashMap::from([(start, 0)]);
        let mut queue = VecDeque::from([start]);
        while let Some(v) = queue.pop_front() {
            for &u in &adj[v] {
                if !seen.contains_key(u) {
                    seen.insert(u, seen[v] + 1);
                    queue.push_back(u);
                }
            }
        }
        dist.insert(start, seen);
    }
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut out = String::new();
    for _ in 0..n {
        let (a, b) = (words.next().unwrap(), words.next().unwrap());
        out.push_str(&format!("{}\n", dist[a][b]));
    }
    print!("{}", out);
}
