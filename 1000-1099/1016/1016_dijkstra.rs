use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};
use std::io::{self, Read};

const SIZE: usize = 8;
const FACES: usize = 6;
const DIRECTIONS: usize = 4;
const BOTTOM: usize = 4;
// faces in the input order near, far, top, right, bottom, left; a roll in
// direction d puts the face from position SOURCE[d][i] to position i
const STEPS: [(i32, i32); DIRECTIONS] = [(0, 1), (0, -1), (1, 0), (-1, 0)];
const SOURCE: [[usize; FACES]; DIRECTIONS] = [
    [4, 2, 0, 3, 1, 5],
    [2, 4, 1, 3, 0, 5],
    [0, 1, 5, 2, 3, 4],
    [0, 1, 3, 4, 5, 2],
];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let tokens: Vec<&str> = input.split_ascii_whitespace().collect();
    let cell = |s: &str| {
        let b = s.as_bytes();
        ((b[0] - b'a') as usize, (b[1] - b'1') as usize)
    };
    let (start, end) = (cell(tokens[0]), cell(tokens[1]));
    let value: Vec<u64> = tokens[2..2 + FACES]
        .iter()
        .map(|t| t.parse().unwrap())
        .collect();

    // the 24 orientations: which original face is at each position
    let identity: [usize; FACES] = std::array::from_fn(|i| i);
    let mut orient = vec![identity];
    let mut id = HashMap::from([(identity, 0)]);
    let mut next: Vec<[usize; DIRECTIONS]> = Vec::new();
    let mut o = 0;
    while o < orient.len() {
        let mut step = [0; DIRECTIONS];
        for (d, src) in SOURCE.iter().enumerate() {
            let r: [usize; FACES] = std::array::from_fn(|i| orient[o][src[i]]);
            let k = *id.entry(r).or_insert(orient.len());
            if k == orient.len() {
                orient.push(r);
            }
            step[d] = k;
        }
        next.push(step);
        o += 1;
    }

    // Dijkstra over (cell, orientation); a state costs its bottom face
    let m = orient.len();
    let state = |x: usize, y: usize, o: usize| (x * SIZE + y) * m + o;
    let mut dist = vec![u64::MAX; SIZE * SIZE * m];
    let mut prev = vec![usize::MAX; SIZE * SIZE * m];
    let first = state(start.0, start.1, 0);
    dist[first] = value[BOTTOM];
    let mut heap = BinaryHeap::from([Reverse((value[BOTTOM], first))]);
    while let Some(Reverse((d, s))) = heap.pop() {
        if d > dist[s] {
            continue;
        }
        let (o, x, y) = (s % m, s / m / SIZE, s / m % SIZE);
        for (k, &(dx, dy)) in STEPS.iter().enumerate() {
            let (nx, ny) = (x as i32 + dx, y as i32 + dy);
            if nx < 0 || ny < 0 || nx >= SIZE as i32 || ny >= SIZE as i32 {
                continue;
            }
            let no = next[o][k];
            let ns = state(nx as usize, ny as usize, no);
            let nd = d + value[orient[no][BOTTOM]];
            if nd < dist[ns] {
                dist[ns] = nd;
                prev[ns] = s;
                heap.push(Reverse((nd, ns)));
            }
        }
    }

    let best = (0..m)
        .map(|o| state(end.0, end.1, o))
        .min_by_key(|&s| dist[s])
        .unwrap();
    let mut route = Vec::new();
    let mut s = best;
    while s != usize::MAX {
        let c = s / m;
        route.push(format!(
            "{}{}",
            (b'a' + (c / SIZE) as u8) as char,
            c % SIZE + 1
        ));
        s = prev[s];
    }
    route.reverse();
    println!("{} {}", dist[best], route.join(" "));
}
