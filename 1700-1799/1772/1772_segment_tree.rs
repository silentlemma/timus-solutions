use std::io::{self, Read};

const FAR: i64 = 1 << 40;

struct Track {
    n: usize,
    s: i64,
    size: usize,
    latest: Vec<usize>,
    left: Vec<i64>,
    right: Vec<i64>,
}

impl Track {
    // the cost of a lane comes from the latest obstacle covering it, as
    // min(left[t] + x, right[t] - x), or from the start as |x - s| if none
    fn cost(&self, x: usize) -> i64 {
        let mut t = 0;
        let mut node = x + self.size;
        while node > 0 {
            t = t.max(self.latest[node]);
            node >>= 1;
        }
        let x = x as i64;
        if t == 0 {
            (x - self.s).abs()
        } else {
            (self.left[t] + x).min(self.right[t] - x)
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let mut next = || words.next().unwrap();
    let (n, s, k) = (next(), next(), next());
    let mut size = 1;
    while size <= n {
        size *= 2;
    }
    // latest[node]: the last obstacle whose lanes cover the node's whole range
    let mut track = Track {
        n,
        s: s as i64,
        size,
        latest: vec![0; 2 * size],
        left: vec![0; k + 1],
        right: vec![0; k + 1],
    };
    for t in 1..=k {
        let (lo, hi) = (next(), next());
        // the cost stays one per lane apart, so going round the obstacle
        // only needs the lanes just beside it
        let below = if lo > 1 { track.cost(lo - 1) } else { FAR };
        let above = if hi < track.n { track.cost(hi + 1) } else { FAR };
        track.left[t] = below - (lo as i64 - 1);
        track.right[t] = above + hi as i64 + 1;
        let (mut a, mut b) = (lo + size, hi + size + 1);
        while a < b {
            if a & 1 == 1 {
                track.latest[a] = t;
                a += 1;
            }
            if b & 1 == 1 {
                b -= 1;
                track.latest[b] = t;
            }
            a >>= 1;
            b >>= 1;
        }
    }
    let best = (1..=n).map(|x| track.cost(x)).min().unwrap();
    println!("{}", best);
}
