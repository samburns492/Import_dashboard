import pandas as pd

def main():
    
    #Algeria
    df_algeria = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=7210')
    #Bahrain
    df_bahrain = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5250')
    #Egypt
    df_egypt = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=7290')
    #Iran
    df_iran = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5070')
    #Iraq
    df_iraq = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5050')
    #Israel
    df_israel = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5081')
    #Jordan
    df_jordan = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5110')
    #Kuwait
    df_kuwait = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5130')
    #Lebanon
    df_lebanon = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5040')
    #Libya
    df_libya = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=7250')
    #Morocco
    df_morocco = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=7140')
    #Oman
    df_oman = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5230')
    #Qatar
    df_qatar = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5180')
    #Saudi Arabia
    df_saudi = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5170')
    #Syria
    df_syria = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5020')
    #Tunisia
    df_tunisia = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=7230')
    #UAE
    df_uae = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5200')
    #Palestine
    #df_gaza = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5082')
    #&
    #df_westbank = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5083')
    #Yemen
    df_yemen = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_LDESC,GEN_VAL_MO,GEN_VAL_YR&time=2013-03&CTY_CODE=5210')
    
    print(df_yemen)

if __name__ == '__main__':
    main()