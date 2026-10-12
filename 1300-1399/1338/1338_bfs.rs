use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

const SIDES: usize = 4;
// the sides, in the order cars prefer to turn
const SOUTH: usize = 0;
const NORTH: usize = 1;
const WEST: usize = 2;
const EAST: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.split('\n');
    let head: Vec<usize> = lines
        .next()
        .unwrap()
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (w, h) = (head[0], head[1]);
    let width = w + 2;
    // the plan with a frame of buildings, as one flat array
    let rows: Vec<Vec<u8>> = (0..h)
        .map(|_| {
            let mut row = lines
                .next()
                .unwrap_or("")
                .trim_end_matches('\r')
                .as_bytes()
                .to_vec();
            row.resize(w, b'.');
            row
        })
        .collect();
    let mut road = vec![false; width * (h + 2)];
    for r in 0..h {
        for c in 0..w {
            road[(r + 1) * width + c + 1] = rows[r][c] == b'#' || rows[r][c] == b'o';
        }
    }
    // control points numbered from the bottom row up, left to right
    let grid = &rows;
    let points: Vec<usize> = (0..h)
        .rev()
        .flat_map(|r| {
            (0..w)
                .filter(move |&c| grid[r][c] == b'o')
                .map(move |c| (r + 1) * width + c + 1)
        })
        .collect();
    let wi = width as i64;
    let steps: [i64; SIDES] = [wi, -wi, -1, 1]; // south, north, west, east
    let rest: Vec<usize> = lines
        .flat_map(|l| l.split_ascii_whitespace())
        .map(|t| t.parse().unwrap())
        .collect();
    let m = rest.first().copied().unwrap_or(0);
    let mut dist = vec![-1i64; road.len()];
    let mut side = vec![0usize; road.len()];
    let mut out = String::new();
    for number in 1..=m {
        let goal = points[rest[number] - 1];
        dist.iter_mut().for_each(|d| *d = -1);
        dist[goal] = 0;
        let mut order = vec![goal];
        let mut head = 0;
        while head < order.len() {
            let cell = order[head];
            head += 1;
            for &step in &steps {
                let near = (cell as i64 + step) as usize;
                if road[near] && dist[near] < 0 {
                    dist[near] = dist[cell] + 1;
                    order.push(near);
                }
            }
        }
        // every cell inherits the side its car arrives from from the cell it
        // moves to; cells one step away arrive straight from their own side
        for &cell in &order[1..] {
            for (k, &step) in steps.iter().enumerate() {
                let near = (cell as i64 + step) as usize;
                if dist[near] == dist[cell] - 1 {
                    // stepping in one direction onto the goal arrives from the opposite side
                    side[cell] = if near != goal { side[near] } else { k ^ 1 };
                    break;
                }
            }
        }
        let mut counts = [0; SIDES];
        for &p in &points {
            if p != goal && dist[p] > 0 {
                counts[side[p]] += 1;
            }
        }
        writeln!(
            out,
            "Experiment #{}: North: {}, South: {}, East: {}, West: {}",
            number, counts[NORTH], counts[SOUTH], counts[EAST], counts[WEST]
        )
        .unwrap();
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
