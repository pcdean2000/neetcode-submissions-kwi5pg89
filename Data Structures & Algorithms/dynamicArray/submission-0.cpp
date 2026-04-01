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
        if (i < m_length)
        {
            return m_array[i];
        }
        return 0;
    }

    void set(int i, int n) {
        if (i < m_length)
        {
            m_array[i] = n;
        }
    }

    void pushback(int n) {
        if (m_length == m_capacity)
        {
            resize();
        }

        m_array[m_length] = n;
        ++m_length;
    }

    int popback() {
        if (m_length > 0)
        {
            --m_length;
            return m_array[m_length];
        }
        return 0;
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
