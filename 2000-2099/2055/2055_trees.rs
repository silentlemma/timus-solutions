use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord)]
struct Edge {
    weight: i32,
    first: usize,
    second: usize,
    id: usize,
}

struct DisjointSet {
    parent: Vec<i32>,
}
impl DisjointSet {
    fn new(size: usize) -> Self {
        Self {
            parent: vec![-1; size],
        }
    }
    fn root(&mut self, mut vertex: usize) -> usize {
        while self.parent[vertex] >= 0 {
            let ancestor = self.parent[vertex] as usize;
            if self.parent[ancestor] >= 0 {
                self.parent[vertex] = self.parent[ancestor];
            }
            vertex = self.parent[vertex] as usize;
        }
        vertex
    }
    fn unite(&mut self, first: usize, second: usize) -> bool {
        let mut first = self.root(first);
        let mut second = self.root(second);
        if first == second {
            return false;
        }
        if self.parent[first] > self.parent[second] {
            std::mem::swap(&mut first, &mut second);
        }
        self.parent[first] += self.parent[second];
        self.parent[second] = first as i32;
        true
    }
}

struct LinkCut {
    left: Vec<usize>,
    right: Vec<usize>,
    parent: Vec<usize>,
    minimum: Vec<usize>,
    key: Vec<usize>,
    reverse: Vec<bool>,
    ancestors: Vec<usize>,
}
impl LinkCut {
    fn new(vertices: usize, edges: usize) -> Self {
        let size = 2 * vertices;
        Self {
            left: vec![0; size],
            right: vec![0; size],
            parent: vec![0; size],
            minimum: (0..size).collect(),
            key: vec![edges + 1; size],
            reverse: vec![false; size],
            ancestors: Vec::new(),
        }
    }
    fn auxiliary_root(&self, vertex: usize) -> bool {
        let ancestor = self.parent[vertex];
        ancestor == 0 || (self.left[ancestor] != vertex && self.right[ancestor] != vertex)
    }
    fn pull(&mut self, vertex: usize) {
        let mut best = vertex;
        for child in [self.left[vertex], self.right[vertex]] {
            let candidate = self.minimum[child];
            if self.key[candidate] < self.key[best] {
                best = candidate;
            }
        }
        self.minimum[vertex] = best;
    }
    fn toggle(&mut self, vertex: usize) {
        if vertex != 0 {
            std::mem::swap(&mut self.left[vertex], &mut self.right[vertex]);
            self.reverse[vertex] = !self.reverse[vertex];
        }
    }
    fn rotate(&mut self, vertex: usize) {
        let ancestor = self.parent[vertex];
        let grandparent = self.parent[ancestor];
        let child;
        if self.left[ancestor] == vertex {
            child = self.right[vertex];
            self.left[ancestor] = child;
            self.right[vertex] = ancestor;
        } else {
            child = self.left[vertex];
            self.right[ancestor] = child;
            self.left[vertex] = ancestor;
        }
        if child != 0 {
            self.parent[child] = ancestor;
        }
        if grandparent != 0 {
            if self.left[grandparent] == ancestor {
                self.left[grandparent] = vertex;
            } else if self.right[grandparent] == ancestor {
                self.right[grandparent] = vertex;
            }
        }
        self.parent[vertex] = grandparent;
        self.parent[ancestor] = vertex;
        self.pull(ancestor);
        self.pull(vertex);
    }
    fn splay(&mut self, vertex: usize) {
        self.ancestors.clear();
        let mut node = vertex;
        self.ancestors.push(node);
        while !self.auxiliary_root(node) {
            node = self.parent[node];
            self.ancestors.push(node);
        }
        for index in (0..self.ancestors.len()).rev() {
            node = self.ancestors[index];
            if self.reverse[node] {
                self.toggle(self.left[node]);
                self.toggle(self.right[node]);
                self.reverse[node] = false;
            }
        }
        while !self.auxiliary_root(vertex) {
            let ancestor = self.parent[vertex];
            let grandparent = self.parent[ancestor];
            if !self.auxiliary_root(ancestor) {
                let aligned =
                    (self.left[grandparent] == ancestor) == (self.left[ancestor] == vertex);
                self.rotate(if aligned { ancestor } else { vertex });
            }
            self.rotate(vertex);
        }
    }
    fn access(&mut self, vertex: usize) {
        let mut last = 0;
        let mut node = vertex;
        while node != 0 {
            self.splay(node);
            self.right[node] = last;
            if last != 0 {
                self.parent[last] = node;
            }
            self.pull(node);
            last = node;
            node = self.parent[node];
        }
        self.splay(vertex);
    }
    fn make_root(&mut self, vertex: usize) {
        self.access(vertex);
        self.toggle(vertex);
    }
    fn add(&mut self, first: usize, second: usize, node: usize, rank: usize) {
        self.key[node] = rank;
        self.make_root(first);
        self.parent[first] = node;
        self.make_root(second);
        self.parent[second] = node;
    }
    fn replace_minimum(&mut self, first: usize, second: usize, rank: usize) -> usize {
        self.make_root(first);
        self.access(second);
        let edge = self.minimum[second];
        self.splay(edge);
        let old = self.key[edge];
        self.toggle(self.left[edge]);
        self.toggle(self.right[edge]);
        self.key[edge] = rank;
        self.pull(edge);
        old
    }
}

fn solve(vertices: usize, edges: &[Edge]) -> Vec<usize> {
    let mut forest = LinkCut::new(vertices, edges.len());
    let mut components = DisjointSet::new(vertices);
    let mut active = vec![false; edges.len()];
    let (mut count, mut lower, mut best_left, mut best_right) = (0, 0, 0, 0);
    let mut best_width = -1;
    for (rank, edge) in edges.iter().enumerate() {
        if components.unite(edge.first, edge.second) {
            count += 1;
            forest.add(edge.first + 1, edge.second + 1, vertices + count, rank);
        } else {
            let old = forest.replace_minimum(edge.first + 1, edge.second + 1, rank);
            active[old] = false;
        }
        active[rank] = true;
        while !active[lower] {
            lower += 1;
        }
        if count == vertices - 1 {
            let width = edge.weight - edges[lower].weight;
            if best_width < 0 || width < best_width {
                best_width = width;
                best_left = lower;
                best_right = rank;
            }
            if best_width == 0 {
                break;
            }
        }
    }
    let mut components = DisjointSet::new(vertices);
    let mut chosen = Vec::with_capacity(vertices - 1);
    for edge in &edges[best_left..=best_right] {
        if components.unite(edge.first, edge.second) {
            chosen.push(edge.id);
            if chosen.len() == vertices - 1 {
                break;
            }
        }
    }
    chosen
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut fields = input.split_whitespace();
    let vertices: usize = fields.next().unwrap().parse().unwrap();
    let count: usize = fields.next().unwrap().parse().unwrap();
    let mut edges = Vec::with_capacity(count);
    for id in 1..=count {
        let first: usize = fields.next().unwrap().parse().unwrap();
        let second: usize = fields.next().unwrap().parse().unwrap();
        let weight = fields.next().unwrap().parse().unwrap();
        edges.push(Edge {
            weight,
            first: first - 1,
            second: second - 1,
            id,
        });
    }
    edges.sort_unstable();
    let mut output = String::new();
    for (index, id) in solve(vertices, &edges).iter().enumerate() {
        if index != 0 {
            output.push(' ');
        }
        write!(output, "{}", id).unwrap();
    }
    println!("{}", output);
}
