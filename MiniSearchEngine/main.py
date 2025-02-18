
root = "F:/Programming/Python/MiniSearchEngine/"
# file = open(root+"text.txt","r")
# content = file.read()
# print(content)
# file.close()

doc_list= []
number_of_docs = input("How many files do you have? ")
for i in range(int(number_of_docs)) :
  file_name = input("Enter the name of the file: ")
  file = open(root+file_name,"r")
  content = file.read()
  doc_list.append(content)
  file.close()

for i in doc_list:
  print(i)

terms = sorted(set(" ".join(doc_list).split())) 
print(terms)

matrix = [[0 for _ in range(len(terms))] for _ in range(int(number_of_docs))]


for i in range(len(doc_list)):
  for j in range(len(terms)):
    if terms[j] in doc_list[i]:
      matrix[i][j] = 1

for i in range(len(matrix)):
  print(matrix[i])
related_docs = []
print("documents indexed successfully, you can now perform queries")
query = input("Enter a word to look for: ")
if(query not in terms) :
  print(f"the word {query} doesn't exist in any document")
else:
  word_index = terms.index(query)
  for i in range(len(matrix)):
    if matrix[i][word_index] == 1:
      related_docs.append(i+1)

print(len(matrix))    
print(f"the word {query} was found in docs {related_docs} ")




