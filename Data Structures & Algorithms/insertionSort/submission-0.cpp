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
    vector<vector<Pair>> insertionSort(vector<Pair>& pairs) {
        vector<vector<Pair>> res;
        for (int i = 0; i < pairs.size(); ++i)
        {
            int curr = i;
            int prev = curr - 1;
            while (prev >= 0 && pairs[curr].key < pairs[prev].key)
            {
                Pair temp = pairs[curr];
                pairs[curr] = pairs[prev];
                pairs[prev] = temp;
                --prev;
                --curr;
            }
            res.push_back(pairs);
        }
        return res;
    }
};
