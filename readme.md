==Financial Independance Calculator (FIT) version 2==

Author : Andrew Brown

The FIT V.2 is used to calculate whether the user is financially stable enough to retire for x amount of years. Building from the first version, 
V.2 runs a Monte Carlo experiment to simulate real life flucuations in inflation and interest rates.

User input:

 - How much they spent last year
 - Current inflation rate (2% = 0.02)
 - How much savings the user has
 - Current interest rate for savings (5% = 0.05)
 - How many years they want to test for

New for V.2:

 - Maximum change in inflation rate %
 - Maximum change in interest rate %
 - Number of simulations to run

The output of each test is exported into a text file called output.txt. The format of the text file file is the balance for each year for each 
simulation, and if the balance for the last year is positive it will print "successful", and unsuccesful if the balance is negative.

The console will output how many successful simulations are returned with a percentage of the total simulations.