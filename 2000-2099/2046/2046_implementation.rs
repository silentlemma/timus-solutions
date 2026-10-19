use std::io::{self, Read};

const WIDTH: usize = 10;
const ROWS: usize = 4;
const COLUMNS: usize = 3;
const DAYS: [&str; COLUMNS] = ["Tuesday", "Thursday", "Saturday"];

fn wrap(name: &str) -> Vec<String> {
    let mut lines = vec![String::new()];
    for word in name.split_whitespace() {
        let last = lines.last_mut().unwrap();
        if last.is_empty() {
            last.push_str(word);
        } else if last.len() + 1 + word.len() <= WIDTH {
            last.push(' ');
            last.push_str(word);
        } else {
            lines.push(word.to_string());
        }
    }
    lines
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let n: usize = lines.next().unwrap().parse().unwrap();
    let mut grid = vec![vec![Vec::<String>::new(); DAYS.len()]; ROWS];
    for _ in 0..n {
        let name = lines.next().unwrap();
        let mut slot = lines.next().unwrap().split_whitespace();
        let day = slot.next().unwrap();
        let lesson: usize = slot.next().unwrap().parse().unwrap();
        let column = DAYS.iter().position(|&value| value == day).unwrap();
        grid[lesson - 1][column] = wrap(name);
    }
    let border = format!("+{}", format!("{}+", "-".repeat(WIDTH)).repeat(DAYS.len()));
    let mut output = format!("{}\n", border);
    for row in grid {
        let height = row.iter().map(Vec::len).max().unwrap().max(1);
        for level in 0..height {
            output.push('|');
            for cell in &row {
                let line = cell.get(level).map(String::as_str).unwrap_or("");
                output.push_str(line);
                output.push_str(&" ".repeat(WIDTH - line.len()));
                output.push('|');
            }
            output.push('\n');
        }
        output.push_str(&border);
        output.push('\n');
    }
    print!("{}", output);
}
