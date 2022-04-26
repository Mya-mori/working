#include <iostream>
#include <vector>
using namespace std;

template<class T> void chmin(T& a, T b) {//&参照型 Tをaとして返す
    if (a < b){
        a = b;
    }
}

const long long INF = 1LL << 60;

int main() {
    //入力
    int N;
    cin >> N;
    vector<int> h(N);
    for (int i = 0; i < N; i++){
        cin >> h[i];
    }

    //初期化
    vector<long long> dp(N, INF);

}