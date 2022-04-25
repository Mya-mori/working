int function(int N){
    if (N == 0){
        return 0;
    }
    else{
        return function(N - 1) + N;
    }
}