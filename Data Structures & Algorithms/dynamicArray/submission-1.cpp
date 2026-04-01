class DynamicArray {
private:
    int m_capacity;
    int m_length;
    int *m_array;

public:

    DynamicArray(int capacity) {
        m_capacity = capacity;
        m_length = 0;
        m_array = new int[m_capacity];
    }

    int get(int i) {
        return m_array[i];
    }

    void set(int i, int n) {
        m_array[i] = n;
    }

    void pushback(int n) {
        if (m_length == m_capacity) resize();

        m_array[m_length] = n;
        ++m_length;
    }

    int popback() {
        if (m_length > 0) --m_length;
        return m_array[m_length];
    }

    void resize() {
        m_capacity *= 2;
        int *newArray = new int[m_capacity];
        for (int i = 0; i < m_length; ++i)
        {
            newArray[i] = m_array[i];
        }
        m_array = newArray;
    }

    int getSize() {
        return m_length;
    }

    int getCapacity() {
        return m_capacity;
    }
};
