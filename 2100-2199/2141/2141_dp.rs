use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let first = it.next().unwrap();
    // plus and minus are the best sums of segments ending at the current dish
    // whose last dish counts with a plus or with a minus; before the second
    // dish no minus segment exists, and 0 there only means "start anew"
    let (mut plus, mut minus) = (first, 0i64);
    let mut best = first.max(0);
    for a in it.take(n - 1) {
        let next_plus = a + minus.max(0);
        minus = plus - a;
        plus = next_plus;
        best = best.max(plus).max(minus);
    }
    println!("{}", best);
}
