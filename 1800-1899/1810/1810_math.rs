use std::io::{self, Read};

const MOD: usize = 3;
const SHIFT: u32 = 32;

// a vector over GF(3) as the masks of coordinates equal to 1 and to 2
type Vec3 = (u64, u64);

fn add(a: Vec3, b: Vec3) -> Vec3 {
    let t = (a.0 | b.1) ^ (a.1 | b.0);
    ((a.1 | b.1) ^ t, (a.0 | b.0) ^ t)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let (k, n) = (v[0], v[1]);
    let mut m = vec![vec![0usize; k]; n];
    let mut target = vec![0usize; k];
    for i in 0..k {
        let row = &v[2 + i * (n + 1)..2 + (i + 1) * (n + 1)];
        for j in 0..n {
            m[j][i] = row[j];
        }
        target[i] = row[n];
    }
    // vectors w that are orthogonal to the column of every variable span the
    // null space of the transposed matrix, and y is Ax for some x exactly when
    // every such w is orthogonal to y
    let mut pivots: Vec<usize> = Vec::new();
    for c in 0..k {
        let r = pivots.len();
        let sel = match (r..n).find(|&i| m[i][c] != 0) {
            Some(sel) => sel,
            None => continue,
        };
        m.swap(r, sel);
        if m[r][c] == 2 {
            for x in m[r].iter_mut() {
                *x = *x * 2 % MOD;
            }
        }
        let pivot_row = m[r].clone();
        for (i, row) in m.iter_mut().enumerate() {
            if i == r || row[c] == 0 {
                continue;
            }
            let f = row[c];
            for (x, &p) in row.iter_mut().zip(pivot_row.iter()) {
                *x = (*x + MOD * MOD - f * p) % MOD;
            }
        }
        pivots.push(c);
    }
    let rank = pivots.len();
    let mut basis: Vec<Vec<usize>> = Vec::new();
    for free in (0..k).filter(|c| !pivots.contains(c)) {
        let mut w = vec![0; k];
        w[free] = 1;
        for (i, &c) in pivots.iter().enumerate() {
            w[c] = (MOD - m[i][free]) % MOD;
        }
        basis.push(w);
    }
    // the change that y_i = 1 makes to the syndromes w . y over the basis,
    // and y_i = 2 makes the opposite change, the two masks swapped
    let unit: Vec<Vec3> = (0..k)
        .map(|i| {
            let mut u = (0u64, 0u64);
            for (j, w) in basis.iter().enumerate() {
                if w[i] == 1 {
                    u.0 |= 1 << j;
                } else if w[i] == 2 {
                    u.1 |= 1 << j;
                }
            }
            u
        })
        .collect();
    let syndromes = |from: usize, to: usize| -> Vec<Vec3> {
        let mut sums: Vec<Vec3> = vec![(0, 0)];
        for i in from..to {
            let mut next = Vec::with_capacity(sums.len() * 2);
            for &s in sums.iter() {
                for val in (0..MOD).filter(|&val| val != target[i]) {
                    next.push(match val {
                        0 => s,
                        1 => add(s, unit[i]),
                        _ => add(s, (unit[i].1, unit[i].0)),
                    });
                }
            }
            sums = next;
        }
        sums
    };
    // every y_i has two allowed values: meet in the middle on syndromes
    let half = k / 2;
    let mut left: Vec<u64> = syndromes(0, half).iter().map(|s| s.0 << SHIFT | s.1).collect();
    left.sort_unstable();
    let mut total: u64 = 0;
    for s in syndromes(half, k) {
        let key = s.1 << SHIFT | s.0;
        let lo = left.partition_point(|&x| x < key);
        let hi = left.partition_point(|&x| x <= key);
        total += (hi - lo) as u64;
    }
    for _ in rank..n {
        total *= MOD as u64;
    }
    println!("{}", total);
}
