
#Example implementation of Punnett Squares following MENDELIAN GENETIC INHERITANCE (Laws of Independent Assortment and Segregation used). Multiple features such
#   as: multiple alleles, codominance, and special exceptions to the order in which genes are displayed (appension of gene names). A dataset with 3 gene examples
#   (A, B, O blood types with AB codominance, Rhesus (Rh) Factor with displayed name appension to blood types', and fly eye colours with many alleles) are provided.
#   
#   Run the script in a python runtime after editting the data to your own liking. Enjoy!

#Lucas Benjik, 2023. NBCC.


#We define genes below. Edit the following format to add or remove genes, including multiple features such as codominance, multiple alleles, and paired genes (which
#   append themselves onto other genes IN OUTPUT ONLY*--see Rh Factor example.)
#   
#   Remember to include } endings to { beginnings and commas between items in the table (all objects after the first one have these!)
#   
#   *As this is MENDELIAN INHERITANCE, all genes are randomly put into a table and assorted independently (Law of Independent Assortment) EVEN THOUGH we know this is
#   not always the case (some genes might assort together, in non-random patterns in the real world). FOR THIS IMPLEMENTATION (ad hoc), all genes mix together in a
#   collective "soup" and come out the other side in full-random, all-possible-combination patterns, according to Mendel's theory. This is the aim that this script
#   was created for ad hoc, and so is...not necessarily or very flexible. I would change many things ultimately, with this. (Besides the mess of certain classes.)
#   (This footnote [*] is a post-NBCC remark written for my portfolio. The rest was here before. Extendedly: known issues & limitations will be posted on GitHub.)

##vvvv#################################################vvvv##

genes = {
    #"Gene Name": {
    "Pea Colour": {
        "G": ["G", 0],
        "g": ["g", 1]
        },
    "Pea Roundness": {
        "R": ["R", 0], #round
        "r": ["r", 1] #wrinkled
        }
    }


genotype_1 = {
    #"Gene Name": ["Allele Name", "Allele Name"]
    "Pea Colour": ["G", "g"],
    "Pea Roundness": ["r", "r"]
}

genotype_2 = {
    "Pea Colour": ["G", "g"],
    "Pea Roundness": ["R", "r"]
}


##^^^^#################################################^^^^##

print("\nSuccessful input!")

#Everything below this point is something which you should probably not mess with, unless you really really want to; however be warned: this may ruin or mess
#   up the functionality of this script. Attempt to save a backup copy before you mess with the functions below if you really want to experiment with how the
#   functionality works. All you need to do is edit the "genes = {...}" and, "genotype_1 = {...}" and "genotype_2 = {...}" tables in the above section, and
#   the script below will work on its own in a python runtime enviornment. :D

