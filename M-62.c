void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

long long uniquePaths(int m, int n) {
    int a = m - 1;
    int b = n - 1;

    if (a > b) {
        swap(&a, &b);  
    }

    long long result = 1;

    // C(a + b, b)
    for (int i = 1; i <= a; ++i) {
        result *= (b + i);
        result /= i;
    }

    return result;
}