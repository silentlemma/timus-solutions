use std::io::{self, Read};

const SEATS: i64 = 36;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    // change[k] is how many people get on at station k minus how many get
    // off there; the eastbound and westbound trains are counted apart
    let mut east = vec![0i64; n + 1];
    let mut west = vec![0i64; n + 1];
    for i in 0..n {
        for j in 0..n {
            let a = it.next().unwrap();
            if i < j {
                east[i] += a;
                east[j] -= a;
            } else if i > j {
                west[j] += a;
                west[i] -= a;
            }
        }
    }
    let (mut best, mut load_e, mut load_w) = (0i64, 0i64, 0i64);
    for k in 0..n {
        load_e += east[k];
        load_w += west[k];
        best = best.max(load_e).max(load_w);
    }
    println!("{}", (best + SEATS - 1) / SEATS);
}
