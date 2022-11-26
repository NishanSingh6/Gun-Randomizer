
# Analysis of move constructor
Let n represents the total number of records in the table and lets assume that rhs table has the same number of records as current table.<br>
Let $T(n)$ be number of operations in move constructor<br>

Now lets count the number of operations in move constructor:
```
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
