use std::io::{self, Read};

// R is a real number; all other lengths are integers, so a squared distance
// is an integer and only the integer part of R*R matters
const EPS: f64 = 1e-6;
// above every altitude a station allows: 32000 plus 100000
const SKY: i64 = 1_000_000;

fn isqrt(v: i64) -> i64 {
    let mut s = (v as f64).sqrt() as i64;
    while s * s > v {
        s -= 1;
    }
    while (s + 1) * (s + 1) <= v {
        s += 1;
    }
    s
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let mut next = || it.next().unwrap();
    let m: usize = next().parse().unwrap();
    let n: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();
    let h: Vec<i64> = (0..m * n).map(|_| next().parse().unwrap()).collect();
    let mut taken = vec![false; m * n];
    let mut stations = Vec::new();
    for _ in 0..k {
        let i: i64 = next().parse::<i64>().unwrap() - 1;
        let j: i64 = next().parse::<i64>().unwrap() - 1;
        let r: f64 = next().parse().unwrap();
        let c = i as usize * n + j as usize;
        taken[c] = true;
        stations.push((i, j, h[c], (r * r + EPS) as i64));
    }
    let mut total: i64 = 0;
    for i in 0..m {
        for j in 0..n {
            if taken[i * n + j] {
                continue;
            }
            // the receiver at altitude a hears a station at height z when
            // (a - z)^2 <= R^2 - (horizontal distance)^2
            let (mut low, mut high) = (h[i * n + j], SKY);
            for &(si, sj, z, reach) in &stations {
                let (di, dj) = (i as i64 - si, j as i64 - sj);
                let rest = reach - di * di - dj * dj;
                if rest < 0 {
                    high = -1;
                    break;
                }
                let s = isqrt(rest);
                low = low.max(z - s);
                high = high.min(z + s);
                if low > high {
                    break;
                }
            }
            if low <= high {
                total += high - low + 1;
            }
        }
    }
    println!("{}", total);
}
