use std::io::{self, Read};

struct Scanner {
    data: Vec<u8>,
    position: usize,
}

impl Scanner {
    fn next_usize(&mut self) -> usize {
        while self.position < self.data.len() && self.data[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.data.len() && self.data[self.position].is_ascii_digit() {
            value = value * 10 + usize::from(self.data[self.position] - b'0');
            self.position += 1;
        }
        value
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Scanner { data, position: 0 };
    let n = input.next_usize();
    let m = input.next_usize();
    let x = input.next_usize() as i64;
    let y = input.next_usize() as i64;
    let mut graph = vec![Vec::new(); n];
    let mut reverse = vec![Vec::new(); n];
    for _ in 0..m {
        let from = input.next_usize() - 1;
        let to = input.next_usize() - 1;
        graph[from].push(to);
        reverse[to].push(from);
    }

    let mut seen = vec![false; n];
    let mut next = vec![0; n];
    let mut order = Vec::with_capacity(n);
    let mut stack = Vec::with_capacity(n);
    for start in 0..n {
        if seen[start] {
            continue;
        }
        seen[start] = true;
        stack.push(start);
        while let Some(&vertex) = stack.last() {
            if next[vertex] < graph[vertex].len() {
                let to = graph[vertex][next[vertex]];
                next[vertex] += 1;
                if !seen[to] {
                    seen[to] = true;
                    stack.push(to);
                }
            } else {
                order.push(vertex);
                stack.pop();
            }
        }
    }

    const UNASSIGNED: usize = usize::MAX;
    let mut component = vec![UNASSIGNED; n];
    let mut component_count = 0;
    for &start in order.iter().rev() {
        if component[start] != UNASSIGNED {
            continue;
        }
        component[start] = component_count;
        stack.push(start);
        while let Some(vertex) = stack.pop() {
            for &to in &reverse[vertex] {
                if component[to] == UNASSIGNED {
                    component[to] = component_count;
                    stack.push(to);
                }
            }
        }
        component_count += 1;
    }

    let mut weak_seen = vec![false; n];
    let mut counted = vec![false; component_count];
    let mut answer = 0;
    for start in 0..n {
        if weak_seen[start] {
            continue;
        }
        let mut vertices = 0;
        let mut components = 0;
        weak_seen[start] = true;
        stack.push(start);
        while let Some(vertex) = stack.pop() {
            vertices += 1;
            let id = component[vertex];
            if !counted[id] {
                counted[id] = true;
                components += 1;
            }
            for &to in &graph[vertex] {
                if !weak_seen[to] {
                    weak_seen[to] = true;
                    stack.push(to);
                }
            }
            for &to in &reverse[vertex] {
                if !weak_seen[to] {
                    weak_seen[to] = true;
                    stack.push(to);
                }
            }
        }
        let mut cost = (vertices - 1) * y;
        if x < y {
            cost = ((vertices - components) * y + (components - 1) * x).min(vertices * x);
        }
        answer += cost;
    }
    println!("{}", answer);
}
