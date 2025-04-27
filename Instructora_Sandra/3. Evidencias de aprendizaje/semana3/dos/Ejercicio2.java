package semana3.dos;
import javax.swing.JOptionPane;
public class Ejercicio2 {

    public static void main(String[] args) {
        
        
        // Array
        int[] array = {1, 2, 3, 4, 5};
        JOptionPane.showMessageDialog(null, "Array: " + java.util.Arrays.toString(array));

        // ArrayList
        java.util.ArrayList<Integer> arrayList = new java.util.ArrayList<>();
        arrayList.add(1);
        arrayList.add(2);
        arrayList.add(3);
        JOptionPane.showMessageDialog(null, "ArrayList: " + arrayList);

        // LinkedList
        java.util.LinkedList<Integer> linkedList = new java.util.LinkedList<>();
        linkedList.add(1);
        linkedList.add(2);
        linkedList.add(3);
        JOptionPane.showMessageDialog(null, "LinkedList: " + linkedList);

        // HashMap
        java.util.HashMap<String, Integer> hashMap = new java.util.HashMap<>();
        hashMap.put("one", 1);
        hashMap.put("two", 2);
        hashMap.put("three", 3);
        JOptionPane.showMessageDialog(null, "HashMap: " + hashMap);

        // HashSet
        java.util.HashSet<Integer> hashSet = new java.util.HashSet<>();
        hashSet.add(1);
        hashSet.add(2);
        hashSet.add(3);
        JOptionPane.showMessageDialog(null, "HashSet: " + hashSet);

        // Stack
        java.util.Stack<Integer> stack = new java.util.Stack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        JOptionPane.showMessageDialog(null, "Stack: " + stack);

        // Queue
        java.util.Queue<Integer> queue = new java.util.LinkedList<>();
        queue.add(1);
        queue.add(2);
        queue.add(3);
        JOptionPane.showMessageDialog(null, "Queue: " + queue);

        // PriorityQueue
        java.util.PriorityQueue<Integer> priorityQueue = new java.util.PriorityQueue<>();
        priorityQueue.add(3);
        priorityQueue.add(1);
        priorityQueue.add(2);
        JOptionPane.showMessageDialog(null, "PriorityQueue: " + priorityQueue);
    }

    

}
