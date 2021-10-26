# programming_part_3_lab_3
Hamsters

The pet store sells hamsters. These are peaceful domestic beings, however it turned out that they have interesting eating behavior.

In order to feed a hamster living alone, you need H packets of food for a day. However, if several hamsters live together, they wake up greedy. In this case, each hamster eats an additional G packets of food per day of each neighbor. The daily norm H and greed G are individual for each hamster.

There are only C hamsters in the store. You want to buy as much as possible, but you have there are only S packets of food per day. Determine the maximum number of hamsters you have you can feed.

Input data

The input file hamster_in.txt consists of C + 2 lines.

The first line contains S - daily food supply. 0 ≤ S ≤ 10^9
The second line contains C - the total number of hamsters on sale. 1 ≤ C ≤ 10^5
The next C lines contain H, G - integers separated by a space, which means daily norm and level of greed of each hamster. 0 ≤ H,G ≤ 10^9
Output data

The output file hamster_out.txt must contain one number - the maximum number of hamsters that you can feed by settling them together.

How to run

Download files from the repository

In console python main.py

Enter the name of input file

Check output file to see the result

To run tests: python -m unittest test.TestGreedy
