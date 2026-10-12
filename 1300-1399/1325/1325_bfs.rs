use std::io::{self, Read};

const WALL: u8 = b'0';
const HEADER: usize = 6; // numbers before the plan

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut number = || words.next().unwrap().parse::<usize>().unwrap();
    let (n, m) = (number(), number());
    let (sr, sc, tr, tc) = (number(), number(), number(), number());
    let width = m + 2;
    // the plan with a frame of walls, as one flat array
    let mut grid = vec![WALL; width];
    let rows: Vec<&str> = input
        .split_ascii_whitespace()
        .skip(HEADER)
        .take(n)
        .collect();
    for row in rows {
        let mut line = row.as_bytes().to_vec();
        line.resize(m, WALL);
        grid.push(WALL);
        grid.extend_from_slice(&line);
        grid.push(WALL);
    }
    grid.extend(vec![WALL; width]);
    let mut steps = vec![-1i64; grid.len()];
    let mut seeded = vec![-1i64; grid.len()]; // the layer that last took the cell as a seed
    let w = width as i64;
    let moves: Vec<i64> = [-w - 1, -w, -w + 1, -1, 1, w - 1, w, w + 1].to_vec();
    let (start, target) = (sr * width + sc, tr * width + tc);
    // layer c holds the cells first reached after c changes of shoes, all of
    // the same kind; seeds come in sorted by the number of steps
    let (mut kind, mut changes) = (grid[start], 0i64);
    let mut seeds: Vec<(i64, usize)> = vec![(0, start)];
    while !seeds.is_empty() && steps[target] < 0 {
        let mut later = Vec::new();
        let mut current: Vec<usize> = Vec::new();
        let (mut i, mut level) = (0, seeds[0].0);
        while (i < seeds.len() || !current.is_empty()) && steps[target] < 0 {
            if current.is_empty() && seeds[i].0 > level {
                level = seeds[i].0;
            }
            while i < seeds.len() && seeds[i].0 == level {
                let cell = seeds[i].1;
                i += 1;
                if steps[cell] < 0 {
                    steps[cell] = level;
                    current.push(cell);
                }
            }
            let mut following = Vec::new();
            for &cell in &current {
                for &mv in &moves {
                    let near = (cell as i64 + mv) as usize;
                    if steps[near] >= 0 || grid[near] == WALL {
                        continue;
                    }
                    if grid[near] == kind {
                        steps[near] = level + 1;
                        following.push(near);
                    } else if seeded[near] != changes {
                        seeded[near] = changes;
                        later.push((level + 1, near));
                    }
                }
            }
            current = following;
            level += 1;
        }
        if steps[target] < 0 {
            if let Some(&(_, cell)) = later.first() {
                kind = grid[cell];
            }
            changes += 1;
            seeds = later;
        }
    }
    if steps[target] < 0 {
        println!("0 0");
    } else {
        println!("{} {}", steps[target] + 1, changes);
    }
}
