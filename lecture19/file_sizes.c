/* file_sizes.c */

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    for (int i = 1; i < argc; i++) {
        struct stat s;

        /* Get file meta-data */
        if (stat(argv[i], &s) < 0) {
            fprintf(stderr, "Unable to stat %s: %s\n", argv[i], strerror(errno));
            return EXIT_FAILURE;
        }

        /* Check if directory */
        if (S_ISDIR(s.st_mode)) {
            printf("%s is a directory\n", argv[i]);
        }
        
        /* Check if file is executable */
        if (s.st_mode & S_IXUSR) {
            printf("%s is executable by the user\n", argv[i]);
        }

        /* Display file size in bytes */
        printf("%s size is %ld bytes\n", argv[i], s.st_size);
    }

    return EXIT_SUCCESS;
}

/* vim: set sts=4 sw=4 ts=8 expandtab ft=c: */
