/* 動的計画法
1. スタート地点[0]
dp[0] = 0

2. 頂点1の地点
dp[1]  = dp[0] + A[1]

3. 頂点2の地点
dp[2]  = dp[1] + A[2]
・ 頂点1から頂点2へ移動する

dp[2] = dp[0] + A[1,2]
・ 頂点0から頂点2へ移動する

4. 頂点3の地点
dp[3] = dp[2] + A[3]
・ 頂点２から頂点3へ移動する

dp[3] = dp[1] + A[2,3]
・　頂点1から頂点3へ移動する
*/
#include <iostream>
#include <vector>
using namespace std;
const long long INF  = 1LL << 60; //2^60

int main() {
    //入力
    int N;
    cin >> N;
    vector<int> h(N);
    for (int i = 0; i < N; i++) {
        cin >> h[i];
    }

    //DP
    //配列の定義
    vector<long long> dp(N, INF);

    //初期設定
    dp[0] = 0;

    //実行処理
    for (int i = 1; i < N; i++) {
        if (i == 1){
            dp[i] = abs(h[i] - h[0]);
        }
        else {
            dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),
                        dp[i - 2] + abs(h[i] - h[i - 2]));
        }
    }

    //出力
    cout << dp[N - 1] << endl;
}