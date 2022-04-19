import math

input = 78

# # 파이썬 풀이1번
answer=[]
finish_num=int(math.sqrt(input))
for i in range(1,finish_num):
    if input%i==0:
        print(i)
        answer.append(i)
        answer.append(int(input/i))
answer.sort()
print(answer)
# ###

# int count=0;

# for(int i=1;i<=sqrt(input);i++)
# {
#     if (input%i==0)count++;
# }
# int* array = new int[count];

#  std::cout << "Enter a positive integer: ";
#  int length;
#  std::cin >> length;
#  int *array = new int[length];
#  // 배열 버전 new 연산자를 사용한다.
#  배열 길이는 상수가 아니여도 된다.
#  std::cout << "I just allocated an array of integers of length " << length << '\n';
#  array[0] = 5; 
#  // 요소 0을 값 5로 설정 delete[] array;
#  // 배열 할당 해제를 위해 배열 버전 delete 연산자를 사용한다.
#  return 0



# 파이썬 풀이2번

# for i in range(1,input+1):
#     if input%i==0:
#         print(i,end=" ")

# # c++ 풀이2번
# for(int i=1;i<=input;i++)
# {
#     if(input%2==0)print(input);
# }




