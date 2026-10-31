use std::io::{self, BufWriter, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_ascii_whitespace()
        .map(|s| s.parse::<usize>().unwrap());
    let (n, k) = (values.next().unwrap(), values.next().unwrap());
    // a fenwick tree over the circle: 1 for a soldier still marching
    // initially every interval is full, so its count is lowbit(i) <= n <= 100000.
    let mut tree: Vec<u32> = (0..=n).map(|i| (i & i.wrapping_neg()) as u32).collect();
    let top = 1usize << (usize::BITS - 1 - n.leading_zeros());
    let stdout = io::stdout();
    let mut out = BufWriter::new(stdout.lock());
    let mut rank = 0;
    for left in (1..=n).rev() {
        // the soldier k places ahead, counting among those still marching
        rank = (rank + k - 1) % left;
        // descend to the (rank + 1)-th remaining soldier
        let (mut pos, mut need, mut step) = (0, rank + 1, top);
        while step > 0 {
            let next = pos + step;
            if next <= n {
                if (tree[next] as usize) < need {
                    need -= tree[next] as usize;
                    pos = next;
                } else {
                    // this fenwick interval contains the soldier being removed.
                    tree[next] -= 1;
                }
            }
            step >>= 1;
        }
        write!(out, "{}{}", pos + 1, if left > 1 { ' ' } else { '\n' }).unwrap();
    }
}
