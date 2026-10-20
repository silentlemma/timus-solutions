use std::io::{self, Read};

fn cell(board: &[i64], n: i32, m: i32, row: i32, col: i32) -> i64 {
    if row < 0 || row >= n || col < 0 || col >= m {
        0
    } else {
        board[(row * m + col) as usize]
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: i32 = tokens.next().unwrap().parse().unwrap();
    let m: i32 = tokens.next().unwrap().parse().unwrap();
    let board: Vec<i64> = (0..n * m)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let s = tokens.next().unwrap().as_bytes();
    let directions = b"RDLU";
    let steps = [(0, 1), (1, 0), (0, -1), (-1, 0)];
    let length = s.len();
    let mut x = vec![0; length + 1];
    let mut y = vec![0; length + 1];
    let mut cost = vec![0; length + 1];
    cost[0] = board[0];
    for i in 0..length {
        let d = directions.iter().position(|&c| c == s[i]).unwrap();
        x[i + 1] = x[i] + steps[d].0;
        y[i + 1] = y[i] + steps[d].1;
        cost[i + 1] = cell(&board, n, m, x[i + 1], y[i + 1]);
    }
    let (mut best, mut source, mut target) = (0, 0, 0);
    for (d, &(dx, dy)) in steps.iter().enumerate() {
        let (mut left, mut right, mut left_max, mut right_max) = (0, 0, 0, 0);
        let mut left_at = 0;
        let mut right_at = None;
        for i in 0..length {
            // Prefix maxima select endpoints of the translated path interval.
            if left > left_max {
                left_max = left;
                left_at = i;
            }
            left += cell(&board, n, m, x[i] + dx, y[i] + dy) - cost[i + 1];
            if s[i] == directions[d] && left - left_max < best {
                best = left - left_max;
                source = i;
                target = left_at;
            }
            if s[i] == directions[d] && (right_at.is_none() || right > right_max) {
                right_max = right;
                right_at = Some(i);
            }
            right += cell(&board, n, m, x[i + 1] - dx, y[i + 1] - dy) - cost[i];
            if let Some(at) = right_at {
                if right - right_max < best {
                    best = right - right_max;
                    source = at;
                    target = i;
                }
            }
        }
    }
    let mut answer = s.to_vec();
    let moved = answer.remove(source);
    answer.insert(target, moved);
    println!("{}", String::from_utf8(answer).unwrap());
}
