use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<u64>().unwrap());
    let mut next = || words.next().unwrap();
    let (m, d1, d2) = (next(), next(), next());
    // the work is m * d1 digger-days; spreading it as evenly as possible
    // over d2 days needs the fewest diggers, the rounded-up average
    let work = m * d1;
    let (low, extra) = (work / d2, work % d2);
    let days: Vec<String> = (0..d2)
        .map(|day| (if day < d2 - extra { low } else { low + 1 }).to_string())
        .collect();
    println!("{}", days.join(" "));
}
