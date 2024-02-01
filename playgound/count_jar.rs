// Rust loop to count money in a jar
fn counter(jar: Vec<i32>) -> i32 {
    let mut total = 0;
    for coin in jar {
        total += coin;
    }
    total
}

fn main() {
    let jar = vec![1, 2, 3, 4, 5];
    println!("{}", counter(jar));
}
