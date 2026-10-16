use std::io::{self, Read};

// (lo, hi): the pedestals lo, lo + 2, ..., hi where the artifact may be,
// empty when lo > hi
type Run = (i64, i64);

fn spread((lo, hi): Run, n: i64) -> Run {
    if lo > hi {
        return (lo, hi);
    }
    (if lo > 1 { lo - 1 } else { lo + 1 }, if hi < n { hi + 1 } else { hi - 1 })
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap();
    let m = it.next().unwrap() as usize;
    // runs[p] holds the pedestals of parity p
    let mut runs: [Run; 2] = [(2, n - n % 2), (1, n - 1 + n % 2)];
    for x in it.take(m) {
        let p = (x % 2) as usize;
        let (lo, hi) = runs[p];
        // a touch inside the run leaves a hole that the next move fills
        // again, so only a touch at an end shrinks it
        if x == lo {
            runs[p] = (lo + 2, hi);
        } else if x == hi {
            runs[p] = (lo, hi - 2);
        }
        // every step flips the parity of the pedestal
        runs = [spread(runs[1], n), spread(runs[0], n)];
    }
    let done = runs.iter().all(|&(lo, hi)| lo > hi);
    println!("{}", if done { "YES" } else { "NO" });
}
