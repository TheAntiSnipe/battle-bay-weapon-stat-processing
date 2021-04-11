from os import write
import pandas as pd


def rename_dataframe(given_dataframe):
    return given_dataframe.rename(columns={
        'CostID': 'Rarity and levels',
        'Cost1': 'Sugar',
        'Cost2': 'Common parts',
        'Cost3': 'Uncommon parts',
        'Cost4': 'Rare parts',
        'Cost5': 'Epic parts',
        'Cost6': 'Legendary parts'
    }
    )
    #! The first stage of decoding the document:
    #  The meanings of each column are rewritten onto the intermediate dataframe.


def replace_codewords(dataframe_to_process):
    replacement_keys = ['R1_', 'R2_', 'R3_', 'R4_', 'R5_',
                        'E1_COST', 'E2_COST', 'E3_COST', 'E4_COST', 'E5_COST']
    #! The above is the standard codewording scheme used to denote the values below.
    replacement_values = ['Common ', 'Uncommon ', 'Rare ', 'Epic ', 'Legendary ',
                          'level 1-10', 'level 11-20', 'level 21-30', 'level 31-40', 'level 41-50']
    replacement_dictionary = dict(zip(replacement_keys, replacement_values))

    for initial_text in replacement_dictionary.keys():
        final_text = replacement_dictionary.get(initial_text)
        dataframe_to_process = dataframe_to_process.replace(
            to_replace=initial_text, value=final_text, regex=True)

    return dataframe_to_process
    #! The second stage of decoding the document:
    #  All codewording is removed and replaced with natural language.


def generate_level_list():
    level_list = []
    for rarities in range(5):
        print(rarities)
        initial_level = 1
        while(initial_level != 50):
            if(initial_level % 10 != 0):
                level_list.append(initial_level)
            initial_level += 1
    return pd.DataFrame(level_list)
    #! Levels were labelled incorrectly.
    #  Thus, they were generated programmatically.


def aggregate_by(given_dataframe, operation):
    tier_grouped_dataframe = given_dataframe.groupby(
        by='Rarity and levels', sort=False)

    return tier_grouped_dataframe.agg({
        'Sugar': operation,
        'Common parts': operation,
        'Uncommon parts': operation,
        'Rare parts': operation,
        'Epic parts': operation,
        'Legendary parts': operation})
    #! The final stage of level rush chart generation:
    #  Every ten levels are grouped together and costs are summated.


def write_dataframe_to_file(dataframe_to_write, filename,index_flag):
    data = open(filename, 'w')
    data.write(dataframe_to_write.to_csv(
        index=index_flag, line_terminator='\n'))
    data.close()
    #! Writes to file without indices and empty spaces.


def main():
    print("Beginning processing")
    original_dataframe = pd.read_csv('costs-per-level.csv')
    selected_dataframe = original_dataframe[[
        'CostID', 'Level', 'Cost1', 'Cost2', 'Cost3', 'Cost4', 'Cost5', 'Cost6']]

    renamed_dataframe = rename_dataframe(selected_dataframe)

    processed_readable_dataframe = replace_codewords(renamed_dataframe)

    processed_readable_dataframe['Level'] = generate_level_list()

    write_dataframe_to_file(processed_readable_dataframe, 'levelup-chart.csv',False)
    # * First output: A raw levelup chart containing the
    # * level requirements to upgrade anything by one level.

    final_level_rush_dataframe = aggregate_by(
        processed_readable_dataframe, 'sum')

    write_dataframe_to_file(final_level_rush_dataframe, 'level-rush-chart.csv',True)
    # * Second output: A final level rush chart containing the
    # * aggregated data of every 1o levels combined.

if(__name__=='__main__'):
    main()