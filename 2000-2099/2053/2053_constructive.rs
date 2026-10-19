use std::io::{self, Write};

const GRID: usize = 4;
const VERTICES: usize = GRID * GRID;
const OUTER_SCALE: i32 = 900;
const DIMENSION: usize = 2;
const ROUNDING_OFFSET: f64 = 0.5;
type Graph = [[u8; VERTICES]; VERTICES];
type Points = [[i32; DIMENSION]; VERTICES];

fn connect(graph: &mut Graph, a: usize, b: usize) {
    graph[a][b] = 1;
    graph[b][a] = 1;
}

fn solve() -> (Points, Graph) {
    let mut graph = [[0; VERTICES]; VERTICES];
    for row in 0..GRID {
        for column in 0..GRID {
            let vertex = row * GRID + column;
            if column + 1 < GRID {
                connect(&mut graph, vertex, vertex + 1);
            }
            if row + 1 < GRID {
                connect(&mut graph, vertex, vertex + GRID);
            }
            if row + 1 < GRID && column + 1 < GRID {
                connect(&mut graph, vertex, vertex + GRID + 1);
            }
        }
    }
    let corners = [0, GRID - 1, VERTICES - 1, VERTICES - GRID];
    for side in 0..GRID {
        let (a, d) = (corners[side], corners[(side + 1) % GRID]);
        let step = (d as isize - a as isize) / (GRID - 1) as isize;
        connect(&mut graph, a, d);
        connect(&mut graph, a, (d as isize - step) as usize);
    }
    connect(&mut graph, corners[1], corners[GRID - 1]);
    let mut points = [[0; DIMENSION]; VERTICES];
    let mut fixed = [false; VERTICES];
    points[corners[0]] = [-OUTER_SCALE, -OUTER_SCALE];
    points[corners[1]] = [OUTER_SCALE, -OUTER_SCALE];
    points[corners[GRID - 1]] = [0, OUTER_SCALE];
    fixed[corners[0]] = true;
    fixed[corners[1]] = true;
    fixed[corners[GRID - 1]] = true;
    let mut index = [0; VERTICES];
    let mut inside = Vec::new();
    for vertex in 0..VERTICES {
        if !fixed[vertex] {
            index[vertex] = inside.len();
            inside.push(vertex);
        }
    }
    let size = inside.len();
    let mut matrix = vec![vec![0.0_f64; size + DIMENSION]; size];
    for &vertex in &inside {
        let row = &mut matrix[index[vertex]];
        for neighbour in 0..VERTICES {
            if graph[vertex][neighbour] != 0 {
                row[index[vertex]] += 1.0;
                if !fixed[neighbour] {
                    row[index[neighbour]] -= 1.0;
                } else {
                    for axis in 0..DIMENSION {
                        row[size + axis] += f64::from(points[neighbour][axis]);
                    }
                }
            }
        }
    }
    for column in 0..size {
        let mut pivot = column;
        for row in column + 1..size {
            if matrix[row][column].abs() > matrix[pivot][column].abs() {
                pivot = row;
            }
        }
        matrix.swap(column, pivot);
        let divisor = matrix[column][column];
        for value in &mut matrix[column] {
            *value /= divisor;
        }
        let normalized = matrix[column].clone();
        for (row, entries) in matrix.iter_mut().enumerate() {
            if row != column {
                let factor = entries[column];
                for (value, &unit) in entries.iter_mut().zip(&normalized) {
                    *value -= factor * unit;
                }
            }
        }
    }
    for &vertex in &inside {
        for axis in 0..DIMENSION {
            points[vertex][axis] =
                (matrix[index[vertex]][size + axis] + ROUNDING_OFFSET).floor() as i32;
        }
    }
    (points, graph)
}

fn main() {
    let (points, graph) = solve();
    let mut out = io::BufWriter::new(io::stdout().lock());
    for point in points {
        writeln!(out, "{} {}", point[0], point[1]).unwrap();
    }
    for row in graph {
        for bit in row {
            write!(out, "{}", bit).unwrap();
        }
        writeln!(out).unwrap();
    }
}
