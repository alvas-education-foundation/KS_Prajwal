  
import java.util.*;
import java.io.*;
public class Number_Bit {
	static void findNthNum(int N) 
	{ 
		int bit_L = 1, last_num = 0; 
		while (bit_L * (bit_L + 1) / 2 < N) { 
			last_num = last_num + bit_L; 
			bit_L++; 
		} 
		int bit_R = N - last_num - 1; 

		System.out.print((1 << bit_L) + (1 << bit_R) 
			+"\n"); 
	} 
	public static void main(String[] args) 
	{ 
		int N;
		Scanner s = new Scanner(System.in);
		System.out.print("Enter a number : ");
		N = s.nextInt();
		findNthNum(N); 
	} 
	} 