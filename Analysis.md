
# 6. Analysis of copy constructor
Lets assume that rhs table has the same number of records as current table, which is equal to n.

Now lets count the number of operations in copy constructor:
```cpp
template <class TYPE>
SimpleTable<TYPE>::SimpleTable(const SimpleTable<TYPE>& rhs){
    records_=new Record*[rhs.capacity_+1];      //4
    capacity_=rhs.capacity_;                    //1
    for(int i=0;i<capacity_+1;i++){             //1+n+1+n
        records_[i]=nullptr;                    //2n
    }   
    for(int i=0;i<rhs.numRecords();i++){        //1 + (n+1)(n) + n - we know that time complexity of numRecords is O(n), so it will take n operations for numRecords.
        update(rhs.records_[i]->key_,rhs.records_[i]->data_);       // n * (n) - we know that time complexity of update() is O(n), if item does not exist.
    }
}
```
By adding the total number of operations we can derive the following equation:
$$T(n) = 4 + 1 + 1 + n + 1 + 2n + 1 + (n + 1)*(n) + n + n*n $$
$$T(n) = 8 + 4n + n^2 + n + n^2$$
$$T(n) = 2n^2 + 5n + 8$$
Therefore $T(n)$ is $O(n^2)$, copy constructor is quadratic.

# Analysis of move constructor
Let n represents the total number of records in the table and lets assume that rhs table has the same number of records as current table.<br>
Let $T(n)$ be number of operations in move constructor<br>

Now lets count the number of operations in move constructor:
```cpp
template <class TYPE>
SimpleTable<TYPE>::SimpleTable(SimpleTable<TYPE>&& rhs){
    capacity_=rhs.capacity_;    //1
    records_=rhs.records_;      //1
    rhs.records_=nullptr;       //1
    rhs.capacity_=0;            //1
}
```
By adding the total number of operations we can derive the following equation:
$$T(n) = 1 + 1 + 1 + 1$$
$$T(n) = 4$$
Therefore $T(n)$ is $O(1)$, move constructor is constant and do not depend on total number of records in the table.
