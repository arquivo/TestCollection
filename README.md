# Introduction

The PWA9609 test collection was created to support research on web archive information retrieval (WAIR). It is composed by three parts: (1) a corpus representative of the documents' versions encountered in a real search environment; (2) a set of topics describing users' information needs; and (3) relevance judgments (a.k.a. qrels) indicating the degree of relevance of each document retrieved for each topic.

If you are experimenting with WAIR systems and you are interested in their design and evaluation, then this collection can be useful.

# Corpus

The corpus is composed by 6 collections of the Portuguese web, broadly considered the web subset of interest to the Portuguese. These collections are indexed and searchable through the public access given by the Portuguese Web Archive (PWA) at http://archive.pt.

In total, the corpus contains 255 million web pages' versions collected between 1996 and 2009. It amounts 6.2TB compressed in ARC file format (8.9 TB uncompressed). The corpus' main characteristics are detailed in the following table, showing a significant heterogeneity in age, size and type.

| # | Years | Documents (K) | Size (GB) | Description | 
|:------|:----------|:------------------|:--------------|:----------------| 
| 1 | 1996 | 75 | 0.316 | selective crawl of most popular sites | 
| 2 |1996 - 2000 | 5 047 | 48 | broad crawls periodically made by the Internet Archive |
| 3 | 2000 - 2008 | 118 842 | 1 900 | broad crawls periodically made by the Internet Archive |
| 4 | 2004 - 2006 | 14 374 | 165 | selective crawls made by the Portuguese National Library | 
| 5 | 2008 | 48 718 | 1 600 | exhaustive crawl of mostly the .pt domain | 
| 6 | 2009 | 68 776 | 2 500 | exhaustive crawl of mostly the .pt domain | 
| | TOTAL | 255 832 | 6 213 |

This corpus includes all types of media formats (e.g. text, image, video and audio) and genres (e.g. news, blogs, wikis) to support future IR tasks with different goals in mind.

## Obtaining a Copy of the PWA9609 test collection

The PWA9609 test collection is distributed by the Portuguese Foundation for National Scientific Computation strictly for research purposes only. The collection may be obtained by signing a data license agreement with the Portuguese Foundation for National Scientific Computing.

Please contact miguel.costa (at) fccn.pt for further information.
#Topics

    Navigational topics.
    Infomational topics.

# Relevance Judgments

| Grade | Very relevant | Relevant | Not relevant | 
|:----------|:------------------|:-------------|:-----------------| 
| manual | 69 | 91 | 1 819 | 
| automatic | 5 168 | 5 571 | 257 083 | 
| TOTAL | 5 237 | 5 662 | 258 902 |

    Manuallly assessed qrels.
    Automatically assessed qrels.

# Metadata

A list of mappings between each version id and the corresponding pair can be downloaded.

# Evaluation

Results can be computed with the trec_eval tool used by the TREC community, since the test collection follows the TREC file formats.

# Other Issues

Information about the methodology used to create the PWA9609 collection was published at the 13th International Conference on Web Information System Engineering in a paper named Evaluating Web Archive Search Systems.
