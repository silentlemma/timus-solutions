use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read};

const INFINITY_COST: i32 = 1_000_000_000;
const PADDING: usize = 2;
const DIRECTIONS: usize = 4;

fn neighbors(vertex: usize, stride: usize) -> [usize; DIRECTIONS] {
    [vertex - stride, vertex + 1, vertex + stride, vertex - 1]
}

fn bfs(cells: &[u8], stride: usize, start: usize) -> (Vec<i32>, Vec<usize>, Vec<usize>) {
    let mut distance = vec![-1; cells.len()];
    let mut parent = vec![usize::MAX; cells.len()];
    let mut order = vec![start];
    distance[start] = 0;
    let mut head = 0;
    while head < order.len() {
        let vertex = order[head];
        head += 1;
        for other in neighbors(vertex, stride) {
            if cells[other] == b'.' && distance[other] < 0 {
                distance[other] = distance[vertex] + 1;
                parent[other] = vertex;
                order.push(other);
            }
        }
    }
    (distance, parent, order)
}

fn solve(grid: &[Vec<u8>], sr: usize, sc: usize, tr: usize, tc: usize) -> (usize, usize) {
    let rows = grid.len();
    let cols = grid[0].len();
    let stride = cols + PADDING;
    let mut cells = vec![b'#'; (rows + PADDING) * stride];
    for (row, content) in grid.iter().enumerate() {
        let at = (row + 1) * stride + 1;
        cells[at..at + cols].copy_from_slice(content);
    }
    let start = (sr + 1) * stride + sc + 1;
    let target = (tr + 1) * stride + tc + 1;
    let coordinates = |vertex: usize| (vertex / stride - 1, vertex % stride - 1);
    let (ds, parent, order) = bfs(&cells, stride, start);
    if ds[target] == 1 {
        for (vertex, &ch) in cells.iter().enumerate() {
            if ch == b'.' && vertex != start && vertex != target {
                return coordinates(vertex);
            }
        }
    }
    let (dt, _, _) = bfs(&cells, stride, target);
    let mut path = Vec::new();
    let mut vertex = target;
    while vertex != usize::MAX {
        path.push(vertex);
        vertex = parent[vertex];
    }
    path.reverse();
    let length = path.len() - 1;
    let mut position = vec![usize::MAX; cells.len()];
    let mut level = vec![usize::MAX; cells.len()];
    for (at, &vertex) in path.iter().enumerate() {
        position[vertex] = at;
    }
    for &vertex in &order {
        level[vertex] = if position[vertex] != usize::MAX {
            position[vertex]
        } else {
            level[parent[vertex]]
        };
    }
    let mut edges = Vec::new();
    let mut detour = vec![INFINITY_COST; cells.len()];
    for &vertex in &order {
        for other in neighbors(vertex, stride) {
            if cells[other] != b'.' || level[other] == usize::MAX || level[vertex] >= level[other] {
                continue;
            }
            edges.push((vertex, other));
            if position[other] == usize::MAX {
                detour[other] = detour[other].min(ds[vertex] + 1);
            }
        }
    }
    let mut heap = BinaryHeap::new();
    for &vertex in &order {
        if detour[vertex] < INFINITY_COST {
            heap.push(Reverse((detour[vertex], vertex)));
        }
    }
    while let Some(Reverse((distance, vertex))) = heap.pop() {
        if distance != detour[vertex] {
            continue;
        }
        for other in neighbors(vertex, stride) {
            if level[other] == level[vertex]
                && position[other] == usize::MAX
                && distance + 1 < detour[other]
            {
                detour[other] = distance + 1;
                heap.push(Reverse((distance + 1, other)));
            }
        }
    }
    let mut answer = vec![INFINITY_COST; length + 1];
    let mut intervals = Vec::new();
    for (x, y) in edges {
        let (left, right) = (level[x], level[y]);
        if left + 1 < right {
            intervals.push((left + 1, right - 1, ds[x] + 1 + dt[y]));
        }
        if position[x] == usize::MAX && 1 <= left && left < length {
            answer[left] = answer[left].min(detour[x] + 1 + dt[y]);
        }
    }
    intervals.sort_unstable();
    let mut at = 0;
    let mut best = 1;
    for failed in 1..length {
        while at < intervals.len() && intervals[at].0 <= failed {
            let (_, right, cost) = intervals[at];
            heap.push(Reverse((cost, right)));
            at += 1;
        }
        while heap
            .peek()
            .is_some_and(|Reverse((_, right))| *right < failed)
        {
            heap.pop();
        }
        if let Some(Reverse((cost, _))) = heap.peek() {
            answer[failed] = answer[failed].min(*cost);
        }
        if answer[failed] > answer[best] {
            best = failed;
        }
    }
    coordinates(path[best])
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let rows: usize = tokens.next().unwrap().parse().unwrap();
    let _cols: usize = tokens.next().unwrap().parse().unwrap();
    let sr: usize = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
    let sc: usize = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
    let tr: usize = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
    let tc: usize = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
    let grid: Vec<Vec<u8>> = (0..rows)
        .map(|_| tokens.next().unwrap().as_bytes().to_vec())
        .collect();
    let (row, col) = solve(&grid, sr, sc, tr, tc);
    println!("{} {}", row + 1, col + 1);
}
