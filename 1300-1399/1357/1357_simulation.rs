use std::collections::VecDeque;
use std::io::{self, Read, Write};

const SPECIFIC_HEAT: i64 = 4190; // J/(kg K)
const PORTION_GRAMS: i64 = 200;
const COLD: i64 = 20; // degrees
const BOILING: i64 = 100;
const POWER: i64 = 400; // W

// heating one portion takes C m dT / P seconds; with m in grams this is
// exactly the number of milliseconds, 167 600
const PORTION_MS: i64 = SPECIFIC_HEAT * PORTION_GRAMS * (BOILING - COLD) / POWER;
const CAPACITY: usize = 5; // portions in a full teakettle
const MS: i64 = 1000;
const MINUTE: i64 = 60;
const HOUR: i64 = MINUTE * MINUTE;
const DAY: i64 = 24 * HOUR;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().map_or(0, |t| t.parse().unwrap());
    let wake: Vec<i64> = it
        .take(n)
        .map(|t| {
            let p: Vec<i64> = t.split(':').map(|x| x.parse().unwrap()).collect();
            (p[0] * HOUR + p[1] * MINUTE + p[2]) * MS
        })
        .collect();
    let mut ready = vec![0i64; n];
    let mut kettle: Vec<usize> = Vec::new();
    let mut waiting: VecDeque<usize> = VecDeque::new();
    let mut boil = 0i64; // the moment the water in the kettle boils, in milliseconds
    let mut i = 0;
    while i < n || !kettle.is_empty() {
        // water that boils exactly when someone wakes up is poured out first
        if !kettle.is_empty() && (i == n || wake[i] >= boil) {
            for &j in &kettle {
                ready[j] = boil;
            }
            kettle.clear();
            while kettle.len() < CAPACITY {
                match waiting.pop_front() {
                    Some(j) => kettle.push(j),
                    None => break,
                }
            }
            boil += PORTION_MS * kettle.len() as i64;
            continue;
        }
        if kettle.is_empty() {
            kettle.push(i);
            boil = wake[i] + PORTION_MS;
        } else if kettle.len() < CAPACITY {
            // the heat still missing grows by one portion's worth
            kettle.push(i);
            boil += PORTION_MS;
        } else {
            waiting.push_back(i);
        }
        i += 1;
    }
    let mut out = String::new();
    for &t in &ready {
        let sec = (t + MS - 1) / MS % DAY; // rounded up, past midnight from 00:00:00
        out.push_str(&format!(
            "{:02}:{:02}:{:02}\n",
            sec / HOUR,
            sec / MINUTE % MINUTE,
            sec % MINUTE
        ));
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
