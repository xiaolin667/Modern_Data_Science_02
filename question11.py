import pandas as pd

def extract_data():
    import pandas as pd
    # fig1
    data = {
        "Year": [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        "Enrolments": [8816, 9329, 9490, 10400, 11024, 11753, 12595, 13723, 15043, 16108, 17800, 19237, 19935, 21033,
                       22897]
    }

    df1 = pd.DataFrame(data)
    df1.name = "Indigenous student enrolments, 2006 to 2020"

    # fig2

    data = {
        "Year": [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        "Share of Enrolments": [1.22, 1.25, 1.25, 1.30, 1.30, 1.34, 1.37, 1.41, 1.48, 1.56, 1.69, 1.80, 1.86, 1.95,
                                2.04]
    }

    df2 = pd.DataFrame(data)
    df2.name = "Share of Indigenous student enrolments, 2006 to 2020"

    # fig 3

    data = {
        "Year": [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        "Indigenous Students Growth": [6.0, 2.0, 10.0, 6.0, 6.0, 4.5, 9.0, 10.0, 7.0, 10.0, 8.0, 2.0, 5.0, 10.0],
        "Non-Indigenous Students Growth": [3.0, 1.0, 5.0, 3.5, 1.0, 2.5, 2.0, 1.5, 1.0, 2.0, 1.0, 0.5, 1.0, 4.0]
    }

    df3 = pd.DataFrame(data)
    df3.name = "Annual growth in Indigenous student enrolments, 2007 to 2020"

    #fig3-2

    data = {
        "Year": [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        "Indigenous Students Growth": [6.0, 2.5, 8.0, 7.0, 6.0, 7.5, 9.0, 10.5, 7.0, 8.5, 8.0, 3.0, 5.5, 9.0],
        "Non-Indigenous Students Growth": [4.0, 0.5, 3.5, 4.5, 1.5, 3.0, 2.0, 1.0, 0.5, 1.0, 0.5, 0.0, 0.0, 2.0]
    }

    df3_2 = pd.DataFrame(data)
    df3_2.name = "Domestic undergraduate enrolments"

    # fig 4
    data = {
        "Discipline": [
            "Natural and Physical Sciences", "Information Technology", "Engineering and Related Technologies",
            "Architecture and Building", "Agriculture, Environmental and Related Studies", "Health",
            "Education", "Management and Commerce", "Society and Culture", "Creative Arts",
            "Mixed Field Programs", "Non-award courses"
        ],
        "Indigenous": [5.5, 2.1, 6.9, 0.7, 1.4,21.2, 12.6, 9.4, 32.2, 7.0, 0.3, 0.7],
        "Non-Indigenous": [8.9, 2.9, 7.8, 1.3, 1.5, 10.1, 15.4, 24.6, 19.4, 6.4, 0.3, 1.5]
    }

    df4 = pd.DataFrame(data)
    df4.name = "Enrolments by broad disciplines, 2020"

    # table 1

    data = {
        "Course level": [
            "Postgraduate research", "Postgraduate coursework", "Bachelor",
            "Sub-bachelor", "Enabling", "Non-award", "All courses"
        ],
        "2008": [393, 1138, 6352, 686, 871, 50, 9490],
        "2020": [751, 3330, 15291, 1268, 2097, 160, 22897],
        "Growth since 2008": ["91%", "193%", "141%", "85%", "141%", "220%", "141%"],
        "Annual average growth since 2008": ["5.5%", "9.4%", "7.6%", "5.3%", "7.6%", "10.2%", "7.6%"]
    }

    tab1 = pd.DataFrame(data)
    tab1.name = "Indigenous enrolments by course level, 2008 and 2020"

    # fig5

    data = {
        "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
        "Indigenous": [6.7, 12.7, 8.6, 8.9, 5.0, -4.9, -2.3, 7.9, 1.1],
        "Non-Indigenous": [1.2, 2.2, 2.7, 2.3, 1.4, -1.4, -2.3, 3.3, 2.4]
    }

    df5 = pd.DataFrame(data)
    df5.name = "Annual growth in undergraduate applications, 2013 to 2021"

    # fig 6

    data = {
        "Age Group": ["15 to 19", "20 to 24", "25 to 39", "40 to 64"],
        "Indigenous": [56, 21, 17, 6],
        "Non-Indigenous": [41, 23, 26, 10]
    }

    df6 = pd.DataFrame(data)
    df6.name = "Share of undergraduate applications, by age, 2021"

    # fig7

    data = {
        "Age Group": ["15 to 19", "20 to 24", "25 to 39", "40 to 64"],
        "Indigenous applications": [1.6, 2.3, 3.2, 3.6],
        "Indigenous population": [5.8, 5.0, 3.3, 2.4]
    }

    df7 = pd.DataFrame(data)
    df7.name = "Share of Indigenous undergraduate applications compared to share of Indigenous population, by age, 2021"

    # fig8
    data = {
            "Category": ["Indigenous", "Indigenous", "Non-Indigenous", "Non-Indigenous"],
            "Gender": ["Male", "Female", "Male", "Female"],
            "Percentage": [28, 72, 39, 61]
        }
    df8 = pd.DataFrame(data)
    df8.name = "Share of undergraduate applications, by gender, 2021"

    data = {
        "Year": ["2021", "2020", "2012"],
        "Natural and Physical Sciences": [6.1, 6.6, 5.6],
        "Information Technology": [0, 0, 0],
        "Engineering and Related Technologies": [0, 0, 0],
        "Architecture and Building": [0, 0, 0],
        "Agriculture, Environmental and Related Studies": [0, 0, 0],
        "Health": [33.7, 29.4, 24.0],
        "Education": [12.7, 12.9, 16.3],
        "Management and Commerce": [5.5, 7.1, 8.1],
        "Society and Culture": [30.1, 29.8, 30.3],
        "Creative Arts": [4.9, 6.4, 7.9],
        "Mixed field programs": [0, 0, 0]
    }

    df9 = pd.DataFrame(data)
    df9.name = "Share of Indigenous undergraduate applications by broad disciplines, 2012, 2020 and 2021"

    # fig10
    data = {
        "Year": list(range(2001, 2021)),
        "Bachelor": [500, 550, 600, 650, 700, 750, 800, 830, 860, 900, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600,
                     1800, 2000],
        "Sub-bachelor": [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 250, 260, 270, 280, 300, 320,
                         340],
        "PG Coursework": [50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 350, 400, 500, 600, 700, 800, 900, 1000, 1200,
                          1400],
        "PG Research": [10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
    }

    df10 = pd.DataFrame(data)
    df10.name = "Number of award course completions by Indigenous students, by course level"

    # fig11
    data = {
        "Cohort": ["2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012"],
        "Indigenous students": [46.5, 47.2, 47.1, 47.9, 47.7, 47.8, 47.5, 49.4],
        "Non-Indigenous students": [73.9, 73.9, 74.0, 74.4, 74.3, 73.5, 73.4, 72.2]
    }

    df11 = pd.DataFrame(data)
    df11.name = "Nine-year completion rates of commencing Indigenous and non-Indigenous Bachelor degree students"

    # fig12
    import pandas as pd

    data = {
        "Cohort": [
            "2005", "2006", "2007", "2008",
            "2009", "2010", "2011", "2012",
            "2013", "2014", "2015", "2016",
            "2017"
        ],
        "Percentage": [
            25.8, 21.9, 22.9, 20.0, 19.9, 20.7, 20.7, 20.2,
            19.1, 19.5, 18.5, 18.4, 20.4
        ]
    }

    # df_Share_of_Indigenous_students_commencing_a_Bachelor_degree_that_never_return_after_four_years = pd.DataFrame(data)
    df12 = pd.DataFrame(data)
    df12.name = "Nine-year completion rates of commencing Indigenous and non-Indigenous Bachelor degree students"

    #fig13
    data = {
        'Year': ['2008', '2018', '2019', '2020'],
        'Indigenous Success Rates': [68.8, 71.1, 71.2, 72.5],
        'Non-Indigenous Success Rates': [85.6, 84.7, 85.1, 86.1],
        'Indigenous Retention Rates': [74.0, 72.4, 73.9, 76.5],
        'Non-Indigenous Retention Rates': [87.4, 85.1, 85.4, 86.8]
    }

    df13 = pd.DataFrame(data)
    df13.name = "Retention and success rates of domestic Bachelor degree students, Indigenous vs non-Indigenous, per cent"

    # fig14
    data = {
        'Coursework': ['Undergraduate', 'Undergraduate', 'Undergraduate', 'Undergraduate',
                       'Postgraduate coursework', 'Postgraduate coursework', 'Postgraduate coursework',
                       'Postgraduate coursework'],
        'Employment Type': ['Full-time', 'Full-time', 'Overall', 'Overall',
                            'Full-time', 'Full-time', 'Overall', 'Overall'],
        'Category': ['Indigenous', 'Non-Indigenous', 'Indigenous', 'Non-Indigenous',
                     'Indigenous', 'Non-Indigenous', 'Indigenous', 'Non-Indigenous'],
        'Percentage': [76.8, 68.8, 85.7, 84.7, 87.9, 84.9, 92.5, 90.8]
    }

    df14 = pd.DataFrame(data)
    df14.name = "Short-term graduate employment outcomes, 2021"

    # fig15

    data = {
        'Coursework': ['Undergraduate', 'Undergraduate', 'Undergraduate', 'Undergraduate',
                       'Postgraduate coursework', 'Postgraduate coursework', 'Postgraduate coursework',
                       'Postgraduate coursework'],
        'Employment Type': ['Full-time', 'Full-time', 'Overall', 'Overall',
                            'Full-time', 'Full-time', 'Overall', 'Overall'],
        'Category': ['Indigenous', 'Non-Indigenous', 'Indigenous', 'Non-Indigenous',
                     'Indigenous', 'Non-Indigenous', 'Indigenous', 'Non-Indigenous'],
        'Percentage': [77.0, 89.7, 74.3, 88.9, 91.4, 98.0, 86.5, 93.2]
    }

    df15 = pd.DataFrame(data)
    df15.name = "Short and medium-term full-time employment outcomes, for 2018 graduates"

    #fig16
    data = {
        'Year': [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
        'Level A': [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520],
        'Level B': [180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500],
        'Level C': [160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480],
        'Level D and above': [140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460],
        'Non-academic': [800, 820, 840, 860, 880, 900, 920, 940, 960, 980, 1000, 1020, 1040, 1060, 1080, 1100, 1120]
    }

    df16 = pd.DataFrame(data)
    df16.name = "Number of Indigenous staff by duties classification, 2005 to 2021"

    #fig17
    data = {
        'Year': [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
        'Indigenous Academic': [0.6, 0.65, 0.7, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3,
                                1.35],
        'Indigenous Non-Academic': [0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5,
                                    1.55, 1.6],
        'All Indigenous Staff': [0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6,
                                 1.65]
    }

    df17 = pd.DataFrame(data)
    df17.name = "Share of Indigenous staff, 2005 to 2021"

    # fig18
    data = {
        'Year': [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
        'Level A': [5, 5, 5, 6, 6, 5, 6, 6, 5, 5, 6, 6, 6, 5, 5, 6, 6],
        'Level B': [10, 10, 10, 11, 11, 10, 11, 11, 10, 10, 11, 11, 11, 10, 10, 11, 11],
        'Level C': [15, 15, 15, 14, 14, 15, 14, 14, 15, 15, 14, 14, 14, 15, 15, 14, 14],
        'Level D and above': [20, 20, 20, 19, 19, 20, 19, 19, 20, 20, 19, 19, 19, 20, 20, 19, 19],
        'Non-academic': [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
    }

    df18 = pd.DataFrame(data)
    df18.name = "Proportion of Indigenous staff by duties classification, 2005 to 2021"

   # fig 19
    data = {
        'Duties Classification': ['Level A', 'Level B', 'Level C', 'Level D and above', 'All academic staff',
                                  'Non-academic'],
        'Indigenous Staff': [64.3, 66.7, 67.0, 57.1, 64.0, 71.8],
        'Non-Indigenous Staff': [52.7, 55.7, 48.7, 36.8, 48.0, 66.4]
    }

    df19 = pd.DataFrame(data)
    df19.name = "Share of female staff by duties classification, 2021"

    # fig20
    data = {
        'Duties Classification': ['Level A', 'Level B', 'Level C', 'Level D and above', 'All academic staff',
                                  'Non-academic'],
        'Indigenous Staff': [53.5, 29.1, 17.4, 5.0, 27.1, 52.0],
        'Non-Indigenous Staff': [70.5, 42.7, 20.4, 3.9, 31.0, 40.5]
    }

    df20 = pd.DataFrame(data)
    df20.name = "Proportion of staff aged under 40 by duties classification, 2021"

    # fig21
    data = {
        'Year': ['2005', '2005', '2010', '2010', '2021', '2021'],
        'Category': ['Indigenous', 'Non-Indigenous', 'Indigenous', 'Non-Indigenous', 'Indigenous', 'Non-Indigenous'],
        'Level A': [27.7, 19.5, 20.4, 18.3, 23.3, 17.5],
        'Level B': [43.3, 33.8, 41.2, 33.3, 35.5, 30.1],
        'Level C': [17.0, 24.1, 18.3, 23.1, 18.6, 22.6],
        'Level D and above': [12.1, 22.6, 20.1, 25.3, 22.6, 29.7]
    }

    df21 = pd.DataFrame(data)
    df21.name = "Share of staff by academic duties classification, 2005, 2010 and 2021"

    # fig22
    data = {
        'Year': ['2005', '2005', '2010', '2010', '2021', '2021'],
        'Category': ['Indigenous', 'Non-Indigenous', 'Indigenous', 'Non-Indigenous', 'Indigenous', 'Non-Indigenous'],
        'Teaching and Research': [80.6, 68.0, 73.7, 63.8, 53.7, 53.4],
        'Research Only': [13.9, 29.1, 20.2, 32.2, 29.8, 35.3],
        'Teaching Only': [5.6, 3.0, 6.0, 4.0, 16.5, 11.3]
    }

    df22 = pd.DataFrame(data)
    df22.name = "Share of staff by academic functions, 2005, 2010 and 2021"

    # fig23
    data = {
        'Function': ['Teaching-only', 'Research-only', 'Teaching and research', 'Other function'],
        'Indigenous Staff (actual numbers)': [99, 179, 323, 1079],
        'Population Parity Figure': [189, 590, 893, 2068]
    }

    df23 = pd.DataFrame(data)
    df23.name = "Indigenous staff, actual vs population parity figures, 2021"


    # fig24
    data = {
        'Year': [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        'Postgraduate Research': [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400],
        'Postgraduate Coursework': [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300,
                                    2400, 2500]
    }

    df24 = pd.DataFrame(data)
    df24.name = "Indigenous postgraduate enrolments, 2005 to 2020"

    # fig25
    data = {
        'Year': [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        'Postgraduate Research': [0.8, 0.82, 0.85, 0.87, 0.88, 0.9, 0.92, 0.95, 0.97, 1.0, 1.05, 1.1, 1.15, 1.2, 1.3,
                                  1.4],
        'Postgraduate Coursework': [0.6, 0.62, 0.64, 0.67, 0.69, 0.7, 0.73, 0.75, 0.77, 0.8, 0.85, 0.9, 0.95, 1.0, 1.1,
                                    1.2]
    }

    df25 = pd.DataFrame(data)
    df25.name = "Share of Indigenous postgraduate enrolments, 2005 to 2020"

    # fig 26
    data = {
        'Year': [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        'Postgraduate Research': [0.4, 0.45, 0.5, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.85, 0.8, 0.95, 1.0, 1.2, 1.3],
        'Postgraduate Coursework': [0.5, 0.55, 0.6, 0.65, 0.7, 0.8, 0.85, 0.9, 0.8, 0.7, 0.75, 0.8, 1.0, 1.15, 1.3,
                                    1.25]
    }

    df26 = pd.DataFrame(data)
    df26.name = "Share of Indigenous postgraduate award completions, 2005 to 2020"

    # fig27
    data = {
        'Category': ['Postgraduate research', 'Postgraduate coursework', 'Postgraduate research',
                     'Postgraduate coursework'],
        'Type': ['Enrolment', 'Enrolment', 'Award completions', 'Award completions'],
        'Actual Indigenous Students': [743, 3017, 71, 764],
        'Population Parity Figure': [1308, 6258, 194, 2009]
    }

    df27 = pd.DataFrame(data)
    df27.name = "Indigenous postgraduate student, actual and population parity figures, 2020"

    dataframes_dict = {
        'df1': {'dataframe': df1, 'name': df1.name},
        'df2': {'dataframe': df2, 'name': df2.name},
        'df3': {'dataframe': df3, 'name': df3.name},
        'df3_2': {'dataframe': df3_2, 'name': df3_2.name},
        'df4': {'dataframe': df4, 'name': df4.name},
        'tab1': {'dataframe': tab1, 'name': tab1.name},
        'df5': {'dataframe': df5, 'name': df5.name},
        'df6': {'dataframe': df6, 'name': df6.name},
        'df7': {'dataframe': df7, 'name': df7.name},
        'df8': {'dataframe': df8, 'name': df8.name},
        'df9': {'dataframe': df9, 'name': df9.name},
        'df10': {'dataframe': df10, 'name': df10.name},
        'df11': {'dataframe': df11, 'name': df11.name},
        'df12': {'dataframe': df12, 'name': df12.name},
        'df13': {'dataframe': df13, 'name': df13.name},
        'df14': {'dataframe': df14, 'name': df14.name},
        'df15': {'dataframe': df15, 'name': df15.name},
        'df16': {'dataframe': df16, 'name': df16.name},
        'df17': {'dataframe': df17, 'name': df17.name},
        'df18': {'dataframe': df18, 'name': df18.name},
        'df19': {'dataframe': df19, 'name': df19.name},
        'df20': {'dataframe': df20, 'name': df20.name},
        'df21': {'dataframe': df21, 'name': df21.name},
        'df22': {'dataframe': df22, 'name': df22.name},
        'df23': {'dataframe': df23, 'name': df23.name},
        'df24': {'dataframe': df24, 'name': df24.name},
        'df25': {'dataframe': df25, 'name': df25.name},
        'df26': {'dataframe': df26, 'name': df26.name},
        'df27': {'dataframe': df27, 'name': df27.name}
    }

    return dataframes_dict
    # return (df1,df2,df3, df3_2, df4,tab1, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14,
    #         df15, df16, df17, df18, df19, df20, df21, df22, df23, df24, df25, df26, df27)




if __name__ == "__main__":
    dataframes_dict = extract_data()
    # df1, df2, df3, df3_2, df4, tab1, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15,
    # df16, df17, df18, df19, df20, df21, df22, df23, df24, df25, df26, df27 = extract_data()
    names = [df_info['name'] for df_info in dataframes_dict.values()]
    for name in names:
        print(name)
    # analyse combine table 1 and fig 11,/f13
    # table1: the growth of indigenous enrolments 2008 and 2020
    # predict the enrolments through 2008 to 2012 by annual average growth
    # combine with fig11， calculate the incompletion rate/ number 2008 to 2012

    # analyse combin fig 4 and fig 9 .
    # the difference between application and enrolments in 2020
    # which disciplines are the most popular,
    # may be combine the completion rate by broad disciplines
    # to see if students encounters difficulties in different disciplines

    # combine fig 14 and fig 15
    # calculate the difference between short and medium term ,


print("13")