use std::collections::{BTreeSet, HashMap};
use std::io::{self, Read};

const MINUTE: i64 = 60;
const HOUR: i64 = MINUTE * MINUTE;
const DAY: i64 = 24 * HOUR;
const ELEMENTS: &str = "AEFW";
// values closer than this are taken as equal
const EPS: f64 = 1e-9;

struct Element {
    strong: i64,
    top: i64,
    weak: i64,
    low: i64,
}

fn seconds(text: &str) -> i64 {
    text.split(':')
        .map(|p| p.parse::<i64>().unwrap())
        .fold(0, |acc, v| acc * MINUTE + v)
}

// the power falls linearly from the strong moment to the weak one and rises
// back over the rest of the day
fn power(e: &Element, t: i64) -> f64 {
    let fall = (e.weak - e.strong).rem_euclid(DAY);
    let since = (t - e.strong).rem_euclid(DAY);
    if since <= fall {
        e.top as f64 + (e.low - e.top) as f64 * since as f64 / fall as f64
    } else {
        e.low as f64 + (e.top - e.low) as f64 * (since - fall) as f64 / (DAY - fall) as f64
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input.split_ascii_whitespace();
    let mut moments: HashMap<char, Element> = HashMap::new();
    for _ in 0..ELEMENTS.len() {
        let code = tok.next().unwrap().chars().next().unwrap();
        let strong = seconds(tok.next().unwrap());
        let top = tok.next().unwrap().parse().unwrap();
        let weak = seconds(tok.next().unwrap());
        let low = tok.next().unwrap().parse().unwrap();
        moments.insert(
            code,
            Element {
                strong,
                top,
                weak,
                low,
            },
        );
    }
    let mut side: HashMap<char, i64> = HashMap::new();
    for c in tok.next().unwrap().chars() {
        *side.entry(c).or_default() += 1;
    }
    for c in tok.next().unwrap().chars() {
        *side.entry(c).or_default() -= 1;
    }
    let advantage = |t: i64| -> f64 {
        ELEMENTS
            .chars()
            .map(|e| side.get(&e).copied().unwrap_or(0))
            .zip(ELEMENTS.chars())
            .filter(|&(c, _)| c != 0)
            .map(|(c, e)| c as f64 * power(&moments[&e], t))
            .sum()
    };
    // the advantage is linear between the moments, so its largest value over
    // the day is at a moment or at either end of the day
    let mut times: BTreeSet<i64> = [0, DAY - 1].into_iter().collect();
    for e in moments.values() {
        times.insert(e.strong);
        times.insert(e.weak);
    }
    let mut best: Option<(f64, i64)> = None;
    for &t in &times {
        let v = advantage(t);
        if best.map_or(true, |(b, _)| v > b + EPS) {
            best = Some((v, t));
        }
    }
    let (best, when) = best.unwrap();
    if best <= EPS {
        println!("We can't win!");
    } else {
        println!(
            "{:02}:{:02}:{:02}\n{:.2}",
            when / HOUR,
            when / MINUTE % MINUTE,
            when % MINUTE,
            best
        );
    }
}
