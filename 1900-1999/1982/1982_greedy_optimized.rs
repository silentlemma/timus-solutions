use std::io::{self, BufRead, BufReader};

const BUFFER_SIZE: usize = 4096;
const MAX_COST: u32 = 100000;

fn read_number(input: &mut impl BufRead) -> usize {
    let mut value = 0;
    let mut started = false;
    loop {
        let data = input.fill_buf().unwrap();
        if data.is_empty() {
            return value;
        }
        let mut count = 0;
        let mut done = false;
        for &c in data {
            count += 1;
            if c.is_ascii_digit() {
                value = value * 10 + usize::from(c - b'0');
                started = true;
            } else if started {
                done = true;
                break;
            }
        }
        input.consume(count);
        if done {
            return value;
        }
    }
}

fn main() {
    // refill a small buffer instead of retaining the full matrix text.
    let mut input = BufReader::with_capacity(BUFFER_SIZE, io::stdin().lock());
    let n = read_number(&mut input);
    let k = read_number(&mut input);
    // every cost is at most MAX_COST, so MAX_COST + 1 works as infinity
    let mut best = vec![MAX_COST + 1; n];
    let mut used = vec![false; n];
    for _ in 0..k {
        best[read_number(&mut input) - 1] = 0;
    }
    // n <= 100 and costs <= 100000: edges and the total <= 9900000 fit u32.
    let cost: Vec<u32> = (0..n * n).map(|_| read_number(&mut input) as u32).collect();
    let mut answer = 0;
    for _ in 0..n {
        let vertex = (0..n)
            .filter(|&v| !used[v])
            .min_by_key(|&v| best[v])
            .unwrap();
        answer += best[vertex];
        used[vertex] = true;
        for v in 0..n {
            if !used[v] && cost[vertex * n + v] < best[v] {
                best[v] = cost[vertex * n + v];
            }
        }
    }
    println!("{}", answer);
}
