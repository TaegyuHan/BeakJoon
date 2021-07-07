#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    int result; // 결과
    long A, //  임대료, 재산세, 보험료, 급여 등 A
         B, //  재료비와 인건비 등 총 B
         C, //  노트북 가격이 C
         temp;

    scanf("%d %d %d", &A, &B, &C);

    temp = C-B;

    if(temp <= 0)
    {   // 손익분기점이 존재하지 않으면 -1을 출력한다.
        printf("-1");
        return 0;
    }

    // 손익분기점을 구하는 부분
    result = (A / temp) + 1;

    printf("%d", result);  

    return 0;
}