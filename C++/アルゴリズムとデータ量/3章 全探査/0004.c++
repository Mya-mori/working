/*全探査
計算量O(N)
*/

/*
Nこの整数 A_1, A_2, ..., A_N
このうちv=A_ihがあるかどうかを判定する。
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
    bool exist = false;
    for (int i = 0; i < N; i++) {
        if (A[i] ==V){
            exist == true;
        }
    }

    //出力結果
    if (exist) {
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }
}
