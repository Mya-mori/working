#include <iostream>
using namespace std;

int fibo (int N){
    cout << "fibo(" << N << ")を呼び出します" << endl;

    //ベースケース
    if (N == 0){
        return 0;
    }
    else if (N == 1){
        return 1;
    }
    else{
        int result = fibo(N - 1) + fibo(N - 2);
        cout << N << " 項目 = " << result << endl;
    }
}
int main() {
    fibo(6);
}