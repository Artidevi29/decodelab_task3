# decodelab_task3
genre based movie recommender using jaccard similarity, decode lab ai internship task


# Project 3 - AI Recommendation Logic

part of my decode lab ai internship tasks

## what it is

a simple recommendation system that suggests movies based on genres you say you like. its content based, meaning it just compares your preferences against tags/genres attached to each movie rather than using other peoples ratings or anything like that

## how it works

there's a small hardcoded list of movies in the script, each one tagged with genres (like sci-fi, comedy, drama etc). you type in the genres youre interested in, and it calculates something called jaccard similarity between your picks and each movies genre list - basically just how much overlap there is - then shows you the top matches sorted by score

## how to run

```
python proj3_recommender.py
```

no extra installs needed, its pure python

it first runs a demo automatically (with sci-fi + action as example preferences) so you can see sample output without typing anything, then it asks you for your own genre preferences after that

available genres are shown on screen when u run it, just type them comma separated like:

```
comedy, romance
```

## notes

pretty basic recommender, real ones usually use ur watch history or ratings from other users (collaborative filtering) instead of just one input like this. this was more about practicing the logic/pattern matching part of it
