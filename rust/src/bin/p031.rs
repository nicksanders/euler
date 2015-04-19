

fn main() {

    let target = 200;
    let coin_sizes = [1, 2, 5, 10, 20, 50, 100, 200];
    let mut ways = vec![0; (target + 1)];
    ways[0] = 1;

    for i in (0..coin_sizes.len()) {
        for j in (coin_sizes[i]..(target + 1)) {
            ways[j] += ways[j - coin_sizes[i]];
        }
    }

    println!("{:?}", ways[ways.len() - 1]);

}
