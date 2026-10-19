use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

fn reliable_teams(values: &[usize]) -> Vec<Vec<usize>> {
    let count = values.len();
    let mut ordered: Vec<(usize, usize)> = values
        .iter()
        .enumerate()
        .map(|(index, &value)| (value, index + 1))
        .collect();
    ordered.sort_unstable();
    let mut teams = Vec::new();
    let mut members = Vec::with_capacity(count);
    for size in 1..=count {
        members.push(ordered[size - 1].1);
        if ordered[size - 1].0 <= size && (size == count || ordered[size].0 > size + 1) {
            teams.push(members.clone());
        }
    }
    teams
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count = tokens.next().unwrap().parse::<usize>().unwrap();
    let values: Vec<usize> = (0..count)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let teams = reliable_teams(&values);
    let mut output = String::new();
    writeln!(output, "{}", teams.len()).unwrap();
    for team in teams {
        write!(output, "{}", team.len()).unwrap();
        for member in team {
            write!(output, " {}", member).unwrap();
        }
        output.push('\n');
    }
    print!("{}", output);
}
