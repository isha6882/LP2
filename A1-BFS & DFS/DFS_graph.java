import java.util.*;

public class DFS_graph {
    private int V;
    private LinkedList<Integer> adj[];

    DFS_graph(int v) {
        V = v;
        adj = new LinkedList[v];
        for (int i = 0; i < v; ++i)
            adj[i] = new LinkedList();
    }

    void addEdge(int v, int w) {
        adj[v].add(w);
    }

    void DFSUtil(int v, boolean visited[])
    {
        visited[v] = true;
        System.out.print(v + " ");
        Iterator<Integer> i = adj[v].listIterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visited[n])
                DFSUtil(n, visited);
        }
    }

    void DFS(int v)
    {
        boolean visited[] = new boolean[V];
        DFSUtil(v, visited);
    }

    int find(int s, int ver)
    {
        boolean visited[] = new boolean[V];

        LinkedList<Integer> queue = new LinkedList();

        visited[s] = true;
        queue.add(s);

        while (queue.size() != 0) {
            s = queue.poll();

            for(int l: adj[s]){
                if(visited[l] == false){
                    if(l == ver){
                        System.out.println("Found Vertex: " + ver);
                        return l;
                    }
                    queue.add(l);
                    visited[l] = true;
                }
            }
        }
        System.out.println("Vertex " + ver + " not found");
        return -1;
    }

    public static void main(String args[]) {
        graph g = new graph(6);

        g.addEdge(0, 1);
        g.addEdge(0, 3);
        g.addEdge(0, 4);
        g.addEdge(1, 2);
        g.addEdge(3, 5);
        g.addEdge(4, 5);

        System.out.println("\nDepth First Traversal:");
        g.DFS(0);

        Scanner sc = new Scanner(System.in);
        while(true){
            System.out.println("\nEnter vertex to find:");
            g.find(0, sc.nextInt());
        }
    }
}


/*
GRAPH:
        0
      / | \
     1  3  4
    /    \ /
   2      5
*/


/*
OUTPUT:

Depth First Traversal:
0 1 2 3 5 4
Enter vertex to find:
4
Found Vertex: 4

Enter vertex to find:
9
Vertex 9 not found

 */