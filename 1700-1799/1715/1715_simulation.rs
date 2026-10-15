use std::io::{self, Read};

const COLORS: &[u8] = b"BGRWY";
const EMPTY: u8 = b'.';

// the largest figure of the main colour or of the others; ties go to the
// figure holding the lowest ball, then the leftmost of the lowest balls
fn best_figure(board: &[u8], n: usize, m: usize, main: u8, take_main: bool) -> Option<Vec<usize>> {
    let mut seen = vec![false; n * m];
    let mut best: Option<(Vec<usize>, usize)> = None;
    for start in 0..n * m {
        let color = board[start];
        if seen[start] || color == EMPTY || (color == main) != take_main {
            continue;
        }
        seen[start] = true;
        let mut cells = vec![start];
        let mut low = start;
        let mut k = 0;
        while k < cells.len() {
            let v = cells[k];
            k += 1;
            let (r, c) = (v / m, v % m);
            if r > low / m || (r == low / m && c < low % m) {
                low = v;
            }
            let mut near = Vec::new();
            if r > 0 {
                near.push(v - m);
            }
            if r + 1 < n {
                near.push(v + m);
            }
            if c > 0 {
                near.push(v - 1);
            }
            if c + 1 < m {
                near.push(v + 1);
            }
            for w in near {
                if !seen[w] && board[w] == color {
                    seen[w] = true;
                    cells.push(w);
                }
            }
        }
        if cells.len() < 2 {
            continue;
        }
        let better = match &best {
            None => true,
            Some((b, b_low)) => {
                cells.len() > b.len()
                    || (cells.len() == b.len()
                        && (low / m > b_low / m || (low / m == b_low / m && low % m < b_low % m)))
            }
        };
        if better {
            best = Some((cells, low));
        }
    }
    best.map(|(cells, _)| cells)
}

fn remove(board: &mut Vec<u8>, n: usize, m: usize, cells: &[usize]) -> i64 {
    for &v in cells {
        board[v] = EMPTY;
    }
    // balls fall down, then empty columns close up to the left
    let mut columns: Vec<Vec<u8>> = Vec::new();
    for c in 0..m {
        let column: Vec<u8> = (0..n).map(|r| board[r * m + c]).filter(|&b| b != EMPTY).collect();
        if !column.is_empty() {
            let mut padded = vec![EMPTY; n - column.len()];
            padded.extend(column);
            columns.push(padded);
        }
    }
    for c in 0..m {
        for r in 0..n {
            board[r * m + c] = if c < columns.len() { columns[c][r] } else { EMPTY };
        }
    }
    let k = cells.len() as i64;
    k * (k - 1)
}

fn play(start: &[u8], n: usize, m: usize, main: u8) -> i64 {
    let mut board = start.to_vec();
    let mut score = 0;
    loop {
        while let Some(cells) = best_figure(&board, n, m, main, false) {
            score += remove(&mut board, n, m, &cells);
        }
        match best_figure(&board, n, m, main, true) {
            Some(cells) => score += remove(&mut board, n, m, &cells),
            None => return score,
        }
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let m: usize = words.next().unwrap().parse().unwrap();
    let board: Vec<u8> = words.take(n).flat_map(|w| w.bytes()).collect();
    let mut out = String::new();
    for &color in COLORS {
        if board.contains(&color) {
            out.push_str(&format!("{}: {}\n", color as char, play(&board, n, m, color)));
        }
    }
    print!("{}", out);
}
