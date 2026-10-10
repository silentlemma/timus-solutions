use std::io::{self, Read};

const NAMES: [&str; 7] = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
const LENGTHS: [i64; 12] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
const WEEK: i64 = 7;
const YEAR: i64 = 365;
const CELL: usize = 5;
const LEAP: i64 = 4;
const CENTURY: i64 = 100;
const ERA: i64 = 400;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (d, m, y) = (v[0], v[1] as usize, v[2]);
    let mut lengths = LENGTHS;
    if y % LEAP == 0 && (y % CENTURY != 0 || y % ERA == 0) {
        lengths[1] += 1;
    }
    // days from 1 January of year 1, a Monday, to the first of the month
    let past = y - 1;
    let before = YEAR * past + past / LEAP - past / CENTURY
        + past / ERA
        + lengths[..m - 1].iter().sum::<i64>();
    let (first, days) = (before % WEEK, lengths[m - 1]);
    let cols = (first + days + WEEK - 1) / WEEK;
    let mut out = String::new();
    for (row, name) in NAMES.iter().enumerate() {
        out += name;
        for col in 0..cols {
            let day = col * WEEK + row as i64 - first + 1;
            let last = col == cols - 1;
            // every column is five characters wide, the last one four,
            // unless the bracketed date sits in it
            if day == d {
                out += &format!(" [{:2}]", day);
            } else if (1..=days).contains(&day) {
                out += &format!("  {:2}{}", day, if last { "" } else { " " });
            } else {
                out += &" ".repeat(if last { CELL - 1 } else { CELL });
            }
        }
        out.push('\n');
    }
    print!("{}", out);
}
