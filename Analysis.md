
# 6. Analysis of copy constructor
Lets assume that rhs table has the same number of records as current table, which is equal to n.

Now lets count the number of operations in copy constructor:
```cpp
template <class TYPE>
SimpleTable<TYPE>::SimpleTable(const SimpleTable<TYPE>& rhs){
    records_=new Record*[rhs.capacity_+1];      //4
    capacity_=rhs.capacity_;                    //1
    for(int i=0;i<capacity_+1;i++){             //1+n+1+n, for worst case scenario lets assume that capacity is equal to number of records
                                                //which means table is full, so capacity_ will be equal to n.
        records_[i]=nullptr;                    //2n, 2 operations and loop will run n times
    }   
    for(int i=0;i<rhs.numRecords();i++){        //1 + (n+1)(n) + n - we know that time complexity of numRecords is O(n), 
                                                //so it will take n operations for numRecords with some constants.
        update(rhs.records_[i]->key_,rhs.records_[i]->data_);       // n * (n) - we know that time complexity of update() is O(n), if item does not exist.
    }
}
```
By adding the total number of operations we can derive the following equation:
$$T(n) = 4 + 1 + 1 + n + 1 + n + 2n + 1 + (n + 1) \times (n) + n + n \times n $$
$$T(n) = 4 + 1 + 1 + n + 1 + 3n + 1 + n^2 + n + n + n^2$$
$$T(n) = n^2 + n^2 + n + 3n + 2n + 6 + 2$$
$$T(n) = 2n^2 + 6n + 8$$
Therefore $T(n)$ is $O(n^2)$, copy constructor is quadratic.

# 7. Analysis of move constructor
Lets assume that rhs table has the same number of records as current table, which is equal to n.<br>

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

# 8. Move Assignment operator
Lets assume that rhs table have the same number of records as current table, which are equal to n.

Now lets count the number of operations:
```cpp
template <class TYPE>
const SimpleTable<TYPE>& SimpleTable<TYPE>::operator=(SimpleTable<TYPE>&& rhs){
    if(records_){                           //2
        while(numRecords() != 0){           //1 + n(n + 1), we know that time complexity of numRecords() is O(n), 
                                            //so, number of operatoins for numRecords will be n and some constant.
                                            
            remove(records_[0]->key_);      //n(n^2+2), we know that time complexity of remove(), if item is there, is O(n^2). 
                                            //so, number of operations for remove functions will be n^2 and some constant, 
                                            //Loop will run n times and remove have n^2 operations, so it will be n*n^2 
        }
        delete [] records_;                 //1
    }
    records_=rhs.records_;                  //1
    capacity_=rhs.capacity_;                //1
    rhs.records_=nullptr;                   //1
    rhs.capacity_=0;                        //1

    return *this;                           //1
}
```
By adding all the operations we can derive the following equation:
$$T(n) = 2 + n(n + 1) + n(n^2 + 2) + 1 + 1 + 1 + 1 + 1 + 1$$
$$T(n) = 2 + n(n + 1) + n(n^2 + 2) + 6$$
$$T(n) = 2 + n^2 + n + n^3 + 2n + 6$$
$$T(n) = n^3 + n^2 + 2n + n + 6 + 2 $$
$$T(n) = n^3 + n^2 + 3n + 8$$
Therefore, $T(n)$ is $O(n^3)$, move assignment operator is cubic. 

# 9. Destructor
Lets count the number of operations:
```cpp
template <class TYPE>
SimpleTable<TYPE>::~SimpleTable(){
    if(records_){                   //1
        int sz=numRecords();        //1
        for(int i=0;i<sz;i++){      //1 + (n + 1) + n
            remove(records_[0]->key_);  // n(n^2 + 2) we know that time complexity of remove(), if item is there, is O(n^2). 
                                        //so, number of operations for remove functions will be n^2 and some constant, 
                                        //Loop will run n times and remove have n^2 operations, so it will be n*n^2 
        }
        delete [] records_;         //1
    }
}
```
By adding all the operations we can derive the following equation:
$$T(n) = 1 + 1 + 1 + (n + 1) + n + n(n^2 + 2) + 1$$
$$T(n) = 3 + n + 1 + n + n(n^2 + 2) + 1$$
$$T(n) = 2n + 4 + n^3 + 2n + 1$$
$$T(n) = n^3 + 4n + 5$$
Therefore, T(n) is O(n^3), destructor is cubic.
