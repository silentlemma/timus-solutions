use std::f64::consts::PI;
use std::io::{self, Read};

const SCALE: i64 = 1000;
const HALF_TURN: i64 = 180 * SCALE;
const FULL_TURN: i64 = 2 * HALF_TURN;
const DIGITS: usize = 3;

// the angle in thousandths of a degree, read exactly from the text
fn thousandths(text: &str) -> i64 {
    let (whole, part) = match text.find('.') {
        Some(dot) => (&text[..dot], &text[dot + 1..]),
        None => (text, ""),
    };
    let part = format!("{}000", part);
    let w: i64 = if whole.is_empty() { 0 } else { whole.parse().unwrap() };
    w * SCALE + part[..DIGITS].parse::<i64>().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let r: f64 = it.next().unwrap().parse().unwrap();
    let a = thousandths(it.next().unwrap());
    // each shore point shows an arc of 2a, so the walk along the shore
    // covers 360 - 2a degrees; chords grow slower than their angles, so
    // it is shortest as full 2a chords and one short chord for the rest
    let steps = HALF_TURN / a;
    let rest = FULL_TURN - steps * 2 * a;
    let chord = |t: i64| 2.0 * r * (t as f64 * PI / FULL_TURN as f64).sin();
    println!("{:.7}", r + (steps - 1) as f64 * chord(2 * a) + chord(rest));
}
