/* Safe input using fgets() for strings
 * Reads into char * line, up to LINE_LENGTH + EXTRA_SPACES characters
 */

        if(fgets(line, LINE_LENGTH + EXTRA_SPACES, stdin) == NULL 
            || line[strlen(needle)-1] != '\n')
        {
            printf("Input failed.\n\n");
            return EXIT_FAILURE;
        }
