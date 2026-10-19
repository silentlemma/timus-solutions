use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<usize>().unwrap());
    let mut next = || it.next().unwrap();
    let (n, s, d) = (next(), next(), next());
    let mut planets: Vec<(usize, usize)> = (0..n).map(|_| (next(), next())).collect();
    planets.sort_unstable();
    let dist: Vec<usize> = planets.iter().map(|p| p.0).collect();
    let race: Vec<usize> = planets.iter().map(|p| p.1).collect();
    // pieces of planets with gaps of at most d: the tourist moves only
    // inside a piece cut by the range [low, high]
    let mut piece = vec![0usize; n];
    let mut first = vec![0usize];
    for i in 1..n {
        if dist[i] - dist[i - 1] > d {
            first.push(i);
        }
        piece[i] = first.len() - 1;
    }
    first.push(n);
    let pieces = first.len() - 1;
    // head[i]: races from the start of i's piece to i; tail[i]: from i to
    // its end; whole[p]: races of piece p
    let (mut head, mut tail, mut whole) = (vec![0; n], vec![0; n], vec![0usize; pieces]);
    let mut mark = vec![usize::MAX; s + 1];
    for p in 0..pieces {
        let mut seen = 0;
        for i in first[p]..first[p + 1] {
            if mark[race[i]] != 2 * p {
                mark[race[i]] = 2 * p;
                seen += 1;
            }
            head[i] = seen;
        }
        whole[p] = seen;
        seen = 0;
        for i in (first[p]..first[p + 1]).rev() {
            if mark[race[i]] != 2 * p + 1 {
                mark[race[i]] = 2 * p + 1;
                seen += 1;
            }
            tail[i] = seen;
        }
    }
    // sparse table of the largest whole piece over ranges of pieces
    let mut table = vec![whole];
    let mut step = 1;
    while 2 * step <= pieces {
        let last = table.last().unwrap();
        let row: Vec<usize> =
            (0..pieces - 2 * step + 1).map(|i| last[i].max(last[i + step])).collect();
        table.push(row);
        step *= 2;
    }
    let largest = |lo: usize, hi: usize| -> usize {
        // the largest whole piece among pieces lo..hi - 1
        if lo >= hi {
            return 0;
        }
        let level = (usize::BITS - 1 - (hi - lo).leading_zeros()) as usize;
        table[level][lo].max(table[level][hi - (1 << level)])
    };
    let m = next();
    let mut answer = vec![0usize; m];
    let mut inside: Vec<(usize, usize, usize)> = Vec::new(); // (right, left, tourist)
    for t in 0..m {
        let (low, high) = (next(), next());
        let lo = dist.partition_point(|&x| x < low);
        let hi_end = dist.partition_point(|&x| x <= high);
        if lo >= hi_end {
            continue;
        }
        let hi = hi_end - 1;
        if piece[lo] == piece[hi] {
            inside.push((hi, lo, t));
        } else {
            answer[t] = tail[lo].max(head[hi]).max(largest(piece[lo] + 1, piece[hi]));
        }
    }
    // distinct races in a range: going right, count each race only at its
    // latest planet, in a Fenwick tree
    inside.sort_unstable();
    let mut tree = vec![0i64; n + 1];
    let mut latest = vec![usize::MAX; s + 1];
    let mut j = 0;
    for i in 0..n {
        if latest[race[i]] != usize::MAX {
            let mut k = latest[race[i]] + 1;
            while k <= n {
                tree[k] -= 1;
                k += k & k.wrapping_neg();
            }
        }
        latest[race[i]] = i;
        let mut k = i + 1;
        while k <= n {
            tree[k] += 1;
            k += k & k.wrapping_neg();
        }
        while j < inside.len() && inside[j].0 == i {
            let (_, lo, t) = inside[j];
            let mut total = 0i64;
            let mut k = i + 1;
            while k > 0 {
                total += tree[k];
                k -= k & k.wrapping_neg();
            }
            k = lo;
            while k > 0 {
                total -= tree[k];
                k -= k & k.wrapping_neg();
            }
            answer[t] = total as usize;
            j += 1;
        }
    }
    let out: Vec<String> = answer.iter().map(|a| a.to_string()).collect();
    println!("{}", out.join("\n"));
}
