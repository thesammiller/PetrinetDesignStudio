# PeNDeS -- Petri Net Design Studio

## Introduction

A "petri net", also known as a "place/transition network", is a discrete event dynamic system. They offer a graphical notation for stepwise processes. 

"A Petri net consists of places, transitions, and arcs. Arcs run from a place to a transition or vice versa, never between places or between transitions. The places from which an arc runs to a transition are called the input places of the transition; the places to which arcs run from a transition are called the output places of the transition." [wikipedia](https://en.wikipedia.org/wiki/Petri_net)

## Typical Use-Cases
Petri nets can be used to describe a variety of processes. 

- Racecar [pit stop](http://www.lindstaedt.com.br/simuljogos/petriNets.pdf)
- [LAN](https://www.intechopen.com/books/petri-nets-applications) architectures
- [Producer-Consumer](https://inst.eecs.berkeley.edu/~ee249/fa07/discussions/PetriNets-Murata.pdf) system

How to start modeling once the studio is installed
Once a network is build, what feature your studio provides and how can the user use
those functions

## Installation
First, install the following:
- [NodeJS](https://nodejs.org/en/) (LTS recommended)
- [MongoDB](https://www.mongodb.com/)

Second, start mongodb locally by running the `mongod` executable in your mongodb installation (you may need to create a `data` directory or set `--dbpath`).

Third, `git clone` this repository.

Then, change into this directory and run `webgme start`. Finally, navigate to `http://localhost:8888` to start using pendes!

## Modeling
How to start modeling once the studio is installed

## Studio Usage
Once a network is build, what feature your studio provides and how can the user use
those functions


