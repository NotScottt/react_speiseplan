from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os, os.path
import pandas as pd
import fitz
from datetime import datetime, timedelta
import re
import pandas

current_date = datetime.now()
year, week_num, day_of_week = current_date.isocalendar()
username = os.getlogin()

today = datetime.now()
year = today.year
kw = today.strftime("%W")
current_calendar_week = today.strftime("%W")
needed_month = today - timedelta(days = today.weekday())

new_month = today - relativedelta(months=1)
new_month = new_month.strftime("%m")

if len(str(needed_month.month)) == 1:
    month = f"0{needed_month.month}"
else:
    month = needed_month.month

date_minus_one = datetime.today() - relativedelta(month=1)
if len(str(date_minus_one.month)) == 1:
    month_minus_one = f"0{date_minus_one.month}"
else:
    month_minus_one = date_minus_one.month

def crawl_file_for(url, string):
    required_url = url
    required_str = string

    doc_cont = requests.get(required_url)
    soup = BeautifulSoup(doc_cont.content, 'lxml')
    
    for current_speiseplan_list in soup.find_all("a", href=lambda href: href and required_str in href):
        ultimate_link_final = current_speiseplan_list["href"]

    # try:
    return ultimate_link_final
    
    # except UnboundLocalError:
    #     print(f"Kein Wert vorhanden für {string}")

def get_current_melexis():
    melexis_year = str(today.year)[2:]

    melexis_plan = crawl_file_for("https://www.essecke-erfurt.de/mittagsverpflegung/essecke-melexis/", f"Speiseplan+{current_calendar_week}.{melexis_year}.pdf")
    return melexis_plan

def get_current_sportklinik():
    month_today = today
    month_today = month_today.strftime("%m")

    try:
        sportklinik_plan = crawl_file_for("https://sportklinik-erfurt.de/klinik/", f"{today.year}/{month_today}/Kw{current_calendar_week}.pdf")

    except:
        sportklinik_plan = crawl_file_for("https://sportklinik-erfurt.de/klinik/", f"{today.year}/{new_month}/Kw{current_calendar_week}.pdf")

    return sportklinik_plan

def get_current_guka():
    try:
        guka_plan = crawl_file_for("https://gulaschkanone-erfurt.de/speiseplan/", f"Sued-Ost-KW-{new_month}.pdf")
    
    except:
        guka_plan = crawl_file_for("https://gulaschkanone-erfurt.de/speiseplan/", f"Sued-Ost-KW-{current_calendar_week}.pdf")

    return guka_plan


this_kw = today.isocalendar().week


def get_date_from_week_and_weekday(weekday_number):
  first_day_of_year = datetime.strptime(f"{today.year}-01-01", "%Y-%m-%d")
  iso_week = first_day_of_year.isocalendar().week
  week_offset = this_kw - iso_week
  days_since_year_start = week_offset * 7 + weekday_number - 1
  
  return first_day_of_year + timedelta(days=days_since_year_start)

def get_essen_dataframe(pdf_link):
    response = requests.get(pdf_link)
    pdf_cont = response.content

    document = fitz.open(stream=pdf_cont, filetype="pdf")

    for page in document:
        tabs = page.find_tables()
        if tabs.tables:
            result_df = tabs[0].to_pandas()
        
    return result_df


def find_prices_melexis(melexis_df):
    regex_for_melexis = r"(?<=Essen\s[A-C]\s)\d+,\d\d"
    price_df_melexis = melexis_df.iloc[0]

    price_df_melexis = pd.DataFrame(price_df_melexis)
    results = []
    for i in range(price_df_melexis.shape[0]):
        for j in range(price_df_melexis.shape[1]):
            matches = re.findall(regex_for_melexis, price_df_melexis.iloc[i, j])
            results.extend(matches)

    return results

def find_sportklinik_preise(sportklinik_df):
    regex = r"([0-9,.]+)"
    sportklinik_dataframe_prices = sportklinik_df.columns[1:]

    prices = []
    for item in list(sportklinik_dataframe_prices):
        preis = re.findall(regex, item)
        if preis:
            prices.append(preis[0])
    
    return prices

pdf_file_link_guka = get_current_guka()
guka_dataframe = get_essen_dataframe(pdf_file_link_guka)

pdf_file_link_guka = get_current_guka()
guka_dataframe = get_essen_dataframe(pdf_file_link_guka)

def transform_guka_plan(guka_df):
    new_df = pandas.DataFrame()
    essen_a_list = []
    essen_b_list = []

    new_df['Datum'] = guka_df.columns
    for i in range(0, 5):
        essen_a_list.append(guka_df.iloc[0][i])
        essen_b_list.append(guka_df.iloc[2][i])
    
    
    new_df["Essen A"] = essen_a_list
    new_df["Essen B"] = essen_b_list
    new_df["Essen C"] = ""
    new_df["Suppe"] = ""
    
    new_df = new_df.replace(["Scan mich:", None], regex=True)
    return new_df

# print(transform_guka_plan(guka_dataframe))