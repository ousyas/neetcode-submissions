class MinStack {
    private List<Integer> stack;
    private List<Integer> min;
    public MinStack() {
        this.stack = new ArrayList<>();
        this.min = new ArrayList<>();
    }
    
    public void push(int val) {
        stack.add(val);
        if (min.size() == 0){
            min.add(val);
        }
        else {
            if (val <= min.get(min.size()-1)){
                min.add(val);
            }
        }
    }
    
    public void pop() {
        System.out.println(min.get(min.size()-1));
        System.out.println(stack.get(stack.size()-1));
        if (stack.get(stack.size()-1).equals(min.get(min.size()-1))){
            System.out.println(min.get(min.size()-1));
            min.remove(min.size()-1);
        }
        stack.remove(stack.size()-1);      
    }
    
    public int top() {
        return stack.get(stack.size()-1);
    }
    
    public int getMin() {
        return min.get(min.size()-1);
    }
}
