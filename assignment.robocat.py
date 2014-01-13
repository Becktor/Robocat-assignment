#
# Robocats assignment
#
# Jonathan Becktor              (JonathanBecktor@gmail.com)
#

from itertools import permutations
import csv


def openmatrix():
	matrix = []												#list to store in
	filename=raw_input('enter filename of matrix file: ')	#what file
	with open(filename) as inputfile:						#open file
	    for row in csv.reader(inputfile):					#loops throug every row
	        matrix.append(map(int,row))						#appends every row to new list 
	return matrix       									#and stores it as an integer
def calc(matrix) :										
	smallest = 0
	permus = list(permutations(matrix))						#finds all permutations of the matrix
	for x in xrange(1,len(permus)):							#loop through all permutations
		sum = 0												
		for y in xrange(0,len(permus[x])):					#calc sum of diagonal for permutation
			sum = sum + permus[x][y][y]
		if sum < smallest or smallest == 0:					#check if smaller than the smallest sum
			smallest = sum
	print smallest

def main():
	
	calc(openmatrix())  

if __name__ == '__main__':
    main()