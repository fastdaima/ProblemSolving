

bool can_make_bouquets(int* bloomDay, int bloomDaySize, int m, int k, int day) {
    int total = 0;

    for (int i = 0; i < bloomDaySize; i++) {
        //     printf("index i: %d | total : %d | arr[%d]: %d \n", i, total, i,
        //            bloomDay[i]);
        int count = 0;

        while (i < bloomDaySize && count < k && bloomDay[i] <= day) {
            count++;
            i++;
            //           printf("count: %d\n", count);
        }

        if (count == k) {
            total++;
            i--;
        }

        //        printf("total: %d\n", total);

        if (total >= m) {
            return true;
        }
    }
    return false;
}

int minDays(int* bloomDay, int bloomDaySize, int m, int k) {

    // handling edge case scenario
    // total number of required flowers cannot be greater than the total count
    // of flowers
    if ((long long)m * k > bloomDaySize) {
        return -1;
    }

    int low = 1, high = 1e9;

    while (low < high) {
        int mid = low + (high - low) / 2;
        //   printf("low %d | mid %d | high %d \n", low, mid, high);
        if (can_make_bouquets(bloomDay, bloomDaySize, m, k, mid)) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
}
