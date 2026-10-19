use std::io::{self, Read};

const TEAM_SIZE: i32 = 3;

fn ways_to_choose(available: i32, count: i32) -> i32 {
    if count < 0 || count > available {
        return 0;
    }
    if count == 0 {
        return 1;
    }
    if count == 1 {
        return available;
    }
    available * (available - 1) / 2
}

fn count_teams(total: i32, special_count: i32, first_special: i32) -> i32 {
    let special = special_count - first_special;
    let ordinary = total - special_count - (1 - first_special);
    let remaining_teams = total / TEAM_SIZE - 1;
    let mut answer = 0;
    for chosen_special in 0..TEAM_SIZE {
        let removed_special = first_special + chosen_special;
        if removed_special == 0 || special_count - removed_special < remaining_teams {
            continue;
        }
        answer += ways_to_choose(special, chosen_special)
            * ways_to_choose(ordinary, TEAM_SIZE - 1 - chosen_special);
    }
    answer
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut tokens = text.split_whitespace();
    let total = tokens.next().unwrap().parse().unwrap();
    let special_count = tokens.next().unwrap().parse().unwrap();
    let first_special = i32::from(tokens.any(|token| token.parse::<i32>().unwrap() == 1));
    println!("{}", count_teams(total, special_count, first_special));
}
