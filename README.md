# Refactored Lecture Code - CS50AI Lecture 2, Uncertainty

<br>

This repository contains a **refactored** version of the source code used in Lecture 2 (Uncertainty) of the CS50AI course. The original code relied on an outdated version of the `pomegranate` library, which raised errors and could not be easily updated to work with modern environments.

To address this issue, I have refactored the code to use `pgmpy` and `hmmlearn`, two well-documented, up-to-date, and cross-platform libraries for probabilistic inference and Hidden Markov Models (HMMs). 

I have kept the structure and comments as close as possible to the original code while ensuring clarity and simplicity. I hope this is helpful for anyone currently learning CS50AI.

## Resources
- **Lecture Link:** [CS50AI - Uncertainty](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/block-v1:HarvardX+CS50AI+1T2020+type@sequential+block@4b8b77db65e54ec9bf3e397b012074bd/block-v1:HarvardX+CS50AI+1T2020+type@vertical+block@f7f87c00eace4aa0b88799eec602e4bf)
- **pgmpy Documentation:** [https://pgmpy.org/](https://pgmpy.org/)
- **hmmlearn Documentation:** [https://hmmlearn.readthedocs.io/en/latest/](https://hmmlearn.readthedocs.io/en/latest/)
- **Original Source Code:** [CS50AI Lecture 2 Source Code](https://cdn.cs50.net/ai/2020/spring/lectures/2/src2.zip)

*(Note: The first commit in this repository contains the original, unmodified code as a reference.)*

## Installation
To run the refactored code, install the required dependencies:

```bash
pip install pgmpy hmmlearn
```

## Usage
Run the refactored scripts as you would with the original course materials:

```bash
python [folder]/filename.py
```

Ensure that your Python environment is set up properly and that you have all required dependencies installed.

## Note
- Contributions and feedback are welcome!
