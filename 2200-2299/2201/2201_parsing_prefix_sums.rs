use std::collections::HashMap;
use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

const LOG_PREFIX_LENGTH: usize = 11;
const MAX_EXPONENT: u32 = 30;
const ADMIN_NAME: &str = "admin";

/// Writes value as root^exponent with the largest possible exponent.
fn perfect_power(value: i64) -> (i64, i64) {
    for exponent in (2..=MAX_EXPONENT).rev() {
        let guess = (value as f64).powf(1.0 / exponent as f64).round() as i64;
        for root in (guess - 1).max(2)..=guess + 1 {
            let mut power: i64 = 1;
            let mut i = 0;
            while i < exponent && power <= value {
                power *= root;
                i += 1;
            }
            if power == value {
                return (root, exponent as i64);
            }
        }
    }
    (value, 1)
}

#[derive(Default)]
struct Player {
    gl: i64,
    hf: i64,
    online: bool,
}

fn message_body(command: &str) -> &str {
    command.split_once(' ').map_or("", |(_, message)| message)
}

fn message_counts(message: &str) -> (i64, i64) {
    let mut gl = 0;
    let mut hf = 0;
    for &letter in message.as_bytes().iter().step_by(2) {
        if letter == b'g' {
            gl += 1;
        } else {
            hf += 1;
        }
    }
    (gl, hf)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let mut header = lines.next().unwrap().split_whitespace();
    let count: usize = header.next().unwrap().parse().unwrap();
    let _message_limit: usize = header.next().unwrap().parse().unwrap();
    let a: f64 = header.next().unwrap().parse().unwrap();
    let b: f64 = header.next().unwrap().parse().unwrap();
    let log_a = a.ln();
    let log_b = b.ln();
    // A^g = B^f exactly when both are powers of one root with matching
    // exponents; a base of 1 contributes nothing.
    let mut related = true;
    let mut scale_good = (a > 1.0) as i64;
    let mut scale_fun = (b > 1.0) as i64;
    if a > 1.0 && b > 1.0 {
        let (good_root, good_exponent) = perfect_power(a as i64);
        let (fun_root, fun_exponent) = perfect_power(b as i64);
        related = good_root == fun_root;
        scale_good = good_exponent;
        scale_fun = fun_exponent;
    }
    let mut players = HashMap::new();
    players.insert(
        ADMIN_NAME.to_string(),
        Player {
            online: true,
            ..Player::default()
        },
    );
    let mut global_gl = 0;
    let mut global_hf = 0;
    let mut online = 1;
    let mut output = String::new();

    for line in lines.take(count) {
        let (author, command) = line[LOG_PREFIX_LENGTH..].split_once(": /").unwrap();
        match command.as_bytes()[0] {
            b'j' => {
                let current = players.entry(author.to_string()).or_default();
                if current.online {
                    writeln!(output, "Failed: {} is already on the server", author).unwrap();
                } else {
                    current.gl -= global_gl;
                    current.hf -= global_hf;
                    current.online = true;
                    online += 1;
                    writeln!(output, "Successful").unwrap();
                }
            }
            b'q' => {
                let current = players.get_mut(author).unwrap();
                current.gl += global_gl;
                current.hf += global_hf;
                current.online = false;
                online -= 1;
                writeln!(output, "Successful").unwrap();
            }
            b'o' => {
                writeln!(output, "There are {} players on the server", online).unwrap();
            }
            b's' => {
                let message = message_body(command);
                let (gl, hf) = message_counts(message);
                global_gl += gl;
                global_hf += hf;
                let current = players.get_mut(author).unwrap();
                current.gl -= gl;
                current.hf -= hf;
                writeln!(output, "{}: {}", author, message).unwrap();
            }
            b'w' => {
                let left = command.find('<').unwrap();
                let right = command.find('>').unwrap();
                let recipient = &command[left + 1..right];
                let message = message_body(command);
                if let Some(target) = players.get_mut(recipient) {
                    if target.online {
                        let (gl, hf) = message_counts(message);
                        target.gl += gl;
                        target.hf += hf;
                    }
                }
                writeln!(output, "{} (to {}): {}", author, recipient, message).unwrap();
            }
            b'c' => {
                if author != ADMIN_NAME {
                    writeln!(output, "Failed: you have no such rights").unwrap();
                    continue;
                }
                let left = command.find('<').unwrap();
                let right = command.find('>').unwrap();
                let mut first_name = &command[left + 1..right];
                let mut second_name = first_name;
                let explicit = right + 1 < command.len();
                if explicit {
                    const COMPARISON_JOIN: &str = ">-<";
                    second_name = &command[right + COMPARISON_JOIN.len()..command.len() - 1];
                } else {
                    first_name = ADMIN_NAME;
                }
                let first = players.get(first_name).filter(|player| player.online);
                let second = players.get(second_name).filter(|player| player.online);
                if first.is_none() {
                    writeln!(output, "Failed: {} is not on the server", first_name).unwrap();
                } else if second.is_none() {
                    writeln!(output, "Failed: {} is not on the server", second_name).unwrap();
                } else {
                    let first = first.unwrap();
                    let second = second.unwrap();
                    // The common public-message counts cancel for two online players.
                    let good = first.gl - second.gl;
                    let fun = first.hf - second.hf;
                    let equal = if related {
                        good * scale_good == fun * scale_fun
                    } else {
                        good == 0 && fun == 0
                    };
                    if equal {
                        if explicit {
                            writeln!(output, "Their luck is equal").unwrap();
                        } else {
                            writeln!(output, "{} is good", second_name).unwrap();
                        }
                    } else if good as f64 * log_a - fun as f64 * log_b > 0.0 {
                        writeln!(output, "{} is a loser", second_name).unwrap();
                    } else {
                        writeln!(output, "{} is a lucky guy", second_name).unwrap();
                    }
                }
            }
            _ => unreachable!(),
        }
    }
    io::stdout().write_all(output.as_bytes()).unwrap();
}
