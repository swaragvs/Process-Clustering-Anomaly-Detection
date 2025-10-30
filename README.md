# Process Resource Clustering with K-Means

This Python script implements an advanced process resource monitoring and anomaly detection system using K-Means clustering and machine learning techniques. The system analyzes system processes based on their resource usage patterns and identifies potential anomalies.

![3D PCA K-Means Clustering](Process-Clustering-Anomaly-Detection/OUTPUT%20SCREENSHOTS/3D%20PCA%20K%20MEANS%201.png)

## Features

- **Resource Monitoring**: Tracks multiple system metrics including:
  - CPU usage percentage
  - Memory usage percentage
  - Disk read/write rates (MB)
  - Network sent/received rates (MB)

- **Advanced Analytics**:
  - K-Means clustering for behavioral profiling
  - Principal Component Analysis (PCA) for dimensionality reduction
  - Hybrid anomaly detection using:
    - Isolation Forest
    - Distance-based metrics
  - Interactive 3D visualization of process clusters

- **Comprehensive Reporting**:
  - Detailed cluster analysis
  - Anomaly detection results
  - Performance metrics
  - Interactive visualizations

## Requirements

```python
# Core Libraries
numpy
pandas
joblib

# Visualization
matplotlib
plotly
plotly.express
plotly.graph_objects

# Machine Learning
scikit-learn
```

## Installation

1. Clone this repository or download the script
2. Install required packages:
```bash
pip install numpy pandas joblib matplotlib plotly scikit-learn
```

## Usage

1. Prepare your process log data in CSV format with the following columns:
   - cpu_percent
   - memory_percent
   - disk_read_mb
   - disk_write_mb
   - net_sent_mb
   - net_recv_mb

2. Update the configuration section in the script:
```python
DATA_PATH = 'process_log.csv'  # Path to your input data
SAVE_DIR = 'models'            # Directory to save models
```

3. Run the script:
```bash
python process_resource_clustering_k_means.py
```

## Script Structure

The script is organized into multiple cells, each handling a specific aspect of the analysis:

1. **Setup & Configuration** (Cell 1)
   - Library imports
   - Global configuration
   - Utility functions

2. **Data Loading & Inspection** (Cell 2)
   - Data loading
   - Initial validation
   - Schema verification

   ![Initial Dataset](Process-Clustering-Anomaly-Detection/OUTPUT%20SCREENSHOTS/INITIAL%20DATASET.png)

3. **Exploratory Data Analysis** (Cells 3-5)
   - Feature distributions
   - Correlation analysis
   - Temporal behavior analysis

   ![Feature Distribution](Process-Clustering-Anomaly-Detection/OUTPUT%20SCREENSHOTS/FEATURE%20PATTERN%20DISTRUBUTION.png)
   ![Correlation Analysis](Process-Clustering-Anomaly-Detection/OUTPUT%20SCREENSHOTS/Co-relation.png)
   ![Temporal Analysis](Process-Clustering-Anomaly-Detection/OUTPUT%20SCREENSHOTS/Temporal.png)

4. **Data Preprocessing** (Cells 6-7)
   - Missing value handling
   - Scaling
   - PCA transformation

   ![Scale and PCA](Process-Clustering-Anomaly-Detection/OUTPUT%20SCREENSHOTS/Scale-PCA.png)

5. **Model Development** (Cells 8-10)
   - K-Means model selection
   - Model training
   - Performance evaluation

   ![Model Selection](Process-Clustering-Anomaly-Detection/OUTPUT%20SCREENSHOTS/MODEL-SELECTION-KMEANS-SIL.png)

6. **Anomaly Detection** (Cell 11)
   - Hybrid approach implementation
   - Distance-based detection
   - Isolation Forest integration

   ![Anomaly Detection](Process-Clustering-Anomaly-Detection/OUTPUT%20SCREENSHOTS/detection-anomaly.png)

7. **Visualization** (Cells 12-14)
   - Interactive 3D cluster visualization
   - Inference overlay
   - Test case visualization

   ![3D Cluster Visualization](Process-Clustering-Anomaly-Detection/OUTPUT%20SCREENSHOTS/3D%20PCA%20K%20MEANS%202.png)
   ![Test Simulation](Process-Clustering-Anomaly-Detection/OUTPUT%20SCREENSHOTS/TEST-SIM.png)

8. **Reporting** (Cells 15-17)
   - Data export
   - Summary metrics
   - Interpretive analysis
   - Anomaly intelligence report

   ![Performance Scores](Process-Clustering-Anomaly-Detection/OUTPUT%20SCREENSHOTS/Scores.png)

## Output

The script generates several outputs:

- Trained models saved in the `models` directory:
  - `scaler.joblib`: StandardScaler model
  - `pca.joblib`: PCA model
  - `kmeans_final.joblib`: Final K-Means model
  - `isolation_forest.joblib`: Isolation Forest model
  - `dist_minmax.joblib`: MinMax scaler for distances

- Comprehensive CSV report:
  - `cluster_anomaly_summary.csv`: Detailed analysis results

- Interactive visualizations:
  - 3D cluster plots
  - Feature distribution plots
  - Correlation heatmaps

## Performance Metrics

The script evaluates clustering performance using multiple metrics:
- Silhouette Score
- Calinski-Harabasz Index
- Davies-Bouldin Index

![Model Performance Metrics](Process-Clustering-Anomaly-Detection/OUTPUT%20SCREENSHOTS/Model%20Selection.png)

## License

This project is open-source and available under the MIT License.

## Author

Swarag V S

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
