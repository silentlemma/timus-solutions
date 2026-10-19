use std::io::{self, Read};

const TRIO: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    if v.is_empty() {
        return;
    }
    let mut times = v[1..=v[0] as usize].to_vec();
    times.sort_unstable();
    let mut total = 0;
    // move the two slowest across each round, in whichever of two ways is
    // cheaper: the fastest escorts each of them, or the two fastest cross,
    // one comes back, the two slowest cross together and the other returns
    while times.len() > TRIO {
        let k = times.len();
        let (a, b, y, z) = (times[0], times[1], times[k - 2], times[k - 1]);
        total += (2 * a + y + z).min(a + 2 * b + z);
        times.truncate(k - 2);
    }
    total += if times.len() == TRIO { times.iter().sum() } else { times[times.len() - 1] };
    println!("{}", total);
}
