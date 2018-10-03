//Author: Delkhaz
//Language: Rust
//Github: Delkhaz

fn main() {
    for i in 1..101 {
        if i % 3 == 0 && i % 5 == 0 {
            println!("spider");
        }else if i % 3 == 0 {
            println!("cats");
        }else if i % 5 == 0 {
            println!("bats");
        }else {
            println!("{}", i);
        }
    }
}
