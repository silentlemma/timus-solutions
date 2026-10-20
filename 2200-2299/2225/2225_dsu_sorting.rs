use std::io::{self, Read};

fn find_root(parent: &mut [usize], mut vertex: usize) -> usize {
    while parent[vertex] != vertex {
        parent[vertex] = parent[parent[vertex]];
        vertex = parent[vertex];
    }
    vertex
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let height: Vec<i64> = tokens.map(|token| token.parse().unwrap()).collect();
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_unstable_by(|&a, &b| height[b].cmp(&height[a]));
    let mut parent: Vec<usize> = (0..n).collect();
    let mut size = vec![0; n];
    let mut answer = 0_i64;
    for vertex in order {
        size[vertex] = 1;
        answer += height[vertex];
        for neighbor in [vertex.checked_sub(1), Some(vertex + 1)] {
            let neighbor = match neighbor {
                Some(value) if value < n && size[value] != 0 => value,
                _ => continue,
            };
            let mut a = find_root(&mut parent, vertex);
            let mut b = find_root(&mut parent, neighbor);
            // Joining two odd runs saves one strike at every remaining level.
            if size[a] % 2 == 1 && size[b] % 2 == 1 {
                answer -= height[vertex];
            }
            if size[a] < size[b] {
                std::mem::swap(&mut a, &mut b);
            }
            parent[b] = a;
            size[a] += size[b];
        }
    }
    println!("{answer}");
}
