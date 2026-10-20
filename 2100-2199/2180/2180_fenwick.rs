use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

enum Operation {
    Query(usize),
    Direct(usize, i64),
    Whole(usize, i64),
    Partial(usize, usize, i64),
}

struct SparseFenwick {
    size: usize,
    coordinates: Vec<Vec<usize>>,
    tree: Vec<Vec<i64>>,
}

impl SparseFenwick {
    fn new(size: usize) -> Self {
        Self {
            size,
            coordinates: vec![Vec::new(); size + 1],
            tree: vec![Vec::new(); size + 1],
        }
    }

    fn register(&mut self, mut position: usize, limit: usize) {
        while position <= self.size {
            self.coordinates[position].push(limit);
            position += position & position.wrapping_neg();
        }
    }

    fn prepare(&mut self) {
        for position in 1..=self.size {
            let values = &mut self.coordinates[position];
            values.sort_unstable();
            values.dedup();
            self.tree[position] = vec![0; values.len() + 1];
        }
    }

    fn add(&mut self, mut position: usize, limit: usize, value: i64) {
        while position <= self.size {
            let values = &self.coordinates[position];
            let mut rank = values.len() - values.partition_point(|&item| item < limit);
            let tree = &mut self.tree[position];
            while rank < tree.len() {
                tree[rank] += value;
                rank += rank & rank.wrapping_neg();
            }
            position += position & position.wrapping_neg();
        }
    }

    fn sum(&self, mut position: usize, depth: usize) -> i64 {
        let mut result = 0;
        while position > 0 {
            let values = &self.coordinates[position];
            let mut rank = values.len() - values.partition_point(|&item| item < depth);
            let tree = &self.tree[position];
            while rank > 0 {
                result += tree[rank];
                rank -= rank & rank.wrapping_neg();
            }
            position -= position & position.wrapping_neg();
        }
        result
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let size: usize = tokens.next().unwrap().parse().unwrap();
    let mut parent = vec![0; size + 1];
    let mut first_child = vec![0; size + 1];
    let mut next_sibling = vec![0; size + 1];
    let mut depth = vec![0; size + 1];
    let mut subtree_size = vec![1; size + 1];
    let mut deepest = vec![0; size + 1];
    for vertex in 2..=size {
        parent[vertex] = tokens.next().unwrap().parse().unwrap();
        depth[vertex] = depth[parent[vertex]] + 1;
        deepest[vertex] = depth[vertex];
        next_sibling[vertex] = first_child[parent[vertex]];
        first_child[parent[vertex]] = vertex;
    }
    for vertex in (2..=size).rev() {
        subtree_size[parent[vertex]] += subtree_size[vertex];
        deepest[parent[vertex]] = deepest[parent[vertex]].max(deepest[vertex]);
    }

    let mut entry = vec![0; size + 1];
    let mut exit = vec![0; size + 1];
    let mut stack = vec![1];
    let mut timer = 0;
    while let Some(vertex) = stack.pop() {
        timer += 1;
        entry[vertex] = timer;
        exit[vertex] = timer + subtree_size[vertex] - 1;
        let mut child = first_child[vertex];
        while child != 0 {
            stack.push(child);
            child = next_sibling[child];
        }
    }

    let query_count: usize = tokens.next().unwrap().parse().unwrap();
    let mut operations = Vec::with_capacity(query_count);
    let mut partial = SparseFenwick::new(size);
    for _ in 0..query_count {
        let symbol = tokens.next().unwrap();
        let vertex: usize = tokens.next().unwrap().parse().unwrap();
        if symbol == "?" {
            operations.push(Operation::Query(vertex));
            continue;
        }
        let radius: usize = tokens.next().unwrap().parse().unwrap();
        let value: i64 = tokens.next().unwrap().parse().unwrap();
        let limit = depth[vertex] + radius;
        if radius == 0 {
            operations.push(Operation::Direct(vertex, value));
        } else if limit >= deepest[vertex] {
            operations.push(Operation::Whole(vertex, value));
        } else {
            partial.register(entry[vertex], limit);
            partial.register(exit[vertex] + 1, limit);
            operations.push(Operation::Partial(vertex, limit, value));
        }
    }
    partial.prepare();

    let mut direct = vec![0_i64; size + 1];
    let mut whole = vec![0_i64; size + 1];
    let mut output = String::new();
    for operation in operations {
        match operation {
            Operation::Query(vertex) => {
                let mut answer = direct[vertex] + partial.sum(entry[vertex], depth[vertex]);
                let mut position = entry[vertex];
                while position > 0 {
                    answer += whole[position];
                    position -= position & position.wrapping_neg();
                }
                writeln!(output, "{}", answer).unwrap();
            }
            Operation::Direct(vertex, value) => direct[vertex] += value,
            Operation::Whole(vertex, value) => {
                let mut position = entry[vertex];
                while position <= size {
                    whole[position] += value;
                    position += position & position.wrapping_neg();
                }
                position = exit[vertex] + 1;
                while position <= size {
                    whole[position] -= value;
                    position += position & position.wrapping_neg();
                }
            }
            Operation::Partial(vertex, limit, value) => {
                partial.add(entry[vertex], limit, value);
                partial.add(exit[vertex] + 1, limit, -value);
            }
        }
    }
    print!("{}", output);
}
