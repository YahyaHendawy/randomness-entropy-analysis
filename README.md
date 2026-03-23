# Randomness & Entropy Analysis

## Overview

This project investigates how "random" computer-generated numbers
actually are by analyzing their statistical properties.

The goal is to move beyond visual inspection and apply quantitative
methods to evaluate randomness quality.

## Objectives

-   Evaluate randomness quality of different generators\
-   Compare pseudo-random vs naive methods\
-   Measure entropy and distribution uniformity\
-   Identify hidden patterns or bias

## Methods

### Data Generation

Two datasets of 10,000 values (0--9) were generated using: - Python
built-in pseudo-random generator\
- Time-based generator (system clock)

### Analysis Techniques

-   Frequency distribution (histogram)
-   Deviation from expected uniform distribution
-   Shannon entropy calculation

## Results

### Python Random Generator

-   Near-uniform distribution\
-   Small deviations from expected values\
-   High entropy

### Time-Based Generator

-   Visually similar distribution\
-   Slight irregularities\
-   Lower randomness quality due to predictability

## Key Insight

Although both generators appear visually uniform, deeper analysis
reveals that not all randomness is equal.

**Visual inspection alone is insufficient to evaluate randomness
quality.**

## Engineering Relevance

Randomness quality is critical in: - simulations\
- modelling\
- cryptography\
- security systems

## Technologies Used

-   Python\
-   Matplotlib\
-   Statistical analysis

## Conclusion

Randomness must be evaluated using quantitative methods rather than
visual inspection alone.
