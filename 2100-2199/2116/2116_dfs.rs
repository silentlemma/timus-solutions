use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: u64 = tokens.next().unwrap().parse().unwrap();
    let a: i32 = tokens.next().unwrap().parse().unwrap();
    let b: i32 = tokens.next().unwrap().parse().unwrap();

    if b == 0 {
        println!("{}", n * n);
        return;
    }

    let side = n.min((2 * b) as u64) as i32;
    let moves = [
        (a, b),
        (a, -b),
        (-a, b),
        (-a, -b),
        (b, a),
        (b, -a),
        (-b, a),
        (-b, -a),
    ];
    let cell_count = (side * side) as usize;
    let mut seen = vec![false; cell_count];
    let mut stack = Vec::with_capacity(cell_count);
    let mut answer = 0;

    for start in 0..cell_count {
        if seen[start] {
            continue;
        }
        answer += 1;
        seen[start] = true;
        stack.push(start);
        while let Some(cell) = stack.pop() {
            let row = cell as i32 / side;
            let col = cell as i32 % side;
            for &(dr, dc) in &moves {
                let next_row = row + dr;
                let next_col = col + dc;
                if next_row < 0 || next_row >= side || next_col < 0 || next_col >= side {
                    continue;
                }
                let next = (next_row * side + next_col) as usize;
                if !seen[next] {
                    seen[next] = true;
                    stack.push(next);
                }
            }
        }
    }
    println!("{}", answer);
}
