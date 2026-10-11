use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut number = || words.next().unwrap().parse::<usize>().unwrap();
    let (w, h, x, y, d) = (number(), number(), number(), number(), number());
    let rows: Vec<&[u8]> = words.take(h).map(|row| row.as_bytes()).collect();
    let mut open = vec![false; w * h];
    for r in 0..h {
        for c in 0..w {
            open[r * w + c] = rows[r][c] != b'#';
        }
    }
    // water reaches a cell that has a way to the surface without going down,
    // so search back from the top row: down, left and right
    let mut wet = vec![false; w * h];
    let mut stack: Vec<usize> = (0..w).filter(|&c| open[c]).collect();
    for &c in &stack {
        wet[c] = true;
    }
    while let Some(cell) = stack.pop() {
        let (r, c) = (cell / w, cell % w);
        let next = [
            (r + 1 < h).then(|| cell + w),
            (c > 0).then(|| cell - 1),
            (c + 1 < w).then(|| cell + 1),
        ];
        for n in next.into_iter().flatten() {
            if open[n] && !wet[n] {
                wet[n] = true;
                stack.push(n);
            }
        }
    }
    // label: moves made under water since the last breath; an air pocket
    // resets it to 0, and no stretch under water may take more than D moves
    let start = (h - y) * w + (x - 1);
    let mut label = vec![d + 1; w * h];
    let mut buckets: Vec<Vec<usize>> = vec![Vec::new(); d + 1];
    label[start] = 0;
    buckets[0].push(start);
    let mut level = 0;
    while level <= d {
        let cell = match buckets[level].pop() {
            Some(cell) => cell,
            None => {
                level += 1;
                continue;
            }
        };
        let here = label[cell];
        if here != level {
            continue;
        }
        let (r, c) = (cell / w, cell % w);
        if r == 0 && here + 1 <= d {
            println!("Can be rescued by himself");
            return;
        }
        let next = [
            (r > 0).then(|| cell - w),
            (r + 1 < h).then(|| cell + w),
            (c > 0).then(|| cell - 1),
            (c + 1 < w).then(|| cell + 1),
        ];
        for n in next.into_iter().flatten() {
            if !open[n] {
                continue;
            }
            let nl = if wet[n] {
                here + 1
            } else if wet[cell] && here + 1 > d {
                continue;
            } else {
                0
            };
            if nl <= d && nl < label[n] {
                label[n] = nl;
                buckets[nl].push(n);
                level = level.min(nl);
            }
        }
    }
    println!("Rescue operation required");
}
