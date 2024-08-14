// Write a program to sort HashMap by value? 

#include<bits/stdc++.h>
using namespace std;

// Sort Function for no. of books 
bool sortByValue(const pair<string, int> &a, const pair<string, int> &b) {
    return a.second < b.second;
}
int main(){
    // Define and initialize the unordered_map data(in Key and value)
    unordered_map<string, int> books = {
        {"DSA", 5},
        {"OOPs", 3},
        {"DBMS", 4},
        {"OS", 2},
        {"C++", 8}
    };

    // Create a vector pairs
    vector<pair<string, int>> vec(books.begin(), books.end());

    // Sort the vector by value using a custom comparator
    sort(vec.begin(), vec.end(), sortByValue);

    // Output the sorted elements 
    cout << "Sorted Books by the no of Books: " << endl;
    for (auto &elem : vec) {
        cout << elem.first << ": " << elem.second << endl;
    }
  return 0;
}


