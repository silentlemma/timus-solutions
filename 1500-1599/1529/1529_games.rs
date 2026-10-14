use std::io::{self, Read};

fn gcd(a: usize, b: usize) -> usize {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

// steps x through all tuples below dims, last axis fastest; false when done
fn advance(x: &mut [usize], dims: &[usize]) -> bool {
    for i in (0..dims.len()).rev() {
        x[i] += 1;
        if x[i] < dims[i] {
            return true;
        }
        x[i] = 0;
    }
    false
}

// turns a into the next ordering, false after the last one
fn next_permutation(a: &mut [usize]) -> bool {
    let n = a.len();
    let mut i = n - 1;
    while i > 0 && a[i - 1] >= a[i] {
        i -= 1;
    }
    if i == 0 {
        return false;
    }
    let mut j = n - 1;
    while a[j] <= a[i - 1] {
        j -= 1;
    }
    a.swap(i - 1, j);
    a[i..].reverse();
    true
}

struct Game {
    radix: Vec<usize>,
    cuts_of: Vec<Vec<usize>>, // legal cuts by edge length
}

impl Game {
    fn offset(&self, x: &[usize]) -> usize {
        x.iter().zip(&self.radix).map(|(v, r)| v * r).sum()
    }

    // the XOR over all parts for every tuple of cuts, last cut fastest: table
    // holds the values of the parts by piece lengths, and each axis in turn is
    // replaced by its cuts, a cut c of an edge d joining the pieces c - 1, d - c
    fn cut_values(&self, mut table: Vec<usize>, dims: &[usize]) -> Vec<usize> {
        let mut sizes = dims.to_vec();
        for axis in (0..dims.len()).rev() {
            let inner: usize = sizes[axis + 1..].iter().product();
            let d = sizes[axis];
            let cuts = &self.cuts_of[d];
            let mut out = Vec::with_capacity(table.len() / d * cuts.len());
            for start in (0..table.len()).step_by(d * inner) {
                for &c in cuts {
                    let (low, high) = (start + (c - 1) * inner, start + (d - c) * inner);
                    out.extend((0..inner).map(|j| table[low + j] ^ table[high + j]));
                }
            }
            table = out;
            sizes[axis] = cuts.len();
        }
        table
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let k = v[0];
    let edges = v[1..1 + k].to_vec();
    if k == 1 {
        // pieces of a segment of length d total d - 1, so by induction its
        // value is d mod 2, and from an odd length every cut wins
        println!("{}", if edges[0] % 2 == 1 { "1\n1" } else { "2" });
        return;
    }
    if edges.contains(&1) {
        // any cut empties a box with an edge of 1, so Alice cuts and wins
        println!("1\n{}", vec!["1"; k].join(" "));
        return;
    }
    // every ordering of a box's edges is stored with the same value, indexed
    // by a mixed radix over the sorted edges of the whole box
    let mut bound = edges.clone();
    bound.sort_unstable();
    let mut radix = vec![1; k];
    for i in (0..k - 1).rev() {
        radix[i] = radix[i + 1] * (bound[i + 1] + 1);
    }
    let longest = bound[k - 1];
    let cuts_of: Vec<Vec<usize>> = (0..=longest)
        .map(|d| {
            (1..=d)
                .filter(|&c| (c > 1 && gcd(c - 1, d) == 1) || (d > c && gcd(d - c, d) == 1))
                .collect()
        })
        .collect();
    let game = Game { radix, cuts_of };
    // boxes with an empty edge stay 0
    let mut grundy = vec![0usize; game.radix[0] * (bound[0] + 1)];
    // the boxes with sorted edges, smaller ones first
    let mut boxes = Vec::new();
    let mut place = vec![0usize; k];
    loop {
        let b: Vec<usize> = place.iter().map(|x| x + 1).collect();
        if b.windows(2).all(|w| w[0] <= w[1]) {
            boxes.push(b);
        }
        if !advance(&mut place, &bound) {
            break;
        }
    }
    boxes.sort_by_key(|b| b.iter().sum::<usize>());
    let mut seen = vec![0usize; grundy.len() + 2];
    let mut stamp = 0;
    for mut b in boxes {
        let mut g = 0;
        if b[0] == 1 {
            g = 1;
        } else if b.iter().all(|&d| !game.cuts_of[d].is_empty()) {
            // the parts by piece lengths, a row along the last axis at a time
            let mut table = Vec::new();
            let mut prefix = vec![0usize; k];
            loop {
                let base = game.offset(&prefix);
                table.extend_from_slice(&grundy[base..base + b[k - 1]]);
                if !advance(&mut prefix[..k - 1], &b[..k - 1]) {
                    break;
                }
            }
            stamp += 1;
            for value in game.cut_values(table, &b) {
                seen[value] = stamp;
            }
            while seen[g] == stamp {
                g += 1;
            }
        }
        // only orderings within the bounds are ever looked up
        loop {
            if b.iter().zip(&bound).all(|(x, e)| x <= e) {
                grundy[game.offset(&b)] = g;
            }
            if !next_permutation(&mut b) {
                break;
            }
        }
    }
    if grundy[game.offset(&bound)] == 0 {
        println!("2");
        return;
    }
    // the first winning cut in lexicographic order, in the input's order
    let mut table = Vec::new();
    let mut x = vec![0usize; k];
    loop {
        let mut sorted = x.clone();
        sorted.sort_unstable();
        table.push(grundy[game.offset(&sorted)]);
        if !advance(&mut x, &edges) {
            break;
        }
    }
    let counts: Vec<usize> = edges.iter().map(|&e| game.cuts_of[e].len()).collect();
    let mut pos = vec![0usize; k];
    for value in game.cut_values(table, &edges) {
        if value == 0 {
            let moves: Vec<String> = (0..k)
                .map(|i| game.cuts_of[edges[i]][pos[i]].to_string())
                .collect();
            println!("1\n{}", moves.join(" "));
            return;
        }
        advance(&mut pos, &counts);
    }
}
