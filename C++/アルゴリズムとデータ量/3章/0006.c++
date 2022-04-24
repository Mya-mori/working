/*全探査
最小値を求める
*/

/*
Nこの整数 A_1, A_2, ..., A_N
このうち最小値を求める
*/

#include <iostream>
#include <vector>
using namespace std;
const int INF = 100000000;

int main() {
    //入力
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++){
        cin >> A[i];
    }

    //線形探索
    int min_value = INF;
    for (int i = 0; i < N; i++){
        if (A[i] < min_value) {
            min_value = A[i];
        }
    }

    //出力結果
    cout << min_value << endl;
}