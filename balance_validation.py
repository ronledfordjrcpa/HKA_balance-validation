import pandas as pd

def load_data(dynamics_file, sage_file, mapping_file):
    dynamics_df = pd.read_excel(dynamics_file)
    sage_df = pd.read_excel(sage_file)
    mapping_df = pd.read_excel(mapping_file)
    return dynamics_df, sage_df, mapping_df

def map_accounts(dynamics_df, mapping_df):
    gl_mapping = dict(zip(mapping_df['Dynamics_GP_Account'], mapping_df['Sage_Intacct_Account']))
    dynamics_df['Mapped_Account'] = dynamics_df['GL_Account'].map(gl_mapping)
    return dynamics_df

def validate_balances(dynamics_df, sage_df):
    group_by_fields = ['Mapped_Account', 'Location', 'Department', 'Class', 'Employee']
    dynamics_summed = dynamics_df.groupby(group_by_fields)['Balance'].sum().reset_index()
    sage_summed = sage_df.groupby(group_by_fields)['Balance'].sum().reset_index()
    merged_df = pd.merge(dynamics_summed, sage_summed, on=group_by_fields, suffixes=('_Dynamics', '_Sage'))
    merged_df['Difference'] = merged_df['Balance_Dynamics'] - merged_df['Balance_Sage']
    return merged_df

def generate_report(merged_df, output_file):
    merged_df.to_excel(output_file, index=False)

if __name__ == "__main__":
    dynamics_file = 'path/to/dynamics_gp.xlsx'
    sage_file = 'path/to/sage_intacct.xlsx'
    mapping_file = 'path/to/mapping_file.xlsx'
    output_file = 'balance_validation_report.xlsx'

    dynamics_df, sage_df, mapping_df = load_data(dynamics_file, sage_file, mapping_file)
    dynamics_df = map_accounts(dynamics_df, mapping_df)
    merged_df = validate_balances(dynamics_df, sage_df)
    generate_report(merged_df, output_file)