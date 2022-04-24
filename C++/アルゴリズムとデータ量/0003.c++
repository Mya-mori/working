#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// distance between two points
double distance(double x1, double y1, double x2, double y2) {
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main(){
    int N;
    cin >> N;
    vector<double> X(N), Y(N);
    for (int i = 0; i < N; i++){
        cin >> X[i] >> Y[i];
    }

    double minimun_dist = 1000000.0;
    for (int i = 0; i < N; i++){
        for (int j = i + 1; j < N; j++){
            double dist_i_j = distance(X[i], Y[i], X[j], Y[j]);

            if (dist_i_j < minimun_dist){
                minimun_dist = dist_i_j;
            }
        }
    }
    cout << minimun_dist << endl;
}