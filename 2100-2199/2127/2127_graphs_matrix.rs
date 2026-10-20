use std::io::{self, Read};

const MOD: i64 = 998244353;
const CYCLE_PERIOD: usize = 4;
const NONE: usize = usize::MAX;

struct Scanner {
    input: Vec<u8>,
    position: usize,
}

impl Scanner {
    fn next(&mut self) -> usize {
        while self.position < self.input.len() && self.input[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.input.len() && !self.input[self.position].is_ascii_whitespace() {
            value = value * 10 + (self.input[self.position] - b'0') as usize;
            self.position += 1;
        }
        value
    }
}

struct Path {
    from: usize,
    to: usize,
    internal: usize,
}

fn power(mut base: i64, mut exponent: i64) -> i64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent % 2 == 1 {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exponent /= 2;
    }
    result
}

fn determinant(matrix: &mut [Vec<i64>]) -> i64 {
    let size = matrix.len();
    let mut result = 1;
    for column in 0..size {
        let pivot = match (column..size).find(|&row| matrix[row][column] != 0) {
            Some(row) => row,
            None => return 0,
        };
        if pivot != column {
            matrix.swap(pivot, column);
            result = MOD - result;
        }
        let value = matrix[column][column];
        result = result * value % MOD;
        let inverse = power(value, MOD - 2);
        let (before, after) = matrix.split_at_mut(column + 1);
        let pivot_row = &before[column];
        for row in after {
            if row[column] == 0 {
                continue;
            }
            let factor = row[column] * inverse % MOD;
            for next in column + 1..size {
                let mut updated = row[next] - factor * pivot_row[next] % MOD;
                if updated < 0 {
                    updated += MOD;
                }
                row[next] = updated;
            }
        }
    }
    result
}

fn add_edge(matrix: &mut [Vec<i64>], from: usize, to: usize, weight: i64) {
    matrix[from][to] = (matrix[from][to] + weight) % MOD;
    matrix[to][from] = (matrix[to][from] + weight) % MOD;
}

fn solve(graph: &[Vec<usize>]) -> i64 {
    let size = graph.len();
    let mut degree: Vec<usize> = graph.iter().map(Vec::len).collect();
    let mut active = vec![true; size];
    let mut queue = Vec::with_capacity(size);
    for (vertex, &count) in degree.iter().enumerate() {
        if count == 0 {
            return 0;
        }
        if count == 1 {
            queue.push(vertex);
        }
    }

    let mut result = 1;
    let mut head = 0;
    while head < queue.len() {
        let leaf = queue[head];
        head += 1;
        if !active[leaf] {
            continue;
        }
        let neighbor = graph[leaf].iter().copied().find(|&v| active[v]).unwrap();
        // Expanding at a leaf removes its neighbor and changes the sign.
        active[leaf] = false;
        active[neighbor] = false;
        result = MOD - result;
        for &vertex in &graph[neighbor] {
            if active[vertex] {
                degree[vertex] -= 1;
                if degree[vertex] == 0 {
                    return 0;
                }
                if degree[vertex] == 1 {
                    queue.push(vertex);
                }
            }
        }
    }

    let mut index = vec![NONE; size];
    let mut branches = 0;
    for vertex in 0..size {
        if active[vertex] && degree[vertex] > 2 {
            index[vertex] = branches;
            branches += 1;
        }
    }
    let mut visited = vec![false; size];
    let mut paths = Vec::new();
    let mut auxiliaries = 0;
    for vertex in 0..size {
        if index[vertex] == NONE {
            continue;
        }
        for &neighbor in &graph[vertex] {
            if !active[neighbor] {
                continue;
            }
            if index[neighbor] != NONE {
                if vertex < neighbor {
                    paths.push(Path {
                        from: index[vertex],
                        to: index[neighbor],
                        internal: 0,
                    });
                }
                continue;
            }
            if visited[neighbor] {
                continue;
            }
            let mut previous = vertex;
            let mut current = neighbor;
            let mut internal = 0;
            while index[current] == NONE {
                visited[current] = true;
                internal += 1;
                let next = graph[current]
                    .iter()
                    .copied()
                    .find(|&candidate| active[candidate] && candidate != previous)
                    .unwrap();
                previous = current;
                current = next;
            }
            auxiliaries += internal % 2;
            paths.push(Path {
                from: index[vertex],
                to: index[current],
                internal,
            });
        }
    }

    // Odd paths leave independent auxiliary vertices in the reduced matrix.
    if auxiliaries > branches {
        return 0;
    }
    for vertex in 0..size {
        if !active[vertex] || index[vertex] != NONE || visited[vertex] {
            continue;
        }
        let mut length = 0;
        let mut previous = NONE;
        let mut current = vertex;
        loop {
            visited[current] = true;
            length += 1;
            let next = graph[current]
                .iter()
                .copied()
                .find(|&candidate| active[candidate] && candidate != previous)
                .unwrap();
            previous = current;
            current = next;
            if current == vertex {
                break;
            }
        }
        if length % 2 == 1 {
            result = result * 2 % MOD;
        } else if length % CYCLE_PERIOD == 0 {
            return 0;
        } else {
            result = result * (MOD - CYCLE_PERIOD as i64) % MOD;
        }
    }

    let reduced_size = branches + auxiliaries;
    let mut matrix = vec![vec![0; reduced_size]; reduced_size];
    let mut next_auxiliary = branches;
    for path in paths {
        let negative = (path.internal / 2) % 2 == 1;
        let weight = if negative { MOD - 1 } else { 1 };
        if negative {
            result = MOD - result;
        }
        // Removing two internal vertices negates the new edge and determinant.
        if path.internal % 2 == 0 {
            add_edge(&mut matrix, path.from, path.to, weight);
        } else {
            add_edge(&mut matrix, path.from, next_auxiliary, weight);
            add_edge(&mut matrix, next_auxiliary, path.to, 1);
            next_auxiliary += 1;
        }
    }
    result * determinant(&mut matrix) % MOD
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let mut scanner = Scanner { input, position: 0 };
    let size = scanner.next();
    let edges = scanner.next();
    let mut graph = vec![Vec::new(); size];
    for _ in 0..edges {
        let from = scanner.next() - 1;
        let to = scanner.next() - 1;
        graph[from].push(to);
        graph[to].push(from);
    }
    println!("{}", solve(&graph));
}
