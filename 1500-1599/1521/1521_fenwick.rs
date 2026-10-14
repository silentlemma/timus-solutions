use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, k) = (v[0], v[1]);
    // a Fenwick tree over the circle: 1 for a soldier still marching
    let mut tree = vec![0usize; n + 1];
    for i in 1..=n {
        tree[i] += 1;
        let parent = i + (i & i.wrapping_neg());
        if parent <= n {
            tree[parent] += tree[i];
        }
    }
    let top = 1usize << (usize::BITS - 1 - n.leading_zeros());
    let mut out = String::new();
    let mut rank = 0;
    for left in (1..=n).rev() {
        // the soldier k places ahead, counting among those still marching
        rank = (rank + k - 1) % left;
        // descend to the (rank + 1)-th remaining soldier
        let (mut pos, mut need, mut step) = (0, rank + 1, top);
        while step > 0 {
            if pos + step <= n && tree[pos + step] < need {
                pos += step;
                need -= tree[pos];
            }
            step >>= 1;
        }
        pos += 1;
        write!(out, "{}{}", pos, if left > 1 { ' ' } else { '\n' }).unwrap();
        let mut i = pos;
        while i <= n {
            tree[i] -= 1;
            i += i & i.wrapping_neg();
        }
    }
    print!("{}", out);
}
