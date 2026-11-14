use std::io::{self, Read, Write};

const MAX_LENGTH: usize = 10_000;

fn pivot(length: usize, path: &[bool]) -> usize {
    let mut start = 0;
    let mut gaps = length + 1;
    for &right in path {
        let left = gaps / 2;
        if right {
            start += left;
            gaps -= left;
        } else {
            gaps = left;
        }
    }
    start + gaps / 2 - 1
}

fn first_at_least(mut lo: usize, mut hi: usize, index: usize, path: &[bool]) -> usize {
    while lo < hi {
        let middle = lo + (hi - lo) / 2;
        if pivot(middle, path) < index {
            lo = middle + 1;
        } else {
            hi = middle;
        }
    }
    lo
}

fn search(
    lo: usize,
    hi: usize,
    target: usize,
    path: &mut [bool],
    depth: usize,
    runs: &mut Vec<(usize, usize)>,
) {
    if lo == hi {
        return;
    }
    // Along a fixed path the pivot never moves left as the array grows.
    let first = first_at_least(lo, hi, target, &path[..depth]);
    let after = first_at_least(first, hi, target + 1, &path[..depth]);
    if depth == path.len() {
        if first < after {
            match runs.last_mut() {
                Some(last) if last.1 + 1 == first => last.1 = after - 1,
                _ => runs.push((first, after - 1)),
            }
        }
        return;
    }
    path[depth] = true;
    search(lo, first, target, path, depth + 1, runs);
    path[depth] = false;
    search(after, hi, target, path, depth + 1, runs);
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input.split_ascii_whitespace();
    let target = values.next().unwrap().parse::<usize>().unwrap();
    let steps = values.next().unwrap().parse::<usize>().unwrap();
    let mut runs = Vec::new();
    let mut path = vec![false; steps - 1];
    search(target + 1, MAX_LENGTH + 1, target, &mut path, 0, &mut runs);
    let mut output = io::BufWriter::new(io::stdout().lock());
    writeln!(output, "{}", runs.len()).unwrap();
    for (first, last) in runs {
        writeln!(output, "{} {}", first, last).unwrap();
    }
}
