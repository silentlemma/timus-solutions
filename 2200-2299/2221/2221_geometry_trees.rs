use std::io::{self, Read};

#[derive(Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
    id: usize,
}

fn chain_sizes(
    p: &[Point],
    left: &[usize],
    right: &[usize],
    order: &[usize],
    size: &[usize],
    turn: i64,
) -> Vec<usize> {
    let n = p.len();
    let mut head = vec![n; n + 1];
    let mut tail = vec![n; n + 1];
    let mut count = vec![0; n + 1];
    let mut previous = vec![n; n];
    let mut following = vec![n; n];
    for &v in order.iter().rev() {
        let a = left[v];
        let b = right[v];
        let forward = size[a] >= size[b];
        let (base, small, back, ahead, sign) = if forward {
            (a, b, &mut previous, &mut following, turn)
        } else {
            (b, a, &mut following, &mut previous, -turn)
        };
        let (mut start, mut end, other) = if forward {
            (head[base], tail[base], head[small])
        } else {
            (tail[base], head[base], tail[small])
        };
        let mut length = count[base];
        let mut c = v;
        // Reuse the larger subtree's chain and insert from its nearer end.
        while c != n {
            let next = if c == v { other } else { ahead[c] };
            while length >= 2 {
                let a = back[end];
                let cross = (p[end].x - p[a].x) * (p[c].y - p[a].y)
                    - (p[end].y - p[a].y) * (p[c].x - p[a].x);
                if cross * sign > 0 {
                    break;
                }
                end = a;
                length -= 1;
            }
            if length != 0 {
                ahead[end] = c;
            } else {
                start = c;
            }
            back[c] = end;
            ahead[c] = n;
            end = c;
            length += 1;
            c = next;
        }
        head[v] = if forward { start } else { end };
        tail[v] = if forward { end } else { start };
        count[v] = length;
    }
    count
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut p = Vec::with_capacity(n);
    for id in 0..n {
        p.push(Point {
            x: words.next().unwrap().parse().unwrap(),
            y: words.next().unwrap().parse().unwrap(),
            id,
        });
    }
    p.sort_unstable_by_key(|point| point.x);
    let mut left = vec![n; n];
    let mut right = vec![n; n];
    let mut stack: Vec<usize> = Vec::with_capacity(n);
    for v in 0..n {
        let mut last = n;
        while let Some(&a) = stack.last() {
            if p[a].y > p[v].y {
                break;
            }
            last = stack.pop().unwrap();
        }
        left[v] = last;
        if let Some(&a) = stack.last() {
            right[a] = v;
        }
        stack.push(v);
    }
    let root = stack[0];
    stack.clear();
    stack.push(root);
    let mut order = Vec::with_capacity(n);
    while let Some(v) = stack.pop() {
        order.push(v);
        if left[v] != n {
            stack.push(left[v]);
        }
        if right[v] != n {
            stack.push(right[v]);
        }
    }
    let mut size = vec![0; n + 1];
    for &v in order.iter().rev() {
        size[v] = size[left[v]] + size[right[v]] + 1;
    }
    let lower = chain_sizes(&p, &left, &right, &order, &size, 1);
    let upper = chain_sizes(&p, &left, &right, &order, &size, -1);
    let mut answer = vec![0; n];
    for v in 0..n {
        answer[p[v].id] = (lower[v] + upper[v]).saturating_sub(2).max(1);
    }
    let output: String = answer.iter().map(|value| format!("{}\n", value)).collect();
    print!("{}", output);
}
