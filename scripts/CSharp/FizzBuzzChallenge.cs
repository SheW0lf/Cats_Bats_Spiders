// Author: Garfield Lee
// Language: C#
// Github: https://github.com/Garfield550

using System;

namespace FizzBuzzChallenge
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 100; i++)
            {
                var isAnimal = CheckAnimal(i, out string animal, out int number);

                if (isAnimal)
                {
                    Console.WriteLine(animal);
                } else 
                {
                    Console.WriteLine(number);
                }
            }
        }

        private static bool CheckAnimal(int input, out string animal, out int number)
        {
            var mul3 = input % 3;
            var mul5 = input % 5;

            animal = "";
            number = input;

            if (mul3 == 0)
            {
                if (mul5 == 0)
                {
                    animal = "Spiders";
                    return true;
                }

                animal = "Cats";
                return true;
            }

            if (mul5 == 0)
            {
                animal = "Bats";
                return true;
            }

            return false;
        }
    }
}
