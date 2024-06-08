import pandas as pd

def main():
    country_code = {'Algeria':7210,
                    'Bahrain':5250,
                    'Egypt':7290,
                    'Iran':5070,
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

    cty_code = pd.Series(country_code)
    cty_code.to_csv('cty_code.csv', index=False)

    print(cty_code)
    # #Algeria
    df_algeria = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=' + str(cty_code['Algeria']))
    # #Bahrain
    # df_bahrain = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5250')
    # #Egypt
    # df_egypt = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=7290')
    # #Iran
    # df_iran = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5070')
    # #Iraq
    # df_iraq = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5050')
    # #Israel
    # df_israel = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5081')
    # #Jordan
    # df_jordan = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5110')
    # #Kuwait
    # df_kuwait = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5130')
    # #Lebanon
    # df_lebanon = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5040')
    # #Libya
    # df_libya = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=7250')
    # #Morocco
    # df_morocco = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=7140')
    # #Oman
    # df_oman = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5230')
    # #Qatar
    # df_qatar = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5180')
    # #Saudi Arabia
    # df_saudi = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5170')
    # #Syria
    # df_syria = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5020')
    # #Tunisia
    # df_tunisia = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=7230')
    # #UAE
    # df_uae = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5200')
    # #Palestine
    # #df_gaza = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5082')
    # #&
    # #df_westbank = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5083')
    # #Yemen
    # df_yemen = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5210')
    

    # result_arr =      [df_algeria,
    #                    df_bahrain,
    #                    df_egypt,
    #                    df_iran,
    #                    df_iraq,
    #                    df_israel,
    #                    df_jordan,
    #                    df_kuwait,
    #                    df_lebanon,
    #                    df_libya,
    #                    df_morocco,
    #                    df_oman,
    #                    df_qatar,
    #                    df_saudi,
    #                    df_syria,
    #                    df_tunisia,
    #                    df_uae,
    #                    df_yemen]
    # result = pd.concat(result_arr)
    print(df_algeria)
    # print(result.describe())
    # result.to_csv('result_mena.csv', index=False)
    
if __name__ == '__main__':
    main()