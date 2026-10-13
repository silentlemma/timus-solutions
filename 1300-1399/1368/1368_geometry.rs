use std::io::{self, Read, Write};

const ENDS: [i64; 2] = [1, 2]; // the first and last rows of a best shape are this narrow

// no k cells have fewer than sqrt(SCALE k - SHIFT) + 2 neighbours
const SCALE: i64 = 8;
const SHIFT: i64 = 4;

fn isqrt(n: i64) -> i64 {
    let mut r = (n as f64).sqrt() as i64;
    while r * r > n {
        r -= 1;
    }
    while (r + 1) * (r + 1) <= n {
        r += 1;
    }
    r
}

fn capped(full: &[i64], cap: i64) -> i64 {
    full.iter().map(|&w| w.min(cap)).sum()
}

/// Row widths of a region of k cells with the smallest fence: with row ends
/// moving by at most one cell per row the fence is two cells per row plus the
/// first and the last row, and no fence is smaller than sqrt(8 k - 4) + 2.
fn widths_for(k: i64) -> Vec<i64> {
    let mut fence = isqrt(SCALE * k - SHIFT - 1) + 1 + 2;
    loop {
        for &first in ENDS.iter() {
            for &last in ENDS.iter() {
                let twice = fence - first - last;
                let rows = twice / 2;
                if twice % 2 != 0 || rows < 1 {
                    continue;
                }
                let full: Vec<i64> = if rows == 1 {
                    if first == last {
                        vec![first]
                    } else {
                        Vec::new()
                    }
                } else {
                    (0..rows)
                        .map(|i| (first + 2 * i).min(last + 2 * (rows - 1 - i)))
                        .collect()
                };
                if full.is_empty() {
                    continue;
                }
                let widest = *full.iter().max().unwrap();
                if capped(&full, widest) < k {
                    continue;
                }
                // cap the widest rows at the smallest level that holds k cells
                let low = full[0].max(full[full.len() - 1]);
                let (mut lo, mut hi) = (low, widest);
                while lo < hi {
                    let mid = (lo + hi) / 2;
                    if capped(&full, mid) < k {
                        lo = mid + 1;
                    } else {
                        hi = mid;
                    }
                }
                let cap = lo;
                let mut widths: Vec<i64> = full.iter().map(|&w| w.min(cap)).collect();
                let extra = (capped(&full, cap) - k) as usize;
                let inner: Vec<usize> = (1..widths.len().saturating_sub(1))
                    .filter(|&i| widths[i] == cap)
                    .collect();
                if cap > low && extra <= inner.len() {
                    for &i in &inner[..extra] {
                        widths[i] -= 1;
                    }
                    return widths;
                }
                if extra == 0 {
                    return widths;
                }
            }
        }
        fence += 1;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let k: i64 = input.trim().parse().unwrap();
    let widths = widths_for(k);
    // place the rows from y = 0 up, the first one starting at x = 0; the ends
    // move by at most one cell, the left one first when the row narrows
    let (mut left, mut right) = (vec![0i64], vec![widths[0] - 1]);
    for &w in &widths[1..] {
        let grow = w - (right[right.len() - 1] - left[left.len() - 1] + 1);
        let dl = if grow == 2 {
            -1
        } else if grow < 0 {
            1
        } else {
            0
        };
        let l = left[left.len() - 1] + dl;
        left.push(l);
        right.push(l + w - 1);
    }
    let top = widths.len() - 1;
    let mut fence: Vec<(i64, i64)> = Vec::new();
    for x in left[0]..=right[0] {
        fence.push((x, -1));
    }
    for y in 0..=top {
        fence.push((right[y] + 1, y as i64));
    }
    for x in (left[top]..=right[top]).rev() {
        fence.push((x, top as i64 + 1));
    }
    for y in (0..=top).rev() {
        fence.push((left[y] - 1, y as i64));
    }
    let mut out = format!("{}\n", fence.len());
    for (x, y) in fence {
        out.push_str(&format!("{} {}\n", x, y));
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
