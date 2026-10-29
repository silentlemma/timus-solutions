use std::io::{self, BufRead, BufReader};

fn main() {
    const INPUT_BUFFER_SIZE: usize = 1024;
    // the prices are read line by line through a 1 KB buffered reader instead
    // of reading the whole input into a string
    let stdin = io::stdin();
    let mut input = BufReader::with_capacity(INPUT_BUFFER_SIZE, stdin.lock());
    let mut line = String::new();
    input.read_line(&mut line).unwrap();
    let n: usize = line.trim().parse().unwrap();
    // best is the largest segment sum so far (the empty segment gives 0), and
    // ending is the largest sum of a segment that ends at the current number
    let (mut best, mut ending) = (0i64, 0i64);
    for _ in 0..n {
        line.clear();
        input.read_line(&mut line).unwrap();
        let p: i64 = line.trim().parse().unwrap();
        ending += p;
        ending = ending.max(0);
        best = best.max(ending);
    }
    println!("{}", best);
}
