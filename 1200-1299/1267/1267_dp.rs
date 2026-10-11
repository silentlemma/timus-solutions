use std::io::{self, Read};

const INF: i64 = 1 << 62;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut pos = vec![0i64; n];
    for i in 1..n {
        pos[i] = pos[i - 1] + it.next().unwrap();
    }
    let start = it.next().unwrap() as usize - 1;
    let (period, first_up, first_down) =
        (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
    if n == 1 {
        println!("0");
        return;
    }
    // trains run forever: towards N they pass station i at first_up + pos[i]
    // plus multiples of the period, towards 1 at first_down + pos[N] - pos[i]
    let phase: [Vec<i64>; 2] = [
        (0..n).map(|i| (first_up + pos[i]) % period).collect(),
        (0..n)
            .map(|i| (first_down + pos[n - 1] - pos[i]) % period)
            .collect(),
    ];
    // the first train in direction d at station j not before time t
    let next = |d: usize, j: usize, t: i64| t + (phase[d][j] - t).rem_euclid(period);
    let full = (1usize << n) - 1;
    let mut arrive = vec![INF; (full + 1) * n];
    let mut best = INF;
    for d0 in 0..2 {
        let t0 = phase[d0][start];
        // arrive[mask * n + j]: earliest time standing at j with mask inspected
        arrive.iter_mut().for_each(|x| *x = INF);
        for k in 0..n {
            if (d0 == 0 && k > start) || (d0 == 1 && k < start) {
                arrive[(1 << start | 1 << k) * n + k] = t0 + (pos[k] - pos[start]).abs();
            }
        }
        for mask in 0..full {
            if mask >> start & 1 == 0 {
                continue;
            }
            for j in 0..n {
                let t = arrive[mask * n + j];
                if t == INF {
                    continue;
                }
                for d in 0..2 {
                    let dep = next(d, j, t + 1);
                    for k in 0..n {
                        if (d == 0 && k <= j) || (d == 1 && k >= j) || mask >> k & 1 == 1 {
                            continue;
                        }
                        let at = (mask | 1 << k) * n + k;
                        arrive[at] = arrive[at].min(dep + (pos[k] - pos[j]).abs());
                    }
                }
            }
        }
        // with everything inspected, ride straight back to the start
        for j in 0..n {
            let t = arrive[full * n + j];
            if t == INF || j == start {
                continue;
            }
            let d = if start > j { 0 } else { 1 };
            best = best.min(next(d, j, t + 1) + (pos[start] - pos[j]).abs() - t0);
        }
    }
    println!("{}", best);
}
