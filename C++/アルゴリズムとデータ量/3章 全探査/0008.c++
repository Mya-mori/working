/*全探査 部分和


*/
#include <iostream>
#include <vector>
using namespace std;
const int INF = 100000000;

int main() {
    //入力
    int N, W;
    cin >> N >> W;
    vector<int> A(N);
    for (int i = 0; i <N; i++){
        cin >> A[i];
    }

    //線形探索
    bool exist = false;
    for (int bit = 0; bit < (1 << N); bit++){
        int sum = 0;
        for (int i = 0; i < N; i++){
            if (bit & (1 << N)){
                sum += A[i];
            }
        }

        if (sum <= W){
            exist = true;
        }
    }
    if (exist){
        cout <<"Yes" << endl;
    }
    else{
        cout <<"No" << endl;
    }
}