class Genome: #(completely unoptimized methods, irrelevant; not run-time friendly or anything like a videogame. It's okay for this case.)
    def __init__(self, alleles):
        self.Genes = alleles
    
    def append(self, genes):
        for gene, alleles in genes.items():
            if gene in self.Genes:
                self.Genes[gene] = self.Genes[gene] + alleles
            else:
                self.Genes[gene] = alleles
           
    def haploids(self):
        gametes = []
        names = []
        
        for gName in self.Genes.keys():
            names = names + [gName]
        
        def iterate_genes(i, alleles):
            for allele in self.Genes[names[i]]:
                continutedAlleles = alleles.copy()
                continutedAlleles[names[i]] = [allele]
                if (i + 1) < len(names):
                    iterate_genes(i + 1, continutedAlleles)
                else:
                    gametes.append(Genome(continutedAlleles))
        
        iterate_genes(0, {})
        
        return gametes
        
    def output(self):
        outputGenes = {}
        
        for sName, sGene in self.Genes.items(): #reformatting
            gene = genes[sName]
            if gene:
                outputGenes[sName] = {}
                i = 0
                for sAllele in sGene:
                    allele = gene[sAllele]
                    if allele:
                        outputGenes[sName][i] = [allele.copy()] #in a list for string appension behaviour
                    i = i + 1
        
        for sName, sGene in self.Genes.items(): #appending
            gene = genes[sName]
            if gene:
                i = 0
                for sAllele in sGene:
                    allele = gene[sAllele]
                    if allele and len(allele) > 2:
                        if allele[2] in outputGenes:
                            appendToGene = outputGenes[allele[2]]
                            if i in appendToGene:
                                appendToGene[i] = appendToGene[i].copy()[0:] + [allele.copy()] #string appension implementation
                                del outputGenes[sName][i]
                            else: #if 1-to-1 mapping does not work, append to end of gene to append to
                                appendToGene[max(appendToGene)] = appendToGene[max(appendToGene)].copy()[0:] + [allele.copy()]
                                del outputGenes[sName][i]
                    i = i + 1
                if len(outputGenes[sName]) <= 0:
                    del outputGenes[sName]
        
        for oName, oGene in outputGenes.copy().items(): #dominance. an issue is with "A^+B" cases
            outputGenes[oName] = {}
            for i, oPairedAlleles in oGene.items():
                weight = 0
                oString = []
                for oAllele in oPairedAlleles:
                    weight = weight + oAllele[1]
                    oString = oString + [oAllele]
                if weight in outputGenes[oName]:
                    outputGenes[oName][weight] = outputGenes[oName][weight] + [oString]
                else:
                    outputGenes[oName][weight] = [oString]
                    
        
        outputString = ""
        
        for oGene in outputGenes.values():
            for _, orderedAlleles in sorted(oGene.items()):
                last = None
                pairedAllelesIndex = 0
                for pairedAlleles in orderedAlleles:
                    independentAlleles = len(pairedAlleles) #for the 'carry over' in cases like "A^+B" to "AB^+" ideally
                    if last == None:
                        last = pairedAlleles
                    elif (len(last) - independentAlleles) > 0:
                        for i in range(len(last) - independentAlleles):
                            pairedAlleles.append(last[independentAlleles])
                            del last[independentAlleles] #...takes care of needing the i
                            #potential error is if we have "A^+_1" and "A_1" and move the 'overflow' to "A^+" and "A_1_1"... multiple appensions beware! (..needs a solution).
                    else:
                        last = pairedAlleles
                    pairedAllelesIndex = pairedAllelesIndex + 1
                for pairedAlleles in orderedAlleles:
                    for independentAllele in pairedAlleles:
                        outputString = outputString + independentAllele[0]
        
        return outputString
        
    def phenotype(self):
        
        phenoGenome = Genome({})
        
        for sName, sGene in self.Genes.items():
            gene = genes[sName]
            if gene:
                dominantAlleles = []
                for sAllele in sGene:
                    allele = gene[sAllele]
                    if allele:
                        if len(dominantAlleles) > 0:
                            if dominantAlleles[0][1] > allele[1]:
                                dominantAlleles = [[sAllele, allele[1]]]
                            elif dominantAlleles[0][1] == allele[1] and not ([sAllele, allele[1]] in dominantAlleles):
                                dominantAlleles.append([sAllele, allele[1]])
                        else:
                            dominantAlleles.append([sAllele, allele[1]])
                for allele in dominantAlleles:
                    phenoGenome.append({sName: [allele[0]]})
        
        phenoString = phenoGenome.output()
        
        return phenoString

