use std::io::{self, Read, Write};

const IDS: usize = 40001;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap();
    let mut children: Vec<Vec<i64>> = vec![Vec::new(); IDS];
    let mut root = -1;
    for _ in 0..n {
        let (node, parent) = (it.next().unwrap(), it.next().unwrap());
        if parent < 0 {
            root = node;
        } else {
            children[parent as usize].push(node);
        }
    }
    // enter[v] and leave[v] bound the times of the whole subtree of v
    let mut enter = vec![-1i64; IDS];
    let mut leave = vec![-1i64; IDS];
    let (mut clock, mut stack) = (0, vec![root]);
    while let Some(node) = stack.pop() {
        if node >= 0 {
            enter[node as usize] = clock;
            clock += 1;
            stack.push(!node);
            stack.extend(children[node as usize].iter());
        } else {
            leave[!node as usize] = clock;
        }
    }
    let queries = it.next().unwrap();
    let mut out = String::new();
    for _ in 0..queries {
        let (a, b) = (it.next().unwrap() as usize, it.next().unwrap() as usize);
        let inside =
            |x: usize, y: usize| enter[x] >= 0 && enter[x] <= enter[y] && enter[y] < leave[x];
        out.push_str(if inside(a, b) {
            "1\n"
        } else if inside(b, a) {
            "2\n"
        } else {
            "0\n"
        });
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
