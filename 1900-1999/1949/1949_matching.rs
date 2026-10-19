use std::io::{self, Read};

struct Movie {
    start: i32,
    finish: i32,
    count: i32,
}

fn augment(
    vertex: usize,
    edges: &[Vec<bool>],
    own: &mut [i32],
    other: &mut [i32],
    active: &[bool],
    visited: &mut [bool],
) -> bool {
    for target in 0..active.len() {
        if !edges[vertex][target] || !active[target] || visited[target] {
            continue;
        }
        visited[target] = true;
        let partner = other[target];
        if partner < 0 || augment(partner as usize, edges, own, other, active, visited) {
            own[vertex] = target as i32;
            other[target] = vertex as i32;
            return true;
        }
    }
    false
}

fn choose_movies(movies: &[Movie], students: usize) -> String {
    let size = movies.len();
    let mut following = vec![vec![false; size]; size];
    let mut preceding = vec![vec![false; size]; size];
    for first in 0..size {
        for second in 0..size {
            if movies[first].finish <= movies[second].start
                && movies[first].count <= movies[second].count
            {
                following[first][second] = true;
                preceding[second][first] = true;
            }
        }
    }
    let (mut left, mut right) = (vec![-1; size], vec![-1; size]);
    let mut active = vec![false; size];
    let (mut chosen, mut matching) = (0, 0);
    let mut answer = String::with_capacity(size);
    for candidate in 0..size {
        let (old_left, old_right, old_matching) = (left.clone(), right.clone(), matching);
        let mut visited = vec![false; size];
        matching += usize::from(augment(
            candidate,
            &following,
            &mut left,
            &mut right,
            &active,
            &mut visited,
        ));
        active[candidate] = true;
        visited.fill(false);
        matching += usize::from(augment(
            candidate,
            &preceding,
            &mut right,
            &mut left,
            &active,
            &mut visited,
        ));
        if chosen + 1 - matching <= students {
            answer.push('1');
            chosen += 1;
        } else {
            answer.push('0');
            active[candidate] = false;
            left = old_left;
            right = old_right;
            matching = old_matching;
        }
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let size: usize = words.next().unwrap().parse().unwrap();
    let students: usize = words.next().unwrap().parse().unwrap();
    let movies: Vec<Movie> = (0..size)
        .map(|_| Movie {
            start: words.next().unwrap().parse().unwrap(),
            finish: words.next().unwrap().parse().unwrap(),
            count: words.next().unwrap().parse().unwrap(),
        })
        .collect();
    println!("{}", choose_movies(&movies, students));
}
