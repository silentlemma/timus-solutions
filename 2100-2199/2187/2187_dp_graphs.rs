use std::io::{self, Read};

const NEGATIVE_INFINITY: i64 = i64::MIN / 2;

struct FastInput {
    data: Vec<u8>,
    position: usize,
}

impl FastInput {
    fn next_usize(&mut self) -> usize {
        while self.data[self.position] <= b' ' {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.data.len() && self.data[self.position] > b' ' {
            value = value * 10 + usize::from(self.data[self.position] - b'0');
            self.position += 1;
        }
        value
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = FastInput { data, position: 0 };
    let n = input.next_usize();
    let m = input.next_usize();
    let mut treasure = vec![0_i64; n];
    let mut cost = vec![0_i64; n];
    for value in &mut treasure {
        *value = input.next_usize() as i64;
    }
    for value in cost.iter_mut().skip(1) {
        *value = input.next_usize() as i64;
    }

    let mut first = vec![0; m];
    let mut second = vec![0; m];
    let mut degree = vec![0; n];
    for edge in 0..m {
        first[edge] = input.next_usize() - 1;
        second[edge] = input.next_usize() - 1;
        degree[first[edge]] += 1;
        degree[second[edge]] += 1;
    }
    let mut offset = vec![0; n + 1];
    for edge in 0..m {
        let (u, v) = (first[edge], second[edge]);
        if degree[u] < degree[v] {
            offset[u + 1] += 1;
        } else if degree[v] < degree[u] {
            offset[v + 1] += 1;
        }
    }
    for vertex in 0..n {
        offset[vertex + 1] += offset[vertex];
    }
    let mut next = offset.clone();
    let mut adjacent = vec![0; offset[n]];
    for edge in 0..m {
        let (u, v) = (first[edge], second[edge]);
        if degree[u] < degree[v] {
            adjacent[next[u]] = v;
            next[u] += 1;
        } else if degree[v] < degree[u] {
            adjacent[next[v]] = u;
            next[v] += 1;
        }
    }

    let mut count = vec![0; n + 1];
    for &value in &degree {
        count[value + 1] += 1;
    }
    for value in 0..n {
        count[value + 1] += count[value];
    }
    let mut order = vec![0; n];
    for vertex in 0..n {
        order[count[degree[vertex]]] = vertex;
        count[degree[vertex]] += 1;
    }

    // A state stores the profit before paying for the unfinished journey.
    let mut states: Vec<Vec<i64>> = vec![Vec::new(); n];
    states[0].push(treasure[0]);
    let mut answer = treasure[0];
    for u in order {
        let mut current = std::mem::take(&mut states[u]);
        if current.is_empty() {
            continue;
        }
        let mut best = current[0];
        for length in 1..current.len() {
            if current[length] != NEGATIVE_INFINITY {
                best = best.max(current[length] - cost[length] + treasure[u]);
            }
        }
        current[0] = best;
        answer = answer.max(best);
        for &v in &adjacent[offset[u]..offset[u + 1]] {
            let target = &mut states[v];
            if target.len() <= current.len() {
                target.resize(current.len() + 1, NEGATIVE_INFINITY);
            }
            for (length, &value) in current.iter().enumerate() {
                target[length + 1] = target[length + 1].max(value);
            }
        }
    }
    println!("{}", answer);
}
