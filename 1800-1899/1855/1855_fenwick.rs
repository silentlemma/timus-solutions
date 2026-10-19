use std::fmt::Write;
use std::io::{self, Read};

const POWERS: usize = 3; // i^0, i^1 and i^2

// all sums are kept modulo 2^64 with wrapping arithmetic: some of them
// overflow on the way, but the final total of a guild fits in an i64

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let m: usize = it.next().unwrap().parse().unwrap();
    // the sums of i^0, i^1 and i^2 for i up to x
    let mut sums = vec![[0i64; POWERS]; n + 2];
    for i in 1..n + 2 {
        let v = i as i64;
        sums[i] = [v, sums[i - 1][1] + v, sums[i - 1][2] + v * v];
    }
    // toll t_i on segment i is the prefix sum of the differences dif_j; the
    // sum of i^k t_i over i <= x is S_k(x) * (sum of dif_j) minus the sum of
    // dif_j * S_k(j - 1) over j <= x: entry 0 keeps dif_j, entry k + 1 the rest
    let size = n + 1;
    let mut tree = vec![[0i64; POWERS + 1]; size + 1];
    let add = |tree: &mut Vec<[i64; POWERS + 1]>, mut j: usize, d: i64| {
        let w = sums[j - 1];
        while j <= size {
            tree[j][0] = tree[j][0].wrapping_add(d);
            for k in 0..w.len() {
                tree[j][k + 1] = tree[j][k + 1].wrapping_add(d.wrapping_mul(w[k]));
            }
            j += j & j.wrapping_neg();
        }
    };
    let prefix = |tree: &Vec<[i64; POWERS + 1]>, x: usize| -> [i64; POWERS] {
        // the sums of t_i, i t_i and i^2 t_i over i <= x
        let mut s = [0i64; POWERS + 1];
        let mut j = x;
        while j > 0 {
            for k in 0..s.len() {
                s[k] = s[k].wrapping_add(tree[j][k]);
            }
            j -= j & j.wrapping_neg();
        }
        let p = sums[x];
        let mut r = [0i64; POWERS];
        for k in 0..r.len() {
            r[k] = p[k].wrapping_mul(s[0]).wrapping_sub(s[k + 1]);
        }
        r
    };
    let mut out = String::new();
    for _ in 0..m {
        let kind = it.next().unwrap();
        let a: usize = it.next().unwrap().parse().unwrap();
        let b: usize = it.next().unwrap().parse().unwrap();
        if kind == "change" {
            let d: i64 = it.next().unwrap().parse().unwrap();
            add(&mut tree, a, d);
            add(&mut tree, b, -d);
            continue;
        }
        let (hi, lo) = (prefix(&tree, b - 1), prefix(&tree, a - 1));
        let s0 = hi[0].wrapping_sub(lo[0]);
        let s1 = hi[1].wrapping_sub(lo[1]);
        let s2 = hi[2].wrapping_sub(lo[2]);
        let (a, b) = (a as i64, b as i64);
        // segment i lies on (i - a + 1)(b - i) of the guild's routes
        let total = (a + b - 1)
            .wrapping_mul(s1)
            .wrapping_sub(s2)
            .wrapping_add((b * (1 - a)).wrapping_mul(s0));
        let routes = (b - a + 1) * (b - a) / 2;
        writeln!(out, "{:.8}", total as f64 / routes as f64).unwrap();
    }
    print!("{}", out);
}
