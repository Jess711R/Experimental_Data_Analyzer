# **Experimental Data Analyzer**

*A Tkinter-based Python tool for exploring and visualizing experimental biology datasets*


# **Overview**

The **Experimental Data Analyzer** is a Python-based graphical application designed to simplify the analysis of experimental biology datasets. The tool loads, validates, filters, and visualizes data without requiring users to write any code, making it accessible to students and researchers with minimal programming experience.

This project demonstrates the workflow using a small MCF-7 breast cancer MTT assay dataset, but the program is built to be flexible and can analyze any similar experimental dataset with columns such as:

* treatment group
* dose
* time point
* sample ID
* measurement/response variable

The project uses a multi-module structure, object-oriented design, robust error handling, and a full suite of unit tests. The graphical interface is built with Tkinter, and visualizations are generated using matplotlib and seaborn.


# 🚀 **Features**

### **📁 Data Loading**

* Supports CSV and Excel files
* Handles UTF-8 and Windows-encoded CSVs
* Detects empty datasets
* Validates presence of required columns
* Provides clear error messages for all loading issues



### **🔎 Data Filtering**

* Filter dataset by **column = value** directly from the GUI
* Detects invalid/missing columns
* Displays number of remaining rows after filtering
* Automatically updates the dataset stored in memory


### ⚠️ **Note on Filtering**

The current version of the filtering feature supports **string-based filtering only**, meaning the program can filter rows using **categorical/text columns** such as:

* `Treatment`
* `SampleID`

However, **numeric columns** — such as:

* `Dose_µM`
* `Time_h`
* `Viability_percent`
* `Replicate`

cannot be filtered using the GUI.
This is because user-entered values in the filter box are treated as text, and numeric comparisons (for example `"10"` vs `10`) do not match. As a result, filtering numeric columns will return zero results even if matching numeric values exist in the dataset.

This limitation applies only to filtering and **does not affect any other features**, including plotting, statistics, or PCA.



### **📊 Visualizations**

The tool supports five major plot types:

| Plot Type        | Use Case                                          |
| ---------------- | ------------------------------------------------- |
| **Line Plot**    | Time-course experiments, dose–response trends     |
| **Bar Plot**     | Comparing conditions or treatments                |
| **Scatter Plot** | Relationship between variables                    |
| **Heatmap**      | Correlation structure between numeric variables   |
| **PCA Plot**     | Dimensionality reduction & pattern identification |

All plots pop up in separate matplotlib windows.


### **🖥 Graphical User Interface (Tkinter)**

The GUI provides a clean, step-wise workflow:

1. Upload data file
2. Apply filtering (optional)
3. Choose a plot type and generate visualizations

No command-line usage required.


### **🧪 Unit Testing Suite**

A complete set of **10 unit tests** ensures reliability and robustness:

* Loading CSVs
* Handling invalid or missing files
* Required column validation
* Filtering valid and invalid columns
* Statistics computation
* Line plot generation
* PCA plot generation
* Heatmap creation

Testing covers both normal and edge-case behaviors.



# 📂 **Project Structure**

```
Experimental_Data_Analyzer/
│
├── data_loader.py               # File loading + validation
├── data_manager.py              # Filtering + statistics
├── visualizer.py                # Plotting functions
├── gui.py                       # Tkinter GUI
├── main.py                      # Application entry point
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation
│
├── sample_data/
│   ├── MCF7_MTT_small.csv       # Demo dataset (MTT assay)
│   └── MCF7_MTT_large.csv      # Optional second dataset
│
└── tests/                       # Unit tests (10 total)
    ├── test_loader_01_load_csv.py
    ├── test_loader_02_invalid_file.py
    ├── test_loader_03_required_columns.py
    ├── test_manager_01_filter.py
    ├── test_manager_02_filter_invalid_column.py
    ├── test_manager_03_stats.py
    ├── test_visualizer.py
    ├── test_visualizer_01_line_plot.py
    ├── test_visualizer_02_pca_plot.py
    ├── test_visualizer_03_heatmap.py
    └── __init__.py
```



# ▶️ **Running the Application**

To launch the GUI:

```
python main.py
```

This opens the graphical interface where users can upload datasets, run filters, and generate plots.



# 📊 **Sample Datasets**

### **1. MCF7_MTT_small.csv (15 samples)**

A compact, simulated MTT assay dataset used for testing, demos, and fast development cycles.
This file contains 15 samples representing a small subset of MCF-7 breast cancer assay conditions.

**Columns included:**

* **SampleID** – unique identifier for each measurement
* **Treatment** – e.g., Control, Quercetin, Metformin
* **Dose_µM** – drug concentration in micromolar
* **Time_h** – incubation time in hours
* **Viability_percent** – cell viability derived from MTT absorbance
* **Replicate** – technical replicate number (1, 2, or 3)

**Best used for:**

* quick GUI demonstration
* unit test execution
* rapid plotting checks (line, bar, scatter)


### **2. MCF7_MTT_large.csv (63 samples)**

A more complete version of the MTT assay dataset containing 63 samples, spread across multiple treatments, doses, time points, and replicates.

**Columns included (same as the small dataset):**

* **SampleID**
* **Treatment**
* **Dose_µM**
* **Time_h**
* **Viability_percent**
* **Replicate**

**Best used for:**

* PCA analysis
* heatmaps with meaningful variation
* demonstrating filtering and subgrouping
* testing scalability on larger data



# 🧪 **How to Run Unit Tests**

### **Run all tests:**

```
python -m unittest discover -s tests -p "test_*.py" -v
```

### **Run an individual test:**

```
python -m unittest tests.test_visualizer_03_heatmap -v
```

When all tests pass, you'll see:

```
Ran 10 tests in X.XXXs
OK
```



# 🧠 **Technical Details**

### **Coding Practices Used**

* Object-oriented design (DataLoader, DataManager, Visualizer, GUI classes)
* Modular architecture (separate files for major components)
* PEP8-compliant naming and layout
* Inline comments and docstrings for every class/method
* Exception raising with descriptive messages
* Tkinter MVC-style layout
* Matplotlib + seaborn plotting pipelines


### **Data Validation**

DataLoader enforces:

* File existence
* Correct file extension
* UTF-8 and fallback encoding
* Non-empty content
* Required columns

If any of these conditions fail, the loader raises an exception that the GUI displays to the user.


### **Plotting Backend**

* Unit tests use the Agg backend implicitly
* The GUI uses interactive windows
* All plotting functions open a new figure for each call
