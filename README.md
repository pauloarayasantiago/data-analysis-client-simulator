# data-analysis-client-simulator
 
## Environment Setup

This project utilizes a dedicated virtual environment to manage dependencies and ensure reproducibility.

**Environment Management Tool:** Conda

**Environment Name:** `dacs`

**Python Version:** 3.13.1

**Key Dependencies:**

*   Flask: 3.0.3
*   google-generativeai: 0.8.3
*   Pandas: 2.2.3
*   Faker: 30.8.1
*   Jupyter: 1.1.1
*   ipywidgets: 7.6.5

**Creating the Environment:**

To create this environment, execute the following command in your terminal:

```bash
conda create --name dacs python=3.13 flask google-generativeai pandas faker jupyter ipywidgets