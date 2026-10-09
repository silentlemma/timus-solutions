use std::io::{self, Read};

const RADIUS: f64 = 6875.0 / 2.0;
const DANGER: f64 = 100.0;
const MINUTES: f64 = 60.0;
const SECONDS: f64 = 3600.0;
const HUNDREDTHS: f64 = 100.0;
const PARTS: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let text: String = input
        .chars()
        .map(|c| if "^'\"".contains(c) { ' ' } else { c })
        .collect();
    let tokens: Vec<&str> = text.split_ascii_whitespace().collect();
    // every coordinate is "degrees minutes seconds" followed by NL, SL, EL or WL
    let mut angle = Vec::new();
    for i in PARTS..tokens.len() {
        let t = tokens[i].as_bytes();
        if t.len() < 2 || t[1] != b'L' || !b"NSEW".contains(&t[0]) {
            continue;
        }
        let part = |k: usize| tokens[i - k].parse::<f64>().unwrap();
        let degrees = part(PARTS) + part(2) / MINUTES + part(1) / SECONDS;
        let signed = if t[0] == b'S' || t[0] == b'W' {
            -degrees
        } else {
            degrees
        };
        angle.push(signed.to_radians());
    }
    let (lat1, lon1, lat2, lon2) = (angle[0], angle[1], angle[2], angle[angle.len() - 1]);
    // the haversine formula keeps its precision for small distances
    let h = ((lat2 - lat1) / 2.0).sin().powi(2)
        + lat1.cos() * lat2.cos() * ((lon2 - lon1) / 2.0).sin().powi(2);
    let distance = 2.0 * RADIUS * h.sqrt().min(1.0).asin();
    println!("The distance to the iceberg: {:.2} miles.", distance);
    // the comparison uses the printed value: 99.996 is printed as 100.00
    if (distance * HUNDREDTHS).round() < DANGER * HUNDREDTHS {
        println!("DANGER!");
    }
}
