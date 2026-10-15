use std::io::{self, Read};

const PER_ATTEMPT: i64 = 20; // minutes for each rejected attempt

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut nums = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let (t1, t2) = (nums.next().unwrap(), nums.next().unwrap());
    let clean = t2 - PER_ATTEMPT * nums.sum::<i64>();
    // without the rejected attempts ZZZ wins only with strictly less time
    println!("{}", if clean < t1 { "Dirty debug :(" } else { "No chance." });
}
