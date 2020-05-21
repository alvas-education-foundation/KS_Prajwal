import java.util.Scanner;
import java.io.*;

public class Dup {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        
            System.out.println("enter a size of array");
            int n=sc.nextInt();
            int[] b=new int[n];
            System.out.println("enter a array elements");
            for(int i=0;i<n;i++)
            {
                b[i]=sc.nextInt();
            }
            int flag = 0;
            for(int i=0;i<n;i++)
            {
                for(int j=i+1;j<n;j++)
                {
                    if(b[i]==b[j])
                    {
                        System.out.println(b[j]);
                        flag = 1;
                    }
                }
            }
            
            if(flag==0) 
            {
                System.out.println("-1");
            }
        }
    }

