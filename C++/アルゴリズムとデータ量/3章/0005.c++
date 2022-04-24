/*全探査*/

/*
Nこの整数 A_1, A_2, ..., A_N
このうちv=A_iの位置を出力する
*/

#include <iostream>
#include <vector>
using namespace std;

int main() {
    //入力
    int N, V;
    cin >> N >> V;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    //線形探索
    int found_id = -1;
    for (int i = 0; i < N; i++) {
        if (A[i] == V) {
            found_id = i;
            break;
        }
    }

    //出力結果
    cout << found_id << endl;
}