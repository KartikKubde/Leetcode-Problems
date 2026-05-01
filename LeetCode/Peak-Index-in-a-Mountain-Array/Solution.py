1class Solution {
2public:
3    int peakIndexInMountainArray(vector<int>& arr) {
4       int s=0;
5       int e=arr.size() - 1;
6
7       int mid=s+(e-s)/2;
8
9       while(s<e){
10        if (arr[mid]<arr[mid+1]){
11            s=mid+1;
12        }
13        else{
14            e=mid;
15        }
16        mid=s+(e-s)/2;
17       }
18       return s;
19
20
21    }
22};