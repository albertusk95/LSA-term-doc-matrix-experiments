import numpy

def buildTermDocumentMatrix(terms,docs):
  '''
    build a term-document matrix
  '''
  tlen = len(terms)
  dlen = len(docs)
  A = numpy.zeros((tlen, dlen))

  for i,t in enumerate(terms):
    for j,d in enumerate(docs):
      # computing terms frequencies
      A[i,j] = d.lower().count(t)

  # normalize columns
  for i in range(dlen):
    A[:tlen,i] = A[:tlen,i]/numpy.linalg.norm(A[:tlen,i])

  return A

def query(A,q,docs):
  '''
    make the query and print the result
  '''
  # normalize query vector
  q = q/numpy.linalg.norm(q)
  for i in range(len(docs)):
    # dot product
    print '-Doc  :',docs[i],'\n-Match:',numpy.dot(A[:6,i].T,q) 

# documents collection
docs =['How to Bake Bread Without Recipes',
       'The Classic Art of Viennese Pastry',
       'Numerical Recipes: The Art of Scientific Computing',
       'Breads, Pastries, Pies and Cakes : Quantity Baking Recipes',
       'Pastry: A Book of Best French Recipe']
       
# interesting terms
terms = ['bak','recipe','bread','cake','pastr','pie']

# return a matrix with size of 6 terms x 5 documents
A = buildTermDocumentMatrix(terms,docs) 
print 'Normalized Terms-Documents matrix'
print A

print 'Query: "bake" / "baking" + "bread"'
q1 = numpy.array([1,0,1,0,0,0])
query(A,q1,docs)

print 'Query: "bake" / "baking" only'
q2 = numpy.array([1,0,0,0,0,0])
query(A,q2,docs)
