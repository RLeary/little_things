void xor_swap(int * first, int * second)
{
  if(first != second)
    {
      *first ^= *second;
      *second ^= *first;
      *first ^= *second;
    }
}
