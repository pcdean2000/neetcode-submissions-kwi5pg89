// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<Pair> mergeSort(vector<Pair>& pairs) {
        if (pairs.size() <= 1) return pairs;

        int middle = pairs.size() / 2;
        vector<Pair> left(pairs.begin(), pairs.begin() + middle);
        vector<Pair> right(pairs.begin() + middle, pairs.end());
        left = mergeSort(left);
        right = mergeSort(right);
        int l = 0;
        int r = 0;
        vector<Pair> res;

        while (l < left.size() || r < right.size())
        {
            if (l == left.size())
            {
                res.push_back(right[r]);
                ++r;
            }
            else if (r == right.size())
            {
                res.push_back(left[l]);
                ++l;
            }
            else if (left[l].key <= right[r].key)
            {
                res.push_back(left[l]);
                ++l;
            }
            else
            {
                res.push_back(right[r]);
                ++r;
            }
        }

        return res;
    }
};
