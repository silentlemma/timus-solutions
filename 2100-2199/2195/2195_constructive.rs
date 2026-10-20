use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};
use std::str::SplitWhitespace;

struct Tree {
    parent: Vec<usize>,
    order: Vec<usize>,
}

fn next_usize(input: &mut SplitWhitespace<'_>) -> usize {
    input.next().unwrap().parse().unwrap()
}

fn read_tree(input: &mut SplitWhitespace<'_>, n: usize) -> Tree {
    let mut parent = vec![0; n];
    let mut children = vec![Vec::new(); n];
    for vertex in 1..n {
        let p = next_usize(input);
        parent[vertex] = p;
        children[p].push(vertex);
    }

    let mut order = Vec::with_capacity(n);
    let mut stack = vec![0];
    while let Some(vertex) = stack.pop() {
        order.push(vertex);
        for &child in children[vertex].iter().rev() {
            stack.push(child);
        }
    }
    Tree { parent, order }
}

fn main() {
    let mut data = String::new();
    io::stdin().read_to_string(&mut data).unwrap();
    let mut input = data.split_whitespace();
    let n = next_usize(&mut input);
    let a = read_tree(&mut input, n);
    let b = read_tree(&mut input, n);
    let mut label = vec![0; n];
    for i in 0..n {
        label[b.order[i]] = a.order[i];
    }

    let mut operations = Vec::with_capacity(n);
    for i in 1..n {
        let vertex = a.order[i];
        let previous = a.order[i - 1];
        if a.parent[vertex] != previous {
            operations.push((vertex, previous));
        }
    }
    // Undo the target's flattening after matching the two preorder paths.
    for i in (1..n).rev() {
        let vertex = b.order[i];
        if b.parent[vertex] != b.order[i - 1] {
            operations.push((label[vertex], label[b.parent[vertex]]));
        }
    }

    let mut output = String::new();
    writeln!(output, "{}", operations.len()).unwrap();
    for (vertex, destination) in operations {
        writeln!(output, "{} {}", vertex, destination).unwrap();
    }
    io::stdout().write_all(output.as_bytes()).unwrap();
}
