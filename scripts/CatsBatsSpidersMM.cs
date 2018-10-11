//  Author: Michael McClean
//  Language: C#
//  Github: https://github.com/mdmcclean

using System;

namespace CatsBatsSpiders
{
    class CatsBatsSpidersMM
    {
        static void Main(string[] args)
        {
            string cats = "cats";
            string bats = "bats";
            string spiders = "spiders";

            string output;

            for(int i = 1; i <= 100; i++)
            {
                if(i % 3 == 0 && i % 5 == 0)
                {
                    output = spiders;
                }
                else if(i % 3 == 0)
                {
                    output = cats;
                }
                else if(i % 5 == 0)
                {
                    output = bats;
                }
                else
                {
                    output = i.ToString();
                }

                Console.WriteLine(output);
            }

            Console.ReadKey();
        }
    }
}
