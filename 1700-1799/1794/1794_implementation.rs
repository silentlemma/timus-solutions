use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap();
    // votes[k]: how many students get their wish if student k starts
    let mut votes = vec![0; n as usize + 1];
    for (i, want) in (1..=n).zip(it) {
        // student i speaks want-th when student i - want + 1 starts
        votes[((i - want).rem_euclid(n) + 1) as usize] += 1;
    }
    let mut best = 1;
    for k in 2..=n as usize {
        if votes[k] > votes[best] {
            best = k;
        }
    }
    println!("{}", best);
}
