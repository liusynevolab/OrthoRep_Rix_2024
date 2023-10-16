# 2022-05-19_TPDNAP-epPCR3

## Experiment

3rd round of error prone PCR for TPDNAP directed evolution. Error prone PCR with the Trixy polymerase as the template was used to generate a ~786k member library in yeast encoding a ura3*-trp5* p1. This library was then subject to selection for both ura3 and trp5 either immediately and simultaneously (UW) or sequentially with ura3 selection followed by trp5 selection. UW-derived clones thus likely underwent fewer generations. Colonies were picked into 96 well blocks, grown to saturation, and immediately sequenced. Both the polymerase and p1 sequences in each block were sequenced. Based on prior results indicating that the mutations per sequence at the first timepoint generally correlates pretty well with the overall mutation rate, we did not sequence a second timepoint.

## Analysis

The same barcode pairs were used for both TPDNAP sequencing and p1 sequencing, so the TPDNAP sequencing was first used to assign a polymerase identity to barcode pairs, and the resulting barcodeGroups.csv file was used to demultiplex the p1 sequencing. Analysis beyond this point was performed mostly manually, see 'mutation-stats-manual-analysis.ods'. Brown used to denote polymerases only identified in a single well, while colors used to denote polymerases identified in more than one well.

## Results

Having already identified multiple polymerases capable of 10^-4 mutation rates, we were most interested in identifying mutations that might raise the rate of the most rare substitution type, A:T->C:G. We identified N449D (highest unique A->C mutations/sequence) and K777T (K7777 mutated in several contexts, only K777T was found alone, and K777T was near the highest A->C mutations/sequence) as candidates for this purpose. We also identified F702I-I761L-I863V and E266D-Q598K-N713S as potential high general mutator phenotypes. In retrospect, D347N-E569A may have also been a good choice of general mutator as well, as this mutant was derived from the simultaneous UW selection, which is a very challenging selection to survive, and may have also been subject to fewer generations of growth, yet was still among the polymerases that exhibited the highest mutations per sequence.

