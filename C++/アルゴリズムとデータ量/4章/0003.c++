/*ユークリッドの互除法
m, nの最大公約数を求める
GCD(m, n)

mをnで割った時のあまりをrとする
GCD(m, n) = GCD(n, r)
*/

#include <iostream>
using namespace std;

int GCD(int m, int n){
    // ベースケース
    if (n == 0){
        return m;
    }
    // 再帰呼び出し
    else {
    return GCD(n, m % n);
    }
}

int main(){
    cout << GCD(51, 15) << endl;
    cout << GCD(15, 51) << endl;
}