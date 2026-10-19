use std::collections::{hash_map::Entry, HashMap};
use std::io::{self, Read};

struct Account {
    password: String,
    online: bool,
}

fn process(commands: &[Vec<String>]) -> Vec<String> {
    let mut accounts: HashMap<String, Account> = HashMap::new();
    let mut replies = Vec::new();
    for command in commands {
        let action = command[0].as_str();
        let reply = match accounts.entry(command[1].clone()) {
            Entry::Vacant(slot) => {
                if action == "register" {
                    slot.insert(Account {
                        password: command[2].clone(),
                        online: false,
                    });
                    "success: new user added"
                } else {
                    "fail: no such user"
                }
            }
            Entry::Occupied(mut slot) => {
                let account = slot.get_mut();
                if action == "register" {
                    "fail: user already exists"
                } else if action == "login" {
                    if account.password != command[2] {
                        "fail: incorrect password"
                    } else if account.online {
                        "fail: already logged in"
                    } else {
                        account.online = true;
                        "success: user logged in"
                    }
                } else if !account.online {
                    "fail: already logged out"
                } else {
                    account.online = false;
                    "success: user logged out"
                }
            }
        };
        replies.push(reply.to_string());
    }
    replies
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let mut commands = Vec::new();
    for _ in 0..count {
        let action = tokens.next().unwrap().to_string();
        let name = tokens.next().unwrap().to_string();
        let mut command = vec![action.clone(), name];
        if action != "logout" {
            command.push(tokens.next().unwrap().to_string());
        }
        commands.push(command);
    }
    for reply in process(&commands) {
        println!("{}", reply);
    }
}
