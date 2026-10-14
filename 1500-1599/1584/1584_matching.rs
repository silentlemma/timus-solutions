use std::io::{self, Read};

const CORNERS: i32 = 4; // cells in a group of mirror positions
const INF: i32 = 1 << 29;
const LETTERS: usize = 26;

/// The least total cost of giving each row its own column of a square
/// matrix, by the potentials method in O(n^3).
fn hungarian(cost: &[Vec<i32>]) -> i32 {
    let n = cost.len();
    let (mut u, mut v) = (vec![0; n + 1], vec![0; n + 1]);
    let (mut owner, mut prev) = (vec![0usize; n + 1], vec![0usize; n + 1]);
    for row in 1..=n {
        owner[0] = row;
        let mut col0 = 0;
        let mut least = vec![INF; n + 1];
        let mut used = vec![false; n + 1];
        while owner[col0] != 0 {
            used[col0] = true;
            let r = owner[col0];
            let (mut delta, mut col1) = (INF, 0);
            for c in 1..=n {
                if used[c] {
                    continue;
                }
                let reduced = cost[r - 1][c - 1] - u[r] - v[c];
                if reduced < least[c] {
                    least[c] = reduced;
                    prev[c] = col0;
                }
                if least[c] < delta {
                    delta = least[c];
                    col1 = c;
                }
            }
            for c in 0..=n {
                if used[c] {
                    u[owner[c]] += delta;
                    v[c] -= delta;
                } else {
                    least[c] -= delta;
                }
            }
            col0 = col1;
        }
        while col0 != 0 {
            let col1 = prev[col0];
            owner[col0] = owner[col1];
            col0 = col1;
        }
    }
    -v[0]
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let m: usize = words.next().unwrap().parse().unwrap();
    let grid: Vec<&[u8]> = words.take(n).map(|w| w.as_bytes()).collect();
    // every row and column symmetric means the four mirror images of a cell
    // hold one kind of statue; each group then gets one kind
    let mut groups = Vec::new();
    for i in 0..n / 2 {
        for j in 0..m / 2 {
            groups.push([
                grid[i][j],
                grid[i][m - 1 - j],
                grid[n - 1 - i][j],
                grid[n - 1 - i][m - 1 - j],
            ]);
        }
    }
    // a kind with c statues fills c / 4 groups; one column per such place
    let mut count = [0i32; LETTERS];
    for row in &grid {
        for &c in row.iter() {
            count[(c - b'a') as usize] += 1;
        }
    }
    let mut slots = Vec::new();
    for (k, &c) in count.iter().enumerate() {
        for _ in 0..c / CORNERS {
            slots.push(b'a' + k as u8);
        }
    }
    // a statue not already in place is carried once, and a cycle of k statues
    // takes k carries, so the answer is the number of statues that change
    let cost: Vec<Vec<i32>> = groups
        .iter()
        .map(|g| {
            slots
                .iter()
                .map(|&k| CORNERS - g.iter().filter(|&&c| c == k).count() as i32)
                .collect()
        })
        .collect();
    println!("{}", hungarian(&cost));
}
