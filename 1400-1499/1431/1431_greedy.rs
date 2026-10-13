use std::io::{self, Read};

const TOP: usize = 30;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut count = [0usize; TOP + 2];
    for _ in 0..n {
        count[it.next().unwrap()] += 1;
    }
    // two types share a symmetric alternating row only as ABA...BA, counts differing by one,
    // along the chain of counts, pairing the leftovers of c with c + 1 at once is best
    let (mut pairs, mut left) = (0, 0);
    for c in 1..=TOP {
        let matched = left.min(count[c]);
        pairs += matched;
        left = count[c] - matched;
    }
    println!("{}", n - pairs);
}
