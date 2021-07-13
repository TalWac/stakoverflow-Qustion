
import pandas as pd
import numpy as np

def import_data(path):
    df = pd.read_excel(path)
    return df


def impute_treatment( treatmentspar, data ):

    '''
    treatmentspar: list a list indicating the treatments paramters as writen in the files. 
    The function creates 3 columns :Class, SampleType
    Class = can be eathier QC1-SameVial, Blank or one of the treatments
    SampleType = can be eathier Sample, QC1-SameVial or Blank
    data: the data we are workin on df_reduce_T
    '''
    for treatment in treatmentspar:
        data['Class'] = np.where(data['SampleID'].str.contains(treatment),
                                 treatment, data['Class'])
        data['SampleType'] = np.where(data['SampleID'].str.contains(treatment),
                                      'Sample', data['SampleType'])

    data['Class'] = np.where(data['SampleID'].str.contains("QC1"),
                             'QC1-SameVial', data['Class'])
    data['SampleType'] = np.where(data['SampleID'].str.contains("QC1"),
                                  'QC1-SameVial', data['SampleType'])

    data['Class'] = np.where(data['SampleID'].str.contains("Blank"),
                             'Blank', data['Class'])
    data['SampleType'] = np.where(data['SampleID'].str.contains("Blank"),
                                  'Blank', data['SampleType'])

    return data


def impute_treatment_color(treatmentspar):
    '''
    treatmentspar: recieve a list
    The function assign to each treatmemnt a color - there are 9 colors and the color red to the QC sample type.
    '''
    data = pd.DataFrame()
    colors = ['yellow', 'black', 'blue', 'green', 'gray', 'pink', 'brown', 'purple', 'orange']
    n = len(treatmentspar)
    colors_1 = colors[:n]

    for treatment, color in zip(treatmentspar, colors_1):
        data.loc[treatment, 'color'] = color

    data.loc['QC1-SameVial', 'color'] = 'red'
    return data