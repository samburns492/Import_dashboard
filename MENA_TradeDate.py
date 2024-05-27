import pandas as pd

def main():
    df = pd.read_json('https://api.census.gov/data/timeseries/intltrade/imports/hs?get=I_COMMODITY,I_COMMODITY_SDESC,I_COMMODITY_LDESC,CTY_CODE,CTY_NAME,GEN_VAL_MO,GEN_VAL_YR&time=2013-03')
    print(df)

if __name__ == '__main__':
    main()