use std::io::{self, Read};
use std::str::SplitWhitespace;

struct Group {
    time: i32,
    students: Vec<usize>,
}

fn read_case(tokens: &mut SplitWhitespace<'_>) -> (Vec<Vec<usize>>, Vec<Group>) {
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let group_count: usize = tokens.next().unwrap().parse().unwrap();
    let mut friends = vec![Vec::new(); count];
    for row in &mut friends {
        loop {
            let id: usize = tokens.next().unwrap().parse().unwrap();
            if id == 0 {
                break;
            }
            row.push(id - 1);
        }
    }
    let mut groups = Vec::new();
    for _ in 0..group_count {
        let time = tokens.next().unwrap().parse().unwrap();
        let size: usize = tokens.next().unwrap().parse().unwrap();
        let students = (0..size)
            .map(|_| tokens.next().unwrap().parse::<usize>().unwrap() - 1)
            .collect();
        groups.push(Group { time, students });
    }
    (friends, groups)
}

fn solve(friends: &[Vec<usize>], groups: &[Group]) -> Vec<(i32, usize)> {
    let count = friends.len();
    let mut queues = [Vec::new(), Vec::new()];
    let mut next_completion = [0; 2];
    let mut which = vec![-1; count];
    let mut position = vec![0; count];
    let mut answer = vec![(0, 0); count];
    for group in groups {
        let now = group.time;
        for side in 0..2 {
            let queue = &mut queues[side];
            if queue.is_empty() || next_completion[side] > now {
                continue;
            }
            let served = queue.len().min((now - next_completion[side] + 1) as usize);
            for (at, student) in queue.drain(..served).enumerate() {
                answer[student] = (next_completion[side] + at as i32, side);
                which[student] = -1;
            }
            for (at, &student) in queue.iter().enumerate() {
                position[student] = at;
            }
            next_completion[side] = if queue.is_empty() {
                0
            } else {
                next_completion[side] + served as i32
            };
        }
        for &student in &group.students {
            let mut best = [queues[0].len(), queues[1].len()];
            for &friend in &friends[student] {
                if which[friend] >= 0 {
                    let side = which[friend] as usize;
                    best[side] = best[side].min(position[friend] + 1);
                }
            }
            let side = if best[0] < best[1] { 0 } else { 1 };
            let queue = &mut queues[side];
            let at = best[side];
            queue.insert(at, student);
            which[student] = side as i32;
            for (index, &person) in queue.iter().enumerate().skip(at) {
                position[person] = index;
            }
            if queue.len() == 1 {
                next_completion[side] = now + 1;
            }
        }
    }
    for side in 0..2 {
        for (at, &student) in queues[side].iter().enumerate() {
            answer[student] = (next_completion[side] + at as i32, side);
        }
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let (friends, groups) = read_case(&mut input.split_whitespace());
    let labels = ["left", "right"];
    let output: String = solve(&friends, &groups)
        .iter()
        .map(|(time, side)| format!("{} {}\n", time, labels[*side]))
        .collect();
    print!("{}", output);
}
