/* Graceful opening and closing of files in C - safely close the program
 * instead of crashing or causing errors and bugs
 */

#include <stdlib.h>

/* Graceful read open
 */
FILE * gropen(char * fname)
{
  FILE * fp;
  if((fp = fopen(fname, "r")) == NULL)
    {
      perror("Failed to open file for read");
      exit(EXIT_FAILURE);
    }
  return fp;
}

/* Graceful write open
 */
FILE * gwopen(char * fname)
{
  FILE * fp;
  if((fp = fopen(fname, "w")) == NULL)
    {
      perror("Failed to open file for write";
      exit(EXIT_FAILURE);
    }
  return fp;
}
