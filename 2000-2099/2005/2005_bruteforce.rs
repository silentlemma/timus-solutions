use std::io::{self, Read};

const POINTS: usize = 5;
const END: usize = POINTS - 1;
const FORBIDDEN_LAST: usize = 2;
const MIDDLE_SUM: usize = END * (END - 1) / 2;

fn solve(distance: &[[i32; POINTS]; POINTS]) -> (i32, [usize; POINTS]) {
    let mut best_cost = -1;
    let mut best_route = [0; POINTS];
    for first in 1..END {
        for last in 1..END {
            if first == last || last == FORBIDDEN_LAST {
                continue;
            }
            let middle = MIDDLE_SUM - first - last;
            let route = [0, first, middle, last, END];
            let mut cost = 0;
            for i in 0..END {
                cost += distance[route[i]][route[i + 1]];
            }
            if best_cost < 0 || cost < best_cost {
                best_cost = cost;
                best_route = route;
            }
        }
    }
    (best_cost, best_route)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let mut distance = [[0; POINTS]; POINTS];
    for row in &mut distance {
        for value in row {
            *value = tokens.next().unwrap().parse().unwrap();
        }
    }
    let (cost, route) = solve(&distance);
    println!("{}", cost);
    let output: Vec<String> = route.iter().map(|point| (point + 1).to_string()).collect();
    println!("{}", output.join(" "));
}
