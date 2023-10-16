from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np

training_data = pd.read_csv('data\\dataset\\training.csv')
testing_data = pd.read_csv('data\\dataset\\testing.csv')

training_stats = training_data.describe()
testing_stats = testing_data.describe()

plt.figure(figsize=(10, 6))
plt.scatter(training_data['Width'], training_data['Height'],
            c='blue', label='Training Data')
plt.scatter(testing_data['Width'],
            testing_data['Height'], c='red', label='Testing Data')
plt.xlabel('Width')
plt.ylabel('Height')
plt.title('Width vs Height')
plt.legend()
plt.savefig('scatter_plot.png')

selected_features2 = ['Width', 'Height', 'Elongation', 'Roundness', 'Complexity', 'Symmetry',
                      'Average Nearest Neighbor Distance', 'Maximum Nearest Neighbor Distance', 'Fractal Dimension']

num_selected_features = len(selected_features2)
# Calculate the number of subplot rows
num_subplot_rows = (num_selected_features + 2) // 3
plt.figure(figsize=(15, 10))


for i, feature in enumerate(['Width', 'Height', 'Elongation', 'Roundness', 'Complexity', 'Symmetry',
                             'Average Nearest Neighbor Distance', 'Maximum Nearest Neighbor Distance', 'Fractal Dimension']):

    plt.subplot(num_subplot_rows, 3, i + 1)
    sns.histplot(data=training_data, x=feature, kde=True)
    plt.title(f'{feature} Histogram')
plt.tight_layout()
plt.savefig('histograms.png')

correlation_matrix = training_data.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix Heatmap')
plt.savefig('correlation_heatmap.png')

scatter_plot = px.scatter(training_data, x='Width',
                          y='Height', color='Label', title='Width vs Height')
scatter_plot_html = scatter_plot.to_html()

# Box plots for selected features
plt.figure(figsize=(12, 8))
selected_features = ['Width', 'Height',
                     'Elongation', 'Roundness', 'Complexity']

sns.boxplot(data=training_data[selected_features])
plt.title('Box Plots of Selected Features')
plt.xticks(rotation=45)
plt.savefig('box_plots.png')

# Pair plot for selected features
sns.pairplot(training_data[selected_features2], diag_kind='kde')
plt.suptitle('Pair Plot of Selected Features')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('pair_plot.png')

# Count plot of labels
plt.figure(figsize=(8, 6))
sns.countplot(data=training_data, x='Label', palette='Set2')
plt.title('Count Plot of Labels')
plt.xticks(rotation=45)
plt.savefig('count_plot.png')

# 3D Scatter plot using Plotly
scatter_3d = px.scatter_3d(training_data, x='Width', y='Height',
                           z='Elongation', color='Label', title='3D Scatter Plot')
scatter_3d_html = scatter_3d.to_html()

# Additional correlations
correlation_matrix_extended = training_data[selected_features].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_extended, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix Heatmap (Selected Features)')
plt.savefig('correlation_heatmap_selected.png')

plt.figure(figsize=(12, 8))


for i, feature in enumerate(selected_features):
    plt.subplot(2, 3, i+1)
    sns.violinplot(data=training_data, x='Label', y=feature, palette='pastel')
    plt.title(f'Violin Plot of {feature}')
plt.tight_layout()
plt.savefig('violin_plots.png')

# Distribution of features by label
plt.figure(figsize=(12, 8))
for i, feature in enumerate(selected_features):
    plt.subplot(2, 3, i+1)
    sns.kdeplot(data=training_data, x=feature,
                hue='Label', common_norm=False, fill=True)
    plt.title(f'{feature} Distribution by Label')
plt.tight_layout()
plt.savefig('feature_distributions.png')


