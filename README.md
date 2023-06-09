# Mendelian-Punnett-Squares
Full random assortment of genes (Mendelian) in a Punnett Square. Matrix multiplication w/ extra steps.

Incredibly Simple Mendelian Inheritance in a python script. Made for biology class (as a homework tool). Due to this ad hoc nature, it is specific (ad hoc!), and not incredibly flexible.

![image](https://raw.githubusercontent.com/PeachDoughnut/Mendelian-Punnett-Squares/main/basic_expected_output.png)

Features:
  1. Matrix multiplication with extra steps - randomly assorts (Mendelian assortion) string-like objects (genes) in a matrix, with particular strings (alleles) always partnered together (exception: see point 5.) E.g.: "R" + "Y" + "y" + "r" = "RrYy" and not "RYyr" (R/r alleles are always part of the "R" gene regardless, in the string output alleles are represented as being written side-by-side. I.e. "R" + "Y" + "y" + "r" = "Rr" + "Yy" == "RrYy"). Unlike numerical multiplication which is commutative and where in that sense orders simply get lost in matrix multiplication.
  2. Phenotype - compared to the genotype (just all children: e.g. "RRYy"), the phenotype removes duplicates and invokes dominances of particular alleles. Some alleles (like "Y" and "y") are dominant over another (such as "Y" taking priority over "y'"). Combined e.g.: "RRYy" becomes "RY". Another e.g.: "Rryy" becomes "Ry".
  3. Codominance - when dominance value is equal, the phenotype displays both. E.g., if "y"'s dominance == "Y"'s, then "RRYy" becomes "RYr". Typical example is with ABO blood types, e.g.: "AO" + "BB" = "AB" (where "A" and "B" are codominant, "O" is less dominant).
  4. Many alleles - this just means more than two alleles can be present: like A, B, and O. Not just two. (Fundamental part of python's lists...)
  5. String name appension - some genes should be placed together IN OUTPUT (not changing the fact that it is randomly mixed & sorted): e.g. "A" + "^+" + "B" + "^-" = "A^+B^-" and NOT "AB^+^-". If the initial table has corresponding objects in what it is to be appended to (i.e. two children as in "A" and "B", and "^+" and "^-", then it will preserve that order in this name-appension feature. If not, then it will just annex to the end or produce unpredictable behaviour. I believe I tried to support some of this--but it wasn't the main focus and they are really like annexes to this code--producing spaghetti code.)
  6. Analysis at the end that produces ratios of said genotypes and phenotypes.

Limitations & known issues:
  1. Multiple appensions onto the same gene. E.g. in main script: if a second gene object is appended onto the blood type BESIDES Rh factor (such as another n-factor antigen), then it breaks down.
  2. Appensions onto appensions. E.g.: if you were to append something onto the Rh factor, too, on the main script.
  3. Non-Mendelian sorting - there is no way to make two genes sort together. I.e. Rh factor does not sort with ABO blood type as one object. As they are on separate chromosomes (chrom. 1 and chrom. 9) this is appropriate, anyway.

Examples:

  Base - three genes: ABO blood type, Rhesus factor, and fruit fly eye colours (E sub 1 through 4). In this example, also, Rh factor is appended onto the blood type gene, and thus outputs as so.

(Pictured in the top image.)
![image](https://raw.githubusercontent.com/PeachDoughnut/Mendelian-Punnett-Squares/main/basic_expected_output.png)

  Example 1 - two genes: ABO blood type, and Rhesus factor. It is the base example without the fruit fly eye colour mixed in.
![image](https://raw.githubusercontent.com/PeachDoughnut/Mendelian-Punnett-Squares/main/ex1_expected_output.png)

  Example 2 - two genes: dog coat colour and the epistatic albinism factor. Epistatic phenotypic effects are another type not represented in the end phenotypic output ratio and have to be deduced manually from the genotype. I.e.: ALL genotypic outcomes with "aa" shall end up albino.
![image](https://raw.githubusercontent.com/PeachDoughnut/Mendelian-Punnett-Squares/main/ex2_expected_output.png)

  Example 3 - two genes: pea colour and pea roundness. Basic punnett square of which I was forced to complete tens of - forcing me to make this script.
![image](https://raw.githubusercontent.com/PeachDoughnut/Mendelian-Punnett-Squares/main/ex3_expected_output.png)

Future:

This would/should/could be remade in a way more modular, sane system. But, it was made ad hoc, and in a single night (initially) with a second night to bug fix. The last time I edited this was to clean up comments for publication on GitHub. Made for a Grade 12 biology class.

Functions are not small enough, the functions are too big and unwieldy. Classes could be improved majorly: they should cache results, possibly store data in a consistant stucture rather than coverting them to different kinds of tables function-to-function.
