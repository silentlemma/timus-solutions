use std::io::{self, Read};

fn draw(points: &[(i32, i32)]) -> String {
    let (mut left, mut right, mut lower, mut upper) = (0, 0, 0, 0);
    for &(x, y) in points {
        left = left.min(x);
        right = right.max(x);
        lower = lower.min(y);
        upper = upper.max(y);
    }
    let width = (right - left + 1) as usize;
    let mut grid = vec![vec![b'.'; width]; (upper - lower + 1) as usize];
    for row in &mut grid {
        row[(-left) as usize] = b'|';
    }
    grid[upper as usize].fill(b'-');
    grid[upper as usize][(-left) as usize] = b'+';
    for &(x, y) in points {
        grid[(upper - y) as usize][(x - left) as usize] = b'*';
    }
    let mut output = Vec::new();
    for row in grid {
        output.extend(row);
        output.push(b'\n');
    }
    String::from_utf8(output).unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let size = words.next().unwrap().parse::<usize>().unwrap();
    let points: Vec<(i32, i32)> = (0..size)
        .map(|_| {
            (
                words.next().unwrap().parse().unwrap(),
                words.next().unwrap().parse().unwrap(),
            )
        })
        .collect();
    print!("{}", draw(&points));
}
