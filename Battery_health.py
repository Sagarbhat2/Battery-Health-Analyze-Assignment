import pandas as pd
import plotly.express as px


# Load the dataset
df = pd.read_csv('C:/Users/Sagar/Desktop/Battery Health Analysis/archive/cleaned_dataset/metadata.csv')
df.columns = df.columns.str.strip()

#columns names

print("Columns in the dataset:", df.columns)
df.dropna(subset=['Re', 'Rct'], inplace=True)

# checking for missing value
print(df.isnull().sum())

# df['Cycle'] = df['test_id']

#line plot for Battery Impedance over Cycles
fig_re = px.line(df, 
                x='test_id', 
                y='Re', 
              title='Battery Impedance Over Charge/Discharge Cycles',
              labels={'Battery_impedance': 'Battery Impedance (ohms)', 'test_id': 'Cycle Number'})

# Show the plot
fig_re.show()


#lot for Charge Transfer Resistance (Rct) over Cycles
fig_rct = px.line(df,
                 x='test_id', 
                 y='Rct', 
                  title='Charge Transfer Resistance (Rct) Over Cycles',
                  labels={'Rct': 'Charge Transfer Resistance (ohms)', 'test_id': 'Cycle Number'})

fig_rct.show()










