# How much an annual increase in TFP for each prefecture would increase that prefecture's TFP ranking

## Overview

This project aims to demonstrate the effect of increasing Relative Total Factor Productivity (TFP) by a certain percentage and how this impacts the national Relative Total Factor Productivity ranking for each prefecture. It shows that an increase in Relative TFP by a certain value `x` results in a change of `y` places in the national ranking.

## Running the Analysis

Follow these steps to run the analysis:

1. **Build the Docker Image**:  
   Begin by building the Docker image for the project. Use the following command in your terminal:
    ```bash
    docker build -t average_tfp_change .
    ```

2. **Run the Docker Container**:  
After successfully building the image, run the container with the following command:
    ```bash
    docker run -it average_tfp_change
    ```
    This will launch an interactive shell within the container.

3. **Input the Hypothetical TFP Increase**:  
Once in the interactive shell, you will be prompted to input the hypothetical TFP increase value. For a realistic scenario, consider entering a value like `0.03` (representing a 3% increase).

## Important Notes

- Ensure that Docker is installed on your system and is running before executing these commands.
- The analysis is interactive and requires user input to proceed.