class AssortedGenome:
    def __init__(self, genome_1, genome_2):
        self.Genome1 = genome_1
        self.Genome2 = genome_2
        self.Square = [] #will contain all genomes possible from the two haploid gametes
        self.Phenotypes = {}
        y = 0
        for gamete1 in genome_1:
            self.Square.append([])
            x = 0
            for gamete2 in genome_2:
                self.Square[y].append(Genome(gamete1.Genes.copy()))
                self.Square[y][x].append(gamete2.Genes.copy()) #that's a lotta copies, dunno if they're needed but it's safe ¯\_(ツ)_/¯ That's how it's done. (Future me: as in less error-prone. obviously more unoptimized)
                
                phenotype = self.Square[y][x].phenotype()
                offspring = self.Square[y][x].output()
                
                self.Phenotypes[offspring] = phenotype
                
                self.Square[y][x] =  offspring
                x = x + 1
            y = y + 1
    
    def output(self):
        #just gonna probe for longest and maxX (square width); (not familiar [intimately so,] with python arrays--dunno if 'in' checking would be a/the better way to do it/would work?).
        longest = 0
        maxX = 0
        for row in self.Square:
            X = len(row)
            if X > maxX:
                    maxX = X
            for column in row:
                length = len(column)
                if length > longest:
                    longest = length
        
        outputString = ""
        
        lwBufferLen = 1
        
        outputString = "".center(longest + 2)
        
        for gamete2 in self.Genome2:
            outputString = outputString + "|" + gamete2.output().center(longest + 2)
        
        width = len(outputString)
        
        y = 0
        for gamete1 in self.Genome1:
            columnDividers = "".center(longest + 2)
            for x in range(maxX):
                columnDividers = columnDividers + "|" + "".center(longest + 2)
            
            outputString = outputString + "\n" + columnDividers + "\n" + "".center(width + 2, "-") + "\n" + columnDividers + "\n" + gamete1.output().center(longest + 2)
            for offspring in self.Square[y]:
                outputString = outputString + "|" + offspring.center(longest + 2)
            y = y + 1
        
        return outputString, width
    
    def ratios(self):
        genotype_ratios = {}
        phenotype_ratios = {}
        
        for row in self.Square:
            for offspring in row:
                if offspring in genotype_ratios:
                    genotype_ratios[offspring] = genotype_ratios[offspring] + 1
                else:
                    genotype_ratios[offspring] = 1
                if offspring in self.Phenotypes:
                    phenotype = self.Phenotypes[offspring]
                    if phenotype in phenotype_ratios:
                        phenotype_ratios[phenotype] = phenotype_ratios[phenotype] + 1
                    else:
                        phenotype_ratios[phenotype] = 1                    
        
        genotype_ratioString = []
        phenotype_ratioString = []
        
        def iterate(ratios, ratioSring):
            for phenotype, amount in ratios.items():
                ratioSring.append(str(amount) + " " + phenotype) #interesting python phenomenon with mutability vs immutability here...(list vs string used)
        
        iterate(genotype_ratios, genotype_ratioString)
        iterate(phenotype_ratios, phenotype_ratioString)
        
        return {"Genotype": " : ".join(genotype_ratioString), "Phenotype": " : ".join(phenotype_ratioString)}

genome_1 = Genome(genotype_1)
genome_2 = Genome(genotype_2)

genome_1_output = genome_1.output()
genome_2_output = genome_2.output() #because the class doesn't cache or anything, saving them for later (as they are to be used twice).

genome_1_haploids = genome_1.haploids()
genome_2_haploids = genome_2.haploids()

assortedGenome_3 = AssortedGenome(genome_1_haploids, genome_2_haploids)
punnett_square, psLength = assortedGenome_3.output()

print("\n", ("Genotype #1: " + genome_1_output).center(psLength))
print("\n", ("Genotype #2: " + genome_2_output).center(psLength))

hint1 = "(Reminder that ^ means superscript and _ means subscript in the output.)"
if len(hint1) < psLength:
    hint1 = hint1.center(psLength)

print("\n", hint1)

title = "Punnett Square for: " + genome_1_output + " + " + genome_2_output
if len(title) < psLength:
    title = title.center(psLength)

print("\n\n", title, "\n")
print(punnett_square)
print("\n\nPunnett Square Successfully Calculated! Here are the ratios as the following:")

punnett_ratios = assortedGenome_3.ratios()
print("\n\nGenotype ratio:\n\n", punnett_ratios["Genotype"])

print("\n\nPhenotype ratio:\n\n", punnett_ratios["Phenotype"])

print("\n\n(This script only accounts for dominant, codominant, and recessive phenotypic expressions. See the outputted genotypes for help deducing polygenic, complementary, pleiotropic, and other genotype-phenotype interactions that might arise. Good luck!)")
