use std::io::{self, Read};

const DEGREE: usize = 3;

fn real_map(w: usize, h: usize, lines: &[Vec<u8>]) -> bool {
    let mut adj: Vec<Vec<(usize, usize)>> = vec![Vec::new(); w * h];
    let mut edges = 0;
    for (r, line) in lines.iter().enumerate() {
        for (c, &ch) in line.iter().enumerate() {
            if (r % 2 == 0 && c % 2 == 0) || ch == b' ' {
                continue;
            }
            // the symbol must fit its gap: - between columns, | between rows, \ or / across
            let (dr, dc): (usize, isize) = match (r % 2, c % 2, ch) {
                (0, _, b'-') => (0, 1),
                (_, 0, b'|') => (1, 0),
                (1, 1, b'\\') => (1, 1),
                (1, 1, b'/') => (1, -1),
                _ => return false,
            };
            let a = (r - dr) / 2 * w + ((c as isize - dc) / 2) as usize;
            let b = ((a + dr * w) as isize + dc) as usize;
            adj[a].push((b, edges));
            adj[b].push((a, edges));
            edges += 1;
        }
    }
    if adj.iter().any(|v| v.len() != DEGREE) {
        return false;
    }
    // iterative low-link search: a tree edge to v is a bridge if low[v] > tin[parent]
    let mut tin = vec![usize::MAX; w * h];
    let mut low = vec![0usize; w * h];
    tin[0] = 0;
    let mut timer = 0;
    let mut stack: Vec<(usize, usize, usize)> = vec![(0, usize::MAX, 0)];
    while let Some(&(v, via, k)) = stack.last() {
        if k < adj[v].len() {
            stack.last_mut().unwrap().2 += 1;
            let (u, e) = adj[v][k];
            if e == via {
                continue;
            }
            if tin[u] == usize::MAX {
                timer += 1;
                tin[u] = timer;
                low[u] = timer;
                stack.push((u, e, 0));
            } else {
                low[v] = low[v].min(tin[u]);
            }
            continue;
        }
        stack.pop();
        if let Some(&(p, _, _)) = stack.last() {
            low[p] = low[p].min(low[v]);
            if low[v] > tin[p] {
                return false;
            }
        }
    }
    tin.iter().all(|&t| t != usize::MAX)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.split('\n');
    let head: Vec<usize> = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (m, n) = (head[0], head[1]);
    let picture: Vec<Vec<u8>> = (0..n)
        .map(|_| {
            let line = lines.next().unwrap_or("").trim_end_matches('\r').as_bytes();
            let mut row = vec![b' '; m];
            for (c, &ch) in line.iter().take(m).enumerate() {
                row[c] = ch;
            }
            row
        })
        .collect();
    let ok = real_map((m + 1) / 2, (n + 1) / 2, &picture);
    println!("{}", if ok { "Island world" } else { "Just a picture" });
}
