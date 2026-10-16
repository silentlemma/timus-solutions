use std::io::{self, Read, Write};

// times in tenths of a second; starts are 30 seconds apart
const TENTHS_PER_MINUTE: u32 = 600;
const TENTHS_PER_SECOND: u32 = 10;
const GAP: u32 = 300;

fn tenths(text: &str) -> u32 {
    let (minutes, rest) = text.split_once(':').unwrap();
    let (seconds, tenth) = rest.split_once('.').unwrap();
    minutes.parse::<u32>().unwrap() * TENTHS_PER_MINUTE
        + seconds.parse::<u32>().unwrap() * TENTHS_PER_SECOND
        + tenth.parse::<u32>().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: u32 = match it.next() {
        Some(t) => t.parse().unwrap(),
        None => return,
    };
    let mut finishes: Vec<(u32, u32, &str)> = (0..n)
        .map(|i| {
            let name = it.next().unwrap();
            let run = tenths(it.next().unwrap());
            (i * GAP + run, run, name)
        })
        .collect();
    finishes.sort();
    // replay the finishes in order; the board changes on every new best run
    let mut leaders = Vec::new();
    let mut best = u32::MAX;
    for &(_, run, name) in &finishes {
        if run < best {
            best = run;
            leaders.push(name);
        }
    }
    leaders.sort();
    let mut out = format!("{}\n", leaders.len());
    for name in leaders {
        out.push_str(name);
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
