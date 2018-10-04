/// Author: Teerapong Tienkul
/// Language: C#
/// Github: https://github.com/teerapongt

using System;

namespace Cats_Bats_Spiders
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0 & i % 5 == 0)
                {
                    Console.WriteLine("Spiders");
                }
                else if (i % 3 == 0)
                {
                    Console.WriteLine("Cats");
                }
                else if (i % 5 == 0)
                {
                    Console.WriteLine("Bats");
                }
                else
                {
                    Console.WriteLine(i);
                }
            }
        }
    }
}
