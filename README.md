## Java or Pathon?


# autism4j

1. A generic package for loading/parsing/inmorting/exporting ontology to neo4j.
2. A module which deal with annotation data, specifically autism patient data.
3. A statistic module for analysis such as enrichment analysis and semantic similarity. 
4. may contain possible wrapping of existing C++/R/Python code

# resources
loading of ontologies files (a) in topOnto and
* [pheno4j](https://github.com/phenopolis/pheno4j/tree/master/python)
* [SciGraph](https://github.com/SciGraph)
* [ont4j](https://github.com/ylins/ont4j)

## semantic similarities
* https://arxiv.org/pdf/cmp-lg/9511007.pdf
* https://www.biorxiv.org/content/biorxiv/early/2017/02/16/108977.full.pdf
* https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115692

## network clusting 
* [graph-tool](https://graph-tool.skewed.de/)

## Page rank
* (wiki)[https://en.wikipedia.org/wiki/PageRank]


---

* Colin has python code to export/import obo file to/from the server. NRG is running a neo4j server. (account created:xin)
* Colin: C++ code to contruct a network/vetice/edge object. 
* Colin: C++ hypergeometric test for enrichment test. Accept the two comparing gene list as input.
* R code for entrypy calculation on igraph network. Example in PPI network. Code is currently workong with undirect graph, needs to be implement to work with directional graph.



## NRG server ip:
129.215.164.31








---

# Meeting note 5th Oct 2018

![image](https://user-images.githubusercontent.com/3407502/46533664-59fd6700-c89d-11e8-95bd-98b086a14211.png)
![image](https://user-images.githubusercontent.com/3407502/46533666-5bc72a80-c89d-11e8-99ff-b56e7ebb07bc.png)
![image](https://user-images.githubusercontent.com/3407502/46533748-a5b01080-c89d-11e8-8bf1-6a0464e3ea36.png)


## Neo4j 
* Graph structure:

Nodes, Edges, Graph...[neo4j.jar](https://neo4j.com/docs/java-reference/current/javadocs/overview-summary.html)

* Communication with server 

driver


## Loading ontology into python/java
Owl 
### Java api:
https://github.com/owlcs/owlapi/
* An API for OWL 2 and an in-memory reference implementation
* RDF/XML parser and writer
* OWL/XML parser and writer
* OWL Functional Syntax parser and writer
* Turtle parser and writer
* KRSS parser
* OBO format parser
* Reasoner interfaces for working with reasoners such as FaCT++, HermiT, Pellet, Racer, JFact and Chainsaw.* 


### python api: 
* rdflib





git update-index --assume-unchanged ddp2neo4j/settings.py








