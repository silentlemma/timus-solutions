use std::io::{self, Read};

const YEAR: i64 = 365;
const LEAP: i64 = 4;
const CENTURY: i64 = 100;
const LEAP_CENTURY: i64 = 400;
const MARCH: i64 = 3;
const MONTHS: i64 = 12;
// the five months from March to July hold 153 days, and so do August to
// December, which makes the days before a month a simple formula
const SPAN_DAYS: i64 = 153;
const SPAN_MONTHS: i64 = 5;

// days from a fixed origin, counting years from March so that the leap
// day comes last
fn day_number(text: &str) -> i64 {
    let parts: Vec<i64> = text.split('.').map(|v| v.parse().unwrap()).collect();
    let (d, mut m, mut y) = (parts[0], parts[1], parts[2]);
    if m < MARCH {
        y -= 1;
        m += MONTHS;
    }
    let leaps = y / LEAP - y / CENTURY + y / LEAP_CENTURY;
    YEAR * y + leaps + (SPAN_DAYS * (m - MARCH) + 2) / SPAN_MONTHS + d
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let (mut best, mut answer) = (-1, 0);
    for i in 1..=n {
        let born = words.next().unwrap();
        let _since = words.next().unwrap();
        let died = words.next().unwrap();
        let life = day_number(died) - day_number(born) + 1;
        // the list goes in order of death, so the first record holder died first
        if life > best {
            best = life;
            answer = i;
        }
    }
    println!("{}", answer);
}
