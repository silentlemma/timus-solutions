use std::cmp::{Ordering, Reverse};
use std::collections::BinaryHeap;
use std::fmt::Write as _;
use std::io::{self, Read};

const FAR: i64 = 1 << 62;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut xs = vec![0i64; n];
    let mut ys = vec![0i64; n];
    for i in 0..n {
        xs[i] = it.next().unwrap();
        ys[i] = it.next().unwrap();
    }
    let m = it.next().unwrap() as usize;
    // half-edge 2i runs from ends[i] to tips[i], 2i + 1 back; pipe m is an
    // extra edge from the source, leaving to the left, round the outside to
    // the sink, arriving from the right
    let mut ends = vec![0usize; m + 1];
    let mut tips = vec![n - 1; m + 1];
    let mut caps = vec![0i64; m];
    for i in 0..m {
        ends[i] = it.next().unwrap() as usize - 1;
        tips[i] = it.next().unwrap() as usize - 1;
        caps[i] = it.next().unwrap();
    }
    let halves = 2 * m + 2;
    let mut origin = vec![0usize; halves];
    let mut dx = vec![0i64; halves];
    let mut dy = vec![0i64; halves];
    for i in 0..=m {
        let (a, b) = (ends[i], tips[i]);
        origin[2 * i] = a;
        origin[2 * i + 1] = b;
        dx[2 * i] = xs[b] - xs[a];
        dy[2 * i] = ys[b] - ys[a];
        dx[2 * i + 1] = -dx[2 * i];
        dy[2 * i + 1] = -dy[2 * i];
    }
    dx[2 * m] = -1;
    dy[2 * m] = 0;
    dx[2 * m + 1] = 1;
    dy[2 * m + 1] = 0;
    let mut around: Vec<Vec<usize>> = vec![Vec::new(); n];
    for h in 0..halves {
        around[origin[h]].push(h);
    }
    // counterclockwise from the +x axis, compared exactly
    let low = |h: usize| dy[h] < 0 || (dy[h] == 0 && dx[h] < 0);
    let mut pos = vec![0usize; halves];
    for list in around.iter_mut() {
        list.sort_by(|&g, &h| {
            low(g).cmp(&low(h)).then_with(|| {
                let cross = dx[g] * dy[h] - dy[g] * dx[h];
                if cross > 0 {
                    Ordering::Less
                } else if cross < 0 {
                    Ordering::Greater
                } else {
                    Ordering::Equal
                }
            })
        });
        for (k, &h) in list.iter().enumerate() {
            pos[h] = k;
        }
    }
    // faces: after arriving at a vertex, leave by the next edge clockwise
    let mut face = vec![usize::MAX; halves];
    let mut faces = 0;
    for h in 0..halves {
        if face[h] != usize::MAX {
            continue;
        }
        let mut g = h;
        while face[g] == usize::MAX {
            face[g] = faces;
            let list = &around[origin[g ^ 1]];
            let k = pos[g ^ 1];
            g = list[if k == 0 { list.len() - 1 } else { k - 1 }];
        }
        faces += 1;
    }
    // the minimum cut is the shortest path between the two faces next to
    // the extra edge, with pipe capacities as lengths
    let mut links: Vec<Vec<(usize, i64)>> = vec![Vec::new(); faces];
    for i in 0..m {
        let (a, b) = (face[2 * i], face[2 * i + 1]);
        links[a].push((b, caps[i]));
        links[b].push((a, caps[i]));
    }
    let mut dist = vec![FAR; faces];
    let start = face[2 * m];
    dist[start] = 0;
    let mut heap = BinaryHeap::new();
    heap.push(Reverse((0i64, start)));
    while let Some(Reverse((d, f))) = heap.pop() {
        if d > dist[f] {
            continue;
        }
        for &(g, c) in &links[f] {
            if d + c < dist[g] {
                dist[g] = d + c;
                heap.push(Reverse((d + c, g)));
            }
        }
    }
    // the flow from ends[i] to tips[i] is the difference of the distances
    // of the faces on its two sides
    let mut flow = vec![0i64; m];
    let mut total = 0i64;
    for i in 0..m {
        let (left, right) = (dist[face[2 * i]], dist[face[2 * i + 1]]);
        if left != FAR && right != FAR {
            flow[i] = right - left;
        }
        if ends[i] == 0 {
            total += flow[i];
        } else if tips[i] == 0 {
            total -= flow[i];
        }
    }
    let sign = if total >= 0 { 1 } else { -1 };
    let mut out = String::new();
    writeln!(out, "{}", total * sign).unwrap();
    for i in 0..m {
        let f = flow[i] * sign;
        if f >= 0 {
            writeln!(out, "{} {} {}", ends[i] + 1, tips[i] + 1, f).unwrap();
        } else {
            writeln!(out, "{} {} {}", tips[i] + 1, ends[i] + 1, -f).unwrap();
        }
    }
    print!("{}", out);
}
