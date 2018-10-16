import numpy as np
import pandas as pd
import string
import random


class RandomDataFrameGenerator:
    def __init__(self, type2colname):
        self.type2colname = self._get_valid_cols(type2colname)
        self.create_col_func = {
            'str': self._create_str_col,
            'int': self._create_int_col,
            'float': self._create_float_col
        }
        
    def _get_valid_cols(self, type2colname):
        invalid_types = []
        valid_type2colname = {}
        for str_type, cols_list in type2colname.items():
            if str_type in ('int', 'float', 'str'):
                valid_type2colname[str_type] = cols_list
            else:
                invalid_types.append(str_type)
        self.print_error_msg(invalid_types, type2colname)
        return valid_type2colname

    def _create_str_col(self, n):
        return [random.choice(string.ascii_letters) for i in range(n)]
    
    def _create_int_col(self, n):
        return np.random.choice(np.arange(5000), n)
    
    def _create_float_col(self, n):
        return np.random.random(n)
    
    def get_df(self, n):
        df = pd.DataFrame()
        for str_type, cols_list in self.type2colname.items():
            for col in cols_list:
                df[col] = self.create_col_func[str_type](n)
        return df
    
    def print_error_msg(self, invalid_types, type2colname):
        invalid_cols = []
        for str_type in invalid_types:
            invalid_cols += type2colname[str_type]
        print('Não foi possível tratar o(s) seguinte(s) tipo(s): "{invalid_types}"'.format(invalid_types=', "'.join(invalid_types)))
        print('Assim, a(s) seguinte(s) coluna(s) não aparecerá(ão) no dataset: "{invalid_cols}"'.format(invalid_cols=', "'.join(invalid_cols)))