import json, itertools

total = 1
seq = input("Enter the aminoacid sequence:")

def isPalindrome(s):
    return s == s[::-1]

with open('tab.json', 'r') as f:
	codon_table = json.load(f)


def get_count(json_object, abbr):
	for dict in json_object:
		if dict['abbr'] == abbr:
			return dict['count']

def get_array(json_object,abbr):
	for dict in json_object:
		if dict['abbr'] == abbr:
			d = dict['codons']

			if get_count(json_object,abbr) > 1:
				x = d.split(".")

				return x
			else:
				return d

def subsequences(iterable, length):
	return [iterable[i: i + length] for i in range(len(iterable) - length + 1)]


for co in seq:
	if type(get_count(codon_table,co)) == type(None):
		print("Sequence is wrong!")
		exit()
	total = total * get_count(codon_table,co)

opt1 = input("Write all DNA primer combinations?(Y/n)")
maxlim = int(input("Max primer length:")) + 1
if maxlim > (total+1):
	maxlim = total + 1
elif maxlim < 4:
	maxlim = 4

def pr_sub(tt):
	for t in subsequences(seq,tt):

		dnax = []

		tot = 1
		for d in t:
			tot = tot * get_count(codon_table,d)
			dnax.append(get_array(codon_table,d))
		if (tot < 72) and (seq.count(t) == 1) and (isPalindrome(t) == 0):
			print(t + ": " + str(tot))
			if opt1 == "Y":
				dnaseq_all = list(itertools.product(*dnax))
				print(dnaseq_all)


for i in range(3,maxlim):
	pr_sub(i)

print("Total combinations: " + str(total))