# Pie chart of label distribution
label_counts = training_data['Label'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(label_counts, labels=label_counts.index,
        autopct='%1.1f%%', colors=sns.color_palette('Set2'))
plt.title('Label Distribution')
plt.savefig('pie_chart.png')

# Additional scatter plots using Plotly
scatter_3d_roundness_complexity = px.scatter_3d(
    training_data, x='Roundness', y='Complexity', z='Height', color='Label', title='3D Scatter Plot (Roundness vs Complexity)')
scatter_3d_roundness_complexity_html = scatter_3d_roundness_complexity.to_html()


selected_features3 = ['Symmetry',
                      'Average Nearest Neighbor Distance', 'Maximum Nearest Neighbor Distance', 'Fractal Dimension']

plt.figure(figsize=(12, 8))
for i, feature in enumerate(selected_features3):
    plt.subplot(2, 3, i+1)
    sns.kdeplot(data=training_data, x=feature,
                hue='Label', common_norm=False, fill=True)
    plt.title(f'{feature} Distribution by Label')
plt.tight_layout()
plt.savefig('feature_distributions2.png')

# Principal Component Analysis (PCA) visualization
pca = PCA(n_components=2)
pca_result = pca.fit_transform(training_data[selected_features])
training_data['PCA1'] = pca_result[:, 0]
training_data['PCA2'] = pca_result[:, 1]
plt.figure(figsize=(10, 8))
sns.scatterplot(data=training_data, x='PCA1',
                y='PCA2', hue='Label', palette='Set1')
plt.title('PCA Visualization')
plt.savefig('pca_visualization.png')


html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Data Analysis</title>
    <link rel="shortcut icon" type="image/x-icon" href="D:\Project2\drawing_ml\web\\favicon.ico" />
    <link rel="stylesheet" type="text/css" href="styleanalysis.css">
    
</head>
<body style="background-color: #53026B; text-align: center;"">
    <h1 style="text-align: center; margin-top: 20px; color: #FFFEFF;">Data Analysis</h1>
    
    <h2 style="margin-top: 40px; font-size: 24px; color: #FFFEFF;">Basic Statistics</h2>

    <h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Training Data</h3>

    <div style="display: inline-block; text-align: left;color: #FFFEFF;"> 
        <table style="border-collapse: collapse; width: 100%; border: 1px solid #FFFEFF; background-color: white;">
            {training_stats.to_html()}
        </table>
    </div>


    
    
    <h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Testing Data</h3>
     <div style="display: inline-block; text-align: left;color: #FFFEFF;"> <!-- Center-align container -->
        <table style="border-collapse: collapse; width: 100%; border: 1px solid #FFFEFF; background-color: white;">
            {testing_stats.to_html()}
        </table>
    </div>
    
    <h2 style="margin-top: 40px; font-size: 24px; color: #FFFEFF;">Scatter Plot</h2>
    <h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Using Matplotlib</h3>
    <img src="scatter_plot.png" alt="Scatter Plot" width="800" height="500">
    
    <h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Feature Histograms</h3>
    <img src="histograms.png" alt="Histograms" style="display: block; margin: 20px auto; max-width: 100%;">
    
    <h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Correlation Matrix Heatmap</h3>
    <img src="correlation_heatmap.png" alt="Correlation Heatmap" style="display: block; margin: 20px auto; max-width: 100%;">
    
    <h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Using Plotly</h3>
    {scatter_plot_html}


<h2 style="margin-top: 40px; font-size: 24px; color: #FFFEFF;">Additional Visualizations</h2>

<h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Box Plots</h3>
<img src="box_plots.png" alt="Box Plots" style="display: block; margin: 20px auto; max-width: 100%;">

<h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Pair Plot</h3>
<img src="pair_plot.png" alt="Pair Plot" style="display: block; margin: 20px auto; max-width: 100%;">
<h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Count Plot of Labels</h3>
<img src="count_plot.png" alt="Count Plot" style="display: block; margin: 20px auto; max-width: 100%;">

<h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">3D Scatter Plot</h3>
{scatter_3d_html}

<h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Correlation Matrix Heatmap (Selected Features)</h3>
<img src="correlation_heatmap_selected.png" alt="Correlation Heatmap (Selected Features)" style="display: block; margin: 20px auto; max-width: 100%;">

<h2 style="margin-top: 40px; font-size: 24px; color: #FFFEFF;">More Visualizations</h2>


<h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Feature Distributions by Label</h3>
<img src="feature_distributions.png" alt="Feature Distributions" style="display: block; margin: 20px auto; max-width: 100%;">

<h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Feature Distributions by Label</h3>
<img src="feature_distributions2.png" alt="Feature Distributions" style="display: block; margin: 20px auto; max-width: 100%;">

<h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">Pie Chart of Label Distribution</h3>
<img src="pie_chart.png" alt="Pie Chart" style="display: block; margin: 20px auto; max-width: 100%;">

<h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">3D Scatter Plot (Roundness vs Complexity)</h3>
{scatter_3d_roundness_complexity_html}

<h3 style="font-size: 18px; margin-top: 20px; color: #FFFEFF;">PCA Visualization</h3>
<img src="pca_visualization.png" alt="PCA Visualization" style="display: block; margin: 20px auto; max-width: 100%;">
    
</body>
</html>
"""

with open('data_analysis.html', 'w', encoding='utf-8') as f:
    f.write(html_content)