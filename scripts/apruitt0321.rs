// Author: Apruitt0321
// Language: Rust
// Github: apruitt0321

fn cbs(i: i32) -> String {
    if i % 3 == 0 && i % 5 == 0 {
        String::from("Spiders!")
    }
    else if i % 3 == 0 {
        String::from("Cats!")
    }
    else if i % 5 == 0 {
        String::from("Bats!")
    }
    else {
        format!("{}", i)
    }
}


fn main() {
    for i in 1..101 {
       let mut s = cbs(i);
       println!("{}",s)
    }
}
