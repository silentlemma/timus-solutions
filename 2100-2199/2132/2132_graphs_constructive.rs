use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write as IoWrite};

const MAX_VERTEX: usize = 100000;
const ROOT_PARENT: usize = usize::MAX;

fn emit(output: &mut String, first: usize, middle: usize, last: usize) {
    writeln!(output, "{} {} {}", first, middle, last).unwrap();
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let mut edges = Vec::new();
    let mut degree = vec![0; MAX_VERTEX + 1];
    let mut largest = 0;
    while let Some(token) = tokens.next() {
        let first: usize = token.parse().unwrap();
        let second: usize = tokens.next().unwrap().parse().unwrap();
        edges.push((first, second));
        degree[first] += 1;
        degree[second] += 1;
        largest = largest.max(first).max(second);
    }

    let mut offset = vec![0; largest + 2];
    for vertex in 1..=largest {
        offset[vertex + 1] = offset[vertex] + degree[vertex];
    }
    let mut next = offset.clone();
    let mut adjacent = vec![0; edges.len() * 2];
    for &(first, second) in &edges {
        adjacent[next[first]] = second;
        next[first] += 1;
        adjacent[next[second]] = first;
        next[second] += 1;
    }

    let mut parent = vec![0; largest + 1];
    let mut rank = vec![0; largest + 1];
    let mut stack = Vec::new();
    let mut order = Vec::new();
    for root in 1..=largest {
        if degree[root] == 0 || parent[root] != 0 {
            continue;
        }
        parent[root] = ROOT_PARENT;
        stack.push(root);
        while let Some(vertex) = stack.pop() {
            rank[vertex] = order.len();
            order.push(vertex);
            for &neighbor in &adjacent[offset[vertex]..offset[vertex + 1]] {
                if parent[neighbor] == 0 {
                    parent[neighbor] = vertex;
                    stack.push(neighbor);
                }
            }
        }
    }

    let mut output = format!("{}\n", edges.len() / 2);
    let mut used_parent = vec![false; largest + 1];
    for &vertex in order.iter().rev() {
        let mut pending = 0;
        for &neighbor in &adjacent[offset[vertex]..offset[vertex + 1]] {
            if neighbor == parent[vertex] {
                continue;
            }
            if parent[neighbor] == vertex {
                if used_parent[neighbor] {
                    continue;
                }
            } else if rank[neighbor] > rank[vertex] {
                continue;
            }
            if pending == 0 {
                pending = neighbor;
            } else {
                emit(&mut output, pending, vertex, neighbor);
                pending = 0;
            }
        }
        if pending != 0 {
            if parent[vertex] == ROOT_PARENT {
                println!("-1");
                return;
            }
            emit(&mut output, pending, vertex, parent[vertex]);
            used_parent[vertex] = true;
        }
    }

    let stdout = io::stdout();
    let mut writer = io::BufWriter::new(stdout.lock());
    writer.write_all(output.as_bytes()).unwrap();
}
