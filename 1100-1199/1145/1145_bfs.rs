use std::io::{self, Read};

// breadth-first search; the free cells form a tree, so distances along it
// are the only paths; returns the last cell reached and its distance
fn farthest(free: &[bool], cols: usize, start: usize) -> (usize, i32) {
    let mut dist = vec![-1i32; free.len()];
    let mut queue = vec![start];
    dist[start] = 0;
    let mut head = 0;
    while head < queue.len() {
        let cur = queue[head];
        head += 1;
        for next in [cur + 1, cur - 1, cur + cols, cur - cols] {
            if free[next] && dist[next] < 0 {
                dist[next] = dist[cur] + 1;
                queue.push(next);
            }
        }
    }
    let last = *queue.last().unwrap();
    (last, dist[last])
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input.split_ascii_whitespace();
    let width: usize = tok.next().unwrap().parse().unwrap();
    let height: usize = tok.next().unwrap().parse().unwrap();
    // a border of walls around the maze keeps every neighbour in range
    let cols = width + 2;
    let mut free = vec![false; (height + 2) * cols];
    for r in 1..=height {
        let row = tok.next().unwrap().as_bytes();
        for c in 1..=width {
            free[r * cols + c] = row[c - 1] == b'.';
        }
    }
    let start = free.iter().position(|&f| f).unwrap();
    // the farthest cell from any cell is an end of a longest path
    let (end, _) = farthest(&free, cols, start);
    println!("{}", farthest(&free, cols, end).1);
}
