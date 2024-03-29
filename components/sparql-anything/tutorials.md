---
component-id: sparql-anything-tutorials
type: Tutorial
name: "SPARQL Anything: Tutorials"
description: a collection of tutorials to introduce users to SPARQL Anything
logo: https://avatars.githubusercontent.com/u/79987779?s=200&v=4
demo: https://github.com/SPARQL-Anything/showcase-tate
resource: https://sparql-anything.readthedocs.io/en/latest/TUTORIALS/
licence:
- Apache-2.0
copyright: "Copyright (c) 2022 SPARQL Anything Contributors @ http://github.com/sparql-anything"
contributors:
- Luigi Asprino <https://github.com/luigi-asprino>
- Enrico Daga <https://github.com/enridaga>
- Justin Dowdy <https://github.com/justin2004>
- Marco Ratta <https://github.com/MarcoR1791>
related-components:
- informed-by:
  - sparql-anything-cli
  - sparql-anything-server
  - sparql-anything-python
---

# SPARQL Anything: Tutorials

Here is a list of step-by-step tutorials covering several features of SPARQL Anything:

- [A Gentle introduction to SPARQL Anything](A_GENTLE_INTRODUCTION_TO_SPARQL_ANYTHING.md): this tutorial presents the Facade-X model and shows basic transformations of JSON, CSV and XML. [Video](https://www.dropbox.com/s/bc31v0klg68op0z/SPARQLAnythingTutorial-highres.mp4?dl=0) 
- [SPARQL Anything showcase: open data from the Tate Gallery](https://github.com/SPARQL-Anything/showcase-tate): this tutorial covers formats such as CSV and JSON and features such as the function `fx:anySlot` and the chaining of multiple `SERVICE` clauses. It is based on the SPARQL Anything [CLI](README.md#Usage).
- [Construct a KG of artists and artworks of the IMMA museum website](https://github.com/SPARQL-Anything/showcase-imma): This showcase demonstrates the use of SPARQL Anything for constructing a Knowledge Graph from data encoded in HTML pages. Apart from examples with the HTML input format, it covers features such as parametrised queries and the use of SPARQL result set files as parameters. It is based on the SPARQL Anything [CLI](README.md#Usage).
- [Construct a KG from the Propbank dataset](https://github.com/SPARQL-Anything/showcase-propbank): An advanced example of transformation of XML data, including querying a Zip archive.
- [Construct a KG from YAML annotations in Markdown file headers](https://github.com/SPARQL-Anything/showcase-polifonia-ecosystem): A short but complex case demonstrating how to chain multiple transformations starting from a set of Markdown files, queried to extract the YAML header, which is in turn queried to derive the annotations, that are in turn projected into a KG!
- [Populate a Music Ontology from MusicXML files](https://github.com/SPARQL-Anything/showcase-musicxml): An advanced application of SPARQL Anything to query MusicXML files and derive note sequences, computing n-grams, and populating a Music Notation ontology.