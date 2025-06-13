# Portfolio Optimization

<!-- omit in toc -->

## Languages
[![python](https://img.shields.io/badge/python-3.11-d6123c?color=white&labelColor=d6123c&logo=python&logoColor=white)](https://www.python.org/)

<!-- omit in toc -->
## Frameworks
[![pandas](https://img.shields.io/badge/pandas-2.3.0-d6123c?color=white&labelColor=d6123c&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![yfinance](https://img.shields.io/badge/yfinance-0.2.62-d6123c?color=white&labelColor=d6123c&logo=yfinance&logoColor=white)](https://pypi.org/project/yfinance/)
[![cvxpy](https://img.shields.io/badge/cvxpy-1.6.5-d6123c?color=white&labelColor=d6123c&logo=cvxpy&logoColor=white)](https://www.cvxpy.org/)
[![matplotlib](https://img.shields.io/badge/matplotlib-3.10.3-d6123c?color=white&labelColor=d6123c&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![seaborn](https://img.shields.io/badge/seaborn-0.13.2-d6123c?color=white&labelColor=d6123c&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)
[![plotly](https://img.shields.io/badge/plotly-6.1.2-d6123c?color=white&labelColor=d6123c&logo=plotly&logoColor=white)](https://plotly.com/graphing-libraries/)
[![openai](https://img.shields.io/badge/openai-1.85.0-d6123c?color=white&labelColor=d6123c&logo=openai&logoColor=white)](https://openrouter.ai/)
[![gpt4free](https://img.shields.io/badge/g4free-0.5.4.0-d6123c?color=white&labelColor=d6123c&logo=openai&logoColor=white)](https://github.com/xtekky/gpt4free)


<!-- omit in toc -->
## Table of Contents
- [Portfolio Optimization](#portfolio-optimization)
  - [Languages](#languages)
  - [Introduction](#introduction)
  - [Project Workflow](#project-workflow)
    - [Efficient Frontier](#efficient-frontier)
    - [Mean-Variance Portfolio Composition](#mean-variance-portfolio-composition)
    - [Test](#test)

## Introduction
This project is the final assignment for the Financial and Risk Analytics course at [BigDataLab](https://www.bigdatalab.com.ua/).

## Project Workflow
### Efficient Frontier
The project uses the following portfolios:
- Min-Variance Portfolio
- Max-Return Portfolio
- Max Sharpe Ratio Portfolio
- GPT-4o-mini Portfolio
- GPT-4o Portfolio
- DeepSeek V3 Portfolio
- DeepSeek R1 Portfolio
- Gemini 2.0 Flash-Exp Portfolio
- Llama 4 Maverick Portfolio
- Meta Llama 4 Scout Portfolio
- GPT Web Deep-Research Portfolio
- Grok3 Web Deep-Research Portfolio
- LeChat Web Deep-Research Portfolio

For diversification we used the constraint `0 ≤ weight ≤ 0.2`.  
Cardinality: 20 assets.  
Risk-free rate (for Sharpe ratio): 0.02  

![Efficient Frontier](images/efficient_frontier.png)

### Mean-Variance Portfolio Composition
Portfolio composition for mean-variance, where:
- X - Expected Return
- Y - Weights 

![Portfolio Composition](images/portfolio_composition.png)

### Test
- The min-variance and Sharpe ratio portfolios performed best.  
- The max-returns portfolio performed poorly, possibly due to the current geopolitical situation.  
- The neural network portfolios slightly outperform the S&P 500 benchmark.

![Test](images/test.png)