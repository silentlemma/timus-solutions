use std::collections::HashMap;
use std::io::{self, Read};

const HEALTHY: i32 = 3;
const TEAM_SIZE: usize = 4;
const TRIPLE_SIZE: usize = TEAM_SIZE - 1;

fn find(parent: &mut [usize], mut player: usize) -> usize {
    while parent[player] != player {
        parent[player] = parent[parent[player]];
        player = parent[player];
    }
    player
}

fn unite(parent: &mut [usize], first: usize, second: usize) {
    let mut first = find(parent, first);
    let mut second = find(parent, second);
    if first > second {
        std::mem::swap(&mut first, &mut second);
    }
    parent[second] = first;
}

fn solve(input: &str) -> String {
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let names: Vec<&str> = (0..n).map(|_| tokens.next().unwrap()).collect();
    let index: HashMap<&str, usize> = names
        .iter()
        .enumerate()
        .map(|(player, &name)| (name, player))
        .collect();
    let mut parent: Vec<usize> = (0..n).collect();
    let mut health = vec![HEALTHY; n];
    let m: usize = tokens.next().unwrap().parse().unwrap();
    for _ in 0..m {
        let actor = index[tokens.next().unwrap()];
        let action = tokens.next().unwrap();
        if health[actor] < 2 {
            return "FAKE\n".to_owned();
        }
        match action {
            "HIT" => {
                let target = index[tokens.next().unwrap()];
                tokens.next();
                let damage = if tokens.next().unwrap() == "HEAD" {
                    2
                } else {
                    1
                };
                health[target] = (health[target] - damage).max(0);
            }
            "USES" => {
                tokens.next();
                health[actor] = HEALTHY;
            }
            _ => {
                let target = index[tokens.next().unwrap()];
                if health[target] != 1 {
                    return "FAKE\n".to_owned();
                }
                health[target] = 2;
                unite(&mut parent, actor, target);
            }
        }
    }
    let mut groups = vec![Vec::new(); n];
    for player in 0..n {
        let root = find(&mut parent, player);
        groups[root].push(player);
    }
    let mut buckets = vec![Vec::new(); TEAM_SIZE + 1];
    for group in groups {
        if group.len() > TEAM_SIZE {
            return "FAKE\n".to_owned();
        }
        if !group.is_empty() {
            buckets[group.len()].push(group);
        }
    }
    if buckets[1].len() < buckets[TRIPLE_SIZE].len() {
        return "FAKE\n".to_owned();
    }
    let mut teams = buckets[TEAM_SIZE].clone();
    let mut single = 0;
    for group in &buckets[TRIPLE_SIZE] {
        let mut team = group.clone();
        team.push(buckets[1][single][0]);
        teams.push(team);
        single += 1;
    }
    let mut pair = 0;
    while pair + 1 < buckets[2].len() {
        let mut team = buckets[2][pair].clone();
        team.extend_from_slice(&buckets[2][pair + 1]);
        teams.push(team);
        pair += 2;
    }
    if pair < buckets[2].len() {
        let mut team = buckets[2][pair].clone();
        team.push(buckets[1][single][0]);
        team.push(buckets[1][single + 1][0]);
        teams.push(team);
        single += 2;
    }
    while single < buckets[1].len() {
        let mut team = Vec::with_capacity(TEAM_SIZE);
        for _ in 0..TEAM_SIZE {
            team.push(buckets[1][single][0]);
            single += 1;
        }
        teams.push(team);
    }
    let mut out = String::from("CORRECT\n");
    for team in teams {
        for (member, player) in team.iter().enumerate() {
            if member > 0 {
                out.push(' ');
            }
            out.push_str(names[*player]);
        }
        out.push('\n');
    }
    out
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve(&input));
}
