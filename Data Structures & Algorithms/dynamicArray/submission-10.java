class DynamicArray {
    private int[] arr;
    private int length;
    private int capacity;
    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.arr = new int[this.capacity];
        this.length = 0;
    }

    public int get(int i) {
        try {
            return arr[i];
        }
        catch (IndexOutOfBoundsException e) {
            System.out.print("error");
            return -1;
        }
    }

    public void set(int i, int n) {
         try {
            arr[i] = n;
        }
        catch (IndexOutOfBoundsException e) {
            System.out.print("error");
            
        }
    }

    public void pushback(int n) {
        if(length==capacity) {
            resize();
        }
        arr[length] = n;
        length++;
    }

    public int popback() {
        if(length !=0 ) {
            length--;
        }
        return arr[length];
    }

    private void resize() {
        this.capacity*=2;
        int[] newarr = new int[capacity];
        for(int i=0;i<length;i++) {
            newarr[i] = arr[i];
        }
        arr = newarr;
    }

    public int getSize() {
        return length;
    }

    public int getCapacity() {
        return capacity;
    }
}
