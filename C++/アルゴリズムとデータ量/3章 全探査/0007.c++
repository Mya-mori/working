/*全探査
最小値となるペアを求める
*/

/*
Nこの整数 A_1, A_2, ..., A_N
このうち最小値がK以上となるペアの和をを求める
*/

#include <iostream>
#include <vector>
using namespace std;
const int INF = 100000000;

int main(){
    //入力
    int N, K;
    cin >> N >> K;
    vector<int> A(N);
    for (int i = 0; i < N; i++){
        cin >> A[i];
    }
    //線形探索
    int min_value = INF;
    for (int i = 0; i < N; i++){
        for (int j = i + 1; j < N; j++){
            //K未満はスキップ
            if (A[i] + A[j] < K){
                continue;
            }
            if (A[i] + A[j] < min_value){
                min_value = A[i] + A[j];
            }
        }
    }
    //出力結果
    cout << min_value << endl;
}