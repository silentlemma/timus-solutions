use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let mut next = || it.next().unwrap();
    let (p, t, n, m) = (next(), next(), next(), next());
    let (half, full) = (t / 2, (1usize << n) - 1);
    // after[x]: the dishes that may still be brought over a plate of dish x
    let mut after = vec![full; n];
    for _ in 0..m {
        let (i, j) = (next(), next());
        after[i - 1] &= !(1 << (j - 1));
    }
    // the count of time-tables depends only on the set of dishes that may be
    // brought; plates above a plate of x shrink that set to its part in after[x]
    let mut seen = vec![false; full + 1];
    seen[full] = true;
    let (mut stack, mut order) = (vec![full], Vec::new());
    while let Some(allowed) = stack.pop() {
        order.push(allowed);
        for (x, &mask) in after.iter().enumerate() {
            let inner = allowed & mask;
            if allowed >> x & 1 == 1 && !seen[inner] {
                seen[inner] = true;
                stack.push(inner);
            }
        }
    }
    order.sort_by_key(|s| s.count_ones());
    // ways[s][q]: time-tables of q dishes with the set s allowed
    let mut ways: Vec<Vec<usize>> = vec![Vec::new(); full + 1];
    for allowed in order {
        let mut f = vec![0usize; half + 1];
        let mut tree = vec![0usize; half]; // tree[q]: one plate with q dishes over it
        f[0] = 1;
        for q in 1..=half {
            let mut sum = 0;
            for (x, &mask) in after.iter().enumerate() {
                if allowed >> x & 1 == 1 {
                    let inner = allowed & mask;
                    sum += if inner == allowed {
                        f[q - 1]
                    } else {
                        ways[inner][q - 1]
                    };
                }
            }
            tree[q - 1] = sum % p;
            // the first plate holds a dishes over it, the rest follow it
            f[q] = (0..q).fold(0, |acc, a| (acc + tree[a] * f[q - 1 - a]) % p);
        }
        ways[allowed] = f;
    }
    println!("{}", ways[full][half] % p);
}
