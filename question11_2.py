
from question11 import extract_data
import math
def enrolment(dataframes_dict):
    import pandas as pd

    # Extract the dataframe from the dictionary
    table1 = dataframes_dict['tab1']['dataframe']

    # Calculate enrollments for each year from 2008 to 2020
    years = range(2008, 2021)
    result_list = []

    for _, row in table1.iterrows():
        course_level = row['Course level']
        initial_enrollment = row['2008']
        annual_growth_rate = float(row['Annual average growth since 2008'].replace('%', ''))/100

        enrollments = {
            'Course level': course_level
        }

        for year in years:
            if year == 2008:
                enrollments[year] = initial_enrollment
            else:
                enrollments[year] = math.ceil(enrollments[year - 1] * (1 + annual_growth_rate))

        result_list.append(enrollments)

    # Create and return the final DataFrame
    result_df = pd.DataFrame(result_list)
    result_df = result_df.set_index('Course level')

    return result_df

def enrolments_by_course_plot(result_df):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 6))
    years = range(2008, 2021)

    for index, row in result_df.iloc[:5].iterrows():
        plt.plot(years, row.values, label=index, marker='o')

    plt.title('Enrollments from 2008 to 2020')
    plt.xlabel('Year')
    plt.ylabel('Enrollments')
    plt.legend(title='Course Level')
    plt.grid(True)
    plt.savefig("enrolment_by_course_2008_2020.png")

    return plt.gcf()

def pred_dropout_bachelor(dataframes_dict,enrolment_course ):
    import pandas as pd
    import  math
    df11 = dataframes_dict['df11']['dataframe']
    mean_completion_rate = df11.iloc[:,1:2].mean()
    bachelor_enrolments = enrolment_course.iloc[2:3,:]
    expected_dropout = (bachelor_enrolments *(1- mean_completion_rate.values[0]/100)).applymap(math.ceil)

    return  expected_dropout, bachelor_enrolments

def pred_dropout_plot(df1,df2):
    import pandas as pd
    import matplotlib.pyplot as plt
    df1 = df1.T
    df1.columns = ['Bachelor enrolment']

    df2 =df2.T
    df2.columns = ['Expected Dropout']
    combined_df = pd.concat([df1, df2], axis=1)
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot bar chart
    combined_df.plot(kind='bar', ax=ax, width=0.7, color=['blue', 'red'])

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Values')
    ax.set_title('Indigenous Enrolment and Predicted Nine-Year Drop out Bachelor students, 2008 to 2020')
    ax.legend()

    # Display the plot
    plt.tight_layout()
    plt.savefig("predicted_bachelor_dropout")
    # plt.show()
    return plt.gcf()

def enrolment_discipline(dataframes_dict):
    df4 = dataframes_dict['df4']['dataframe']
    tab1 = dataframes_dict['tab1']['dataframe']
    # df4_first_two_cols = df4.iloc[:, :2]

    # Step 2: Calculate the sum of Bachelor, Sub-bachelor, Enabling for 2020 from tab1
    selected_courses = ['Bachelor', 'Sub-bachelor', 'Enabling','Non-award']
    sum_courses_2020 = tab1.loc[tab1['Course level'].isin(selected_courses), '2020'].sum()

    # Step 3: Calculate the actual enrollment for every discipline
    df4['Actual Enrolment'] = (df4['Indigenous']/100 * sum_courses_2020).apply(math.ceil)

    # Store the results into a new DataFrame
    result_df = df4[['Discipline','Indigenous', 'Actual Enrolment']]

    return result_df

def enrolment_discipline_plot(df):
    import matplotlib.pyplot as plt
    df['Indigenous'] = df['Indigenous'] / 100

    # Set the figure size
    plt.figure(figsize=(14, 8))

    # Bar Chart
    plt.bar(df['Discipline'], df['Actual Enrolment'], color='orange', label='Actual Enrolment')

    # Create a second y-axis for the line chart
    ax2 = plt.gca().twinx()
    ax2.plot(df['Discipline'], df['Indigenous'], marker='o', color='b', label='Indigenous (%)')
    ax2.set_ylabel('Indigenous (%)')

    # Set axis labels and title
    plt.xticks(rotation=45, ha='right', fontsize=10, wrap=True)
    plt.title('Actual Enrolment and Percentage by Discipline, 2020')
    plt.ylabel('Number of Enrolments')

    # Show legends
    plt.subplots_adjust(bottom=0.3)
    plt.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Adjust layout
    plt.tight_layout()
    # plt.show()
    plt.savefig("enrolement_by_discipline.png")

    return plt.gcf()


if __name__ == "__main__":
    dataframes_dict = extract_data()
    # enrolment by course level
    enrolment_course = enrolment(dataframes_dict)
    enrolment_course.to_csv('indigenous_enrolments_by_course_2008_to_2020.csv')
    enrolments_by_course_plot = enrolments_by_course_plot(enrolment_course)

    # predict the Nine-Year dropout number of bachelor students
    expected_dropout_bachelor, bachelor_enrolments =pred_dropout_bachelor(dataframes_dict,enrolment_course)
    dropout_plot = pred_dropout_plot(bachelor_enrolments,expected_dropout_bachelor)

    # enrolment by board discipline 2020
    enrolment_discipline =enrolment_discipline(dataframes_dict)
    enrolment_discipline_plot = enrolment_discipline_plot(enrolment_discipline)

print("15")