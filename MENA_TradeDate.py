import pandas as pd

def pull_api(country_names: dict) -> list:
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    years = ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']

    df_lst = []

    
    for key, value in country_names.items():
        for year in years:
            for month in months:
            
                new_df = pd.DataFrame
                
                new_df = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,GEN_VAL_MO,GEN_VAL_YR&key=717114d894bcc2fa7c3cf60a181828e5c3e3d131&YEAR=' + year + '&MONTH=' + month + '&COMM_LVL=HS10&CTY_CODE=' + str(value))
                
                new_df.sort_values(by=[0],inplace=True,na_position='first')
                substring = 'I_COMMODITY'
                filter = new_df[0].str.contains(substring)
                fil_df = new_df[~filter]
                print('Year:' + year + ' Month: ' + month +  ' Country: ' + str(value))
                df_lst.append(new_df)
    
    return df_lst


def main():
    country_code = {'Algeria':7210,
                     'Bahrain':5250,
                     'Egypt':7290,
                    # 'Iran':5070,
                     'Iraq':5050,
                     'Israel':5081,
                     'Jordan':5110,
                     'Kuwait':5130,
                     'Lebanon':5040,
                     'Libya':7250,
                     'Morocco':7140,
                     'Oman':5230,
                     'Qatar':5180,
                     'Saudi Arabia':5170,
                     'Syria':5020,
                     'Tunisia':7230,
                     'UAE':5200,
                     'Yemen':5210
                    }
    


    result_arr = pull_api(country_code)
    print("Pulled result")

    cty_code = pd.Series(country_code)
    cty_code.to_csv('cty_code.csv', index=False)

    result = pd.concat(result_arr)
    # print(result.describe())
    result.to_csv('result_mena.csv', index=False)
    
if __name__ == '__main__':
    main()