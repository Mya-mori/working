#include <iostream>
using namespace std;

int func(int N) {
    //再帰関数を呼び出す
    cout <<"func(" << N << ")を呼び出します" << endl;

    if (N == 0){
        return 0;
    }

    //出力
    int result = N + func(N - 1);
    cout << N << " までの和 = " << result << endl;

    return result;
}

int main() {
    func(5